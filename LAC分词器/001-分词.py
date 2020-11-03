# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/3 14:06
@Auth ： xiaolu
@File ：001-分词.py
@IDE ：PyCharm
@Email：luxiaonlp@163.com
"""
from LAC import LAC
import jieba


if __name__ == '__main__':
    lac = LAC(mode='seg')

    # 单个样本输入, 输入为unicode编码的字符串
    text = '大王叫我来巡山'
    lac_result = lac.run(text)
    print(lac_result)

    jieba_result = jieba.lcut(text)
    print(jieba_result)

    # 批量样本输入, 输入为多个句子组成的list，平均速率会更快
    texts = ["山里有个庙", "庙里有个老和尚跟一个小和尚"]
    result = lac.run(texts)
    print(result)



