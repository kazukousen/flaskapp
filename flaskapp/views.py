# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals

from flask import Flask, render_template, request
from flaskapp import app

@app.route('/')
def trump_operation():
    '''
    formで入力されたactionの値{random, sort}によって,
    トランプの操作を行う
    '''
    _action = request.args.get('action')

    return render_template('trump.html', result=_action)
