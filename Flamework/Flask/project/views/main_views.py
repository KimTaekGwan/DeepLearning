# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app, jsonify
from flask import Blueprint, render_template

bp = Blueprint('main_views', __name__, url_prefix='/')

# /post/pstId=<int:pstId>
# 특정 게시물로 이동
@bp.route('/')
def grid():
    # 특정 게시물 html 불러오기
    return 'hello'