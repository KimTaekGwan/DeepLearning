# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app, jsonify
from flask import Blueprint, render_template, jsonify

from project.db import db
from project.module import *

import os
import json
from tqdm import tqdm


bp = Blueprint('main_views', __name__, url_prefix='/')

util = Util()
ppt = PPT_Info_Extract()
pdf = PDF_Info_Extract()


@bp.route('/')
def grid():
    cursor = db.cursor()
    sql = 'SELECT * FROM FileInfo;'
    cursor.execute(sql)
    question_list = cursor.fetchall()

    return jsonify(question_list)

	
@bp.route('/list')
def ss_list():
    question_list = {}
    cursor = db.cursor()
    number = 5
    page = request.args.get('page', type=int, default=1)

    sql = 'SELECT * FROM FileInfo LIMIT {} OFFSET {};'.format(number, number * (page - 1))
    cursor.execute(sql)
    item  = cursor.fetchall()

    sql = 'SELECT count(*) as count FROM FileInfo;'
    cursor.execute(sql)
    get_length = cursor.fetchone()

    max_page = (get_length['count'] - 1) // number + 1
    
    question_list['item'] = item
    question_list['max_page'] = list(range(1,max_page+1))
    question_list['page'] = page
    question_list['total'] = get_length['count']
    question_list['number'] = number
    
    return render_template('pages/list.html', question_list=question_list)


@bp.route('/upload')  
def upload():  
    return render_template("pages/file_upload_form.html")  


@bp.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        # print(f.filename, f, '\n')
        
        path = 'data/input/' + f.filename
        f.save(path)
        
        util.dir_Update(f.filename)
        
        name, ext = os.path.splitext(f.filename)
        if ext == '.pdf':
            pdf.extract(f.filename)
            pdf.preprocessing()
            res = {'noun':pdf.pre_text}

        elif ext in ['.pptx', '.ppt']:
            ppt.extract(f.filename)
            ppt.preprocessing()
            res = {'noun':ppt.pre_text}
        
        res = json.dumps(res, ensure_ascii=False)
        
        return render_template("pages/success.html", name = f.filename, res=res)