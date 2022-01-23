"""
@file   : app.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2022-01-08
"""
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/left_data')
def get_left_data():
    day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # nums = [150, 230, 224, 218, 135, 147, 260]
    nums = [random.randint(0, 100) for _ in range(len(day))]
    random.shuffle(nums)
    data = {'day': day, 'nums': nums}
    return jsonify(data)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(port=6000)
    app.run(host='0.0.0.0')