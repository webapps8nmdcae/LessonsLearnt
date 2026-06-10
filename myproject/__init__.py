import os
import urllib

from flask import Flask, redirect, url_for, request, render_template, jsonify, json, Blueprint, flash, abort, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security, current_user
import pymssql
from datetime import timedelta
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'


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

from myproject.LessonsLearnt.views import lessons_learnt_blueprint
from myproject.error_pages.handlers import error_pages

app.register_blueprint(lessons_learnt_blueprint)
app.register_blueprint(error_pages)

# @app.route('/')
# def index():
#     return redirect(url_for('LessonsLearnt.newlesson'))
