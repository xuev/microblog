#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author:  xuev (xuewei918@gmail.com)
@Project: microblog
@File: __init__.py
@Version: 0.01
@License: MIT Licence
@Create Time: 2017/3/1 下午6:59
@Description: 
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
