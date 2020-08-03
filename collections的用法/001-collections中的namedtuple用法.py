# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 15:57
# @Author  : xiaolu
# @FileName: 001-collections中的namedtuple用法.py
# @Software: PyCharm

# 我的认识 感觉nametuple是一种便捷类的使用
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
# 相当于定义了一个Point类，其中x, y为类的属性
p = Point(1, 2)
print(p.x)
print(p.y)


# 在深度学习中 我们可以定义参数文件
from collections import namedtuple
Config = namedtuple('Config', ['learning_rate',
                               'epoch',
                               'device',
                               'batch_size',
                               'vocab_size'])


config = Config(
    learning_rate=1e-5,
    epoch=10,
    device=4,
    batch_size=32,
    vocab_size=12239
)
print(config.learning_rate)


