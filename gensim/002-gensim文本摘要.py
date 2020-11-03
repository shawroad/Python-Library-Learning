# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/3 14:43
@Auth ： xiaolu
@File ：002-gensim文本摘要.py
@IDE ：PyCharm
@Email：luxiaonlp@163.com
"""
import re
from LAC import LAC
from gensim.summarization.summarizer import summarize


def clean(content):
    content = content.replace('.', '')
    content = content.replace(' ', '')
    content = content.replace('\n', '.')
    return content


def process_data(text, lac):
    # 首先对text进行分句子  主要防止摘要为半句话
    text = re.split('[.。？！]', text)

    sentences = []
    for t in text:
        if len(t) == 0:
            continue
        t = lac.run(t)
        sentences.append(' '.join(t))

    # 最后用.将句子连起来
    return '. '.join(sentences)


if __name__ == '__main__':
    lac = LAC(mode='seg')

    # 1. 加载文章
    data = []
    with open('./data/text.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            line = process_data(line, lac)
            line = summarize(line)
            line = clean(line)
            print('*' * 20 + '第{}篇文章的摘要'.format(i + 1) + '*' * 20)
            print(line)




















