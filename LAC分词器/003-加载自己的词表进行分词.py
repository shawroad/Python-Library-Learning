# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/6 11:18
@Auth ： xiaolu
@File ：001-demo.py
@IDE ：PyCharm
@Email：luxiaonlp@163.com
"""
from LAC import LAC
import jieba

if __name__ == '__main__':
    lac = LAC()
    lac.load_customization('./vocab.txt', sep=None)
    res1 = lac.run('字节跳动阿里巴巴腾讯公司金山软件小米科技')
    res2 = jieba.lcut('字节跳动阿里巴巴腾讯公司金山软件小米科技')
    print(res1)
    print(res2)


