from flask import Flask, render_template, session, redirect, url_for, jsonify

from flask import request
from datetime import timedelta

from .views import (main_views)
# flask의 create_app - Flask Application Factory
# debug / 
def create_app(debug=False):
	print('----------create_app----------')	
	app = Flask(__name__, template_folder='templates')
	app.secret_key = 'secretkey' 

	# Blueprint views를 app에 등록
	app.register_blueprint(main_views.bp)

	# socketio.init_app(app) 추가

	return app