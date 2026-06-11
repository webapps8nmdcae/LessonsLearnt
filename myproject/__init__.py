import os
import urllib

from flask import Flask, redirect, request, render_template, jsonify, json, Blueprint, flash, abort, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security, current_user
import pymssql
from datetime import timedelta
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

# class PrefixMiddleware(object):
#     def __init__(self, app, *prefix):
#         self.app = app
#         self.prefixes = list(prefix)
#
#     def __call__(self, environ, start_response):
#         for i in self.prefixes:
#             if environ.get('PATH_INFO', '').startswith(i):
#                 environ['PATH_INFO'] = environ['PATH_INFO'][len(i):]
#                 environ['SCRIPT_NAME'] = i
#                 return self.app(environ, start_response)
#         start_response('404', [('Content-Type', 'text/plain')])
#         return [b"The url does not belong to the app."]
#
# app.wsgi_app = PrefixMiddleware(app.wsgi_app, '/LessonsLearnt')


app.config['SQLALCHEMY_BINDS'] = {
    'WebApps': 'mssql+pymssql://webapps:*nmdc_12345@DMDBSrv.nmdc.local/WebappsDB'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_PASSWORD_SALT'] = 'aslkfj909'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
db = SQLAlchemy(app, session_options={"autoflush": False})

base_url='https://webapps.nmdc.ae'

#############################################################################################
######################## FLASK SECURITY #####################################################
#############################################################################################
# from myproject.models import *
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

from myproject.lessons.views import lessons_learnt_blueprint
from myproject.error_pages.handlers import error_pages

app.register_blueprint(lessons_learnt_blueprint, url_prefix='/lessons')
app.register_blueprint(error_pages)

# @app.route('/')
# def index():
#     return redirect('/LessonsLearnt/lessons/newlesson')
