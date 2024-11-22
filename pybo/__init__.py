#from flask import Flask
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
import os
import config # config.py를 모듈로 불러옴

db = SQLAlchemy() # SQLAlchemy 객체 생성( 다른 모듈에서도 사용하기 위해서 create_app 함수 밖에서 객체를 생성)
migrate = Migrate() # Migrate 객체 생성

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) # 데이터 베이스 설정 파일 읽기

    # ORM
    db.init_app(app) # 객체를 앱에 등록
    migrate.init_app(app, db) # 객체를 앱에 등록
    from . import models

    # Blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    app.config['UPLOAD_FOLDER'] = 'uploads/'

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    return app