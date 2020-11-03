# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/3 14:09
@Auth ： xiaolu
@File ：002-词性标注和实体识别.py
@IDE ：PyCharm
@Email：luxiaonlp@163.com
"""
from LAC import LAC


if __name__ == '__main__':
    lac = LAC(mode='lac')
    text = '我想涨工资'

    lac_result = lac.run(text)
    print(lac_result)

    texts = ["汤青松长得好帅", "我喜欢做安全开发工程师"]
    lac_result = lac.run(texts)
    print(lac_result)






