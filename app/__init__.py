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

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
