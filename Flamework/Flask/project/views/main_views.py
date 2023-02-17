# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app, jsonify
from flask import Blueprint, render_template, jsonify
# from flask_uploads import I
from ..db import db


bp = Blueprint('main_views', __name__, url_prefix='/')

# /post/pstId=<int:pstId>
# 특정 게시물로 이동
@bp.route('/')
def grid():
    cursor = db.cursor()
    sql = 'SELECT * FROM FileInfo;'
    cursor.execute(sql)
    question_list = cursor.fetchall()

    # 특정 게시물 html 불러오기
    return jsonify(question_list)

# myproject/pybo/views/question_views.py
	
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
        f.save(f.filename)  
        return render_template("pages/success.html", name = f.filename)  
    
