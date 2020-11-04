# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/4 16:37
@Auth ： xiaolu
@File ：001-关键词提取.py
@IDE ：PyCharm
@Email：luxiaonlp@163.com
"""
from textrank4zh import TextRank4Keyword


if __name__ == '__main__':
    # 加载文本
    data = []
    with open('./data/text.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)

    # 关键词提取
    tr4w = TextRank4Keyword()

    data = data[:1]
    for text in data:
        tr4w.analyze(text=text, lower=True, window=2)
        for item in tr4w.get_keywords(20, word_min_len=1):
            print('{}:{:6f}'.format(item.word, item.weight))

    # 关键短语抽取
    for text in data:
        tr4w.analyze(text=text, lower=True, window=2)
        for phrase in tr4w.get_keyphrases(20, min_occur_num=1):
            print(phrase)







