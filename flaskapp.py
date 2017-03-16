# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals

from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update({'DEBUG': True })

@app.route('/')
def random_create():
    _action = request.args.get('action')

    return render_template('trump.html', result=_action)

if __name__ == '__main__':
    app.run()
