#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author:  xuev (xuewei918@gmail.com)
@Project: microblog
@File: config.py
@Version: 0.01
@License: MIT Licence
@Create Time: 2017/3/1 下午7:52
@Description: 
"""

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]