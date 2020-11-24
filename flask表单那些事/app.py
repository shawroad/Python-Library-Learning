"""
# -*- coding: utf-8 -*-
# @File    : app.py
# @Time    : 2020/11/19 3:54 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def my_index():
    user_name = request.form.get('username')
    if user_name is not None:
        pass_word = request.form.get('pwd')
        sex = request.form.getlist('sex')
        property = request.form.getlist('property')
        content = request.form.get('content')
        print(content)
        print(user_name)
        print(pass_word)
        print(sex)
        print(property)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

