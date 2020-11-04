# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/4 16:47
@Auth ： xiaolu
@File ：002-摘要抽取.py
@IDE ：PyCharm
@Email：luxiaonlp@163.com
"""
from textrank4zh import TextRank4Sentence

if __name__ == '__main__':
    # 加载文本
    data = []
    with open('./data/text.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)

    # 摘要抽取
    tr4s = TextRank4Sentence()

    data = data[:1]
    for text in data:
        tr4s.analyze(text=text, lower=True, source='all_filters')
        for item in tr4s.get_key_sentences(num=3):
            print(item.index, item.weight, item.sentence)
