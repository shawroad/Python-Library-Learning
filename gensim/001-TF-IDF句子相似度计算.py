# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 11:47
# @Author  : xiaolu
# @FileName: 001-TF-IDF句子相似度计算.py
# @Software: PyCharm
import jieba
from gensim import corpora, models, similarities

import numpy as np
import linecache


def similarity(query_path, query):
    '''
    :param query_path: 问题库的路径
    :param query: 所提的问题
    :return: 问题库中与当前问题相似的问题索引
    '''
    # 对问题库中的问题处理
    questions = []
    with open(query_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            line = jieba.lcut(line)
            temp = []
            for w in line:
                if w not in stopword:
                    temp.append(w)
            questions.append(temp)

    # 创建词典
    dictionary = corpora.Dictionary(questions)
    # 基于词典，将分词列表集转换成稀疏向量集，即语料库
    questions = [dictionary.doc2bow(ques) for ques in questions]
    # 训练TF-IDF模型，传入语料库进行训练
    tfidf = models.TfidfModel(questions)  # 传入的向量集
    # 用训练好的TF-IDF模型处理被检索文本，即语料库
    corpus_tfidf = tfidf[questions]
    # for temp in corpus_tfidf:  # 每个问题中的每个词的tfidf值
    #     print(temp)
    # 对当前所问问题进行处理

    new_vec = dictionary.doc2bow(query.split())
    new_vec_tfidf = tfidf[new_vec]

    # 计算当前问题与问题库中所有问题的相似度
    index = similarities.MatrixSimilarity(corpus_tfidf)   # 最相似问题
    sims = index[new_vec_tfidf]   # 相似的列表吧
    # print(sims)

    max_loc = np.argmax(sims)    # 最相似的问题(问题库)编号
    max_sim = sims[max_loc]
    # print(max_loc)    # 5   相似问题的编号
    # print(max_sim)   # 1.0  相似程度

    # 句子相似度阈值
    sup = 0.7
    # row_index默认为-1，即未匹配到满足相似度阈值的问题
    row_index = -1
    if max_sim > sup:
        # 相似度最大值对应文件中问题所在的行索引
        row_index = max_loc + 1
    return row_index


def get_answer(answer_path, row_index):
    """
    :func: 得到问题对应的答案
    :param answer_path: 答案存储所在文件路径
    :param row_index: 答案的行索引
    :return:
    """
    answer = linecache.getline(answer_path, row_index)
    return answer


if __name__ == '__main__':
    answer_path = './data/answer.txt'
    query_path = './data/question.txt'

    # 加载停用词
    stopword = []
    with open('./data/stopwords.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            stopword.append(line)
    print('退出请按q')
    while True:
        question = input('>:')
        if question == 'q':
            break

        # 首先分词然后去除停用词
        res = jieba.lcut(question)
        question_sep = []
        for r in res:
            if r not in stopword:
                question_sep.append(r)
        # question_sep 是问题经过分词, 停用词处理后的词表
        query = ' '.join(line for line in question_sep)

        # 得到问题对应的行索引   也就是问题来了  我们先和问题库中的问题匹配  得到问题库中的相似问题
        row_index = similarity(query_path, query)   # 找到相似问题的索引位置了

        answer = get_answer(answer_path, row_index)
        print('<:', answer)
