"""
# -*- coding: utf-8 -*-
# @File    : ltp的使用.py
# @Time    : 2020/11/25 9:20 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
from ltp import LTP
# 安装ltp: pip install ltp -i https://pypi.douban.com/simple/
# 学习文档: http://ltp.ai/docs/quickstart.html


def fenju():
    # 分句子
    sents = ltp.sent_split(["他叫汤姆去拿外衣。", "汤姆生病了。他去了医院。"])
    print(sents)


def fenci():
    # 可以加载自己的词表
    ltp.init_dict(path='my_vocab.txt', max_window=4)
    segment, _ = ltp.seg(['我是你爸，我是你妈'])
    print(segment)


def cixingbiaozhu():
    seg, hidden = ltp.seg(['他叫汤姆去拿外衣。'])
    pos = ltp.pos(hidden)
    print(seg)
    print(pos)


def mingmingshitishibie():
    seg, hidden = ltp.seg(['他叫汤姆去拿外衣。孙悟空不同意咋办? 但是奥特曼肯定会同意'])
    ner = ltp.ner(hidden)
    print(seg)
    print(ner)

    for i in ner[0]:
        tag = i[0]
        name = seg[0][i[1]: i[2]+1]
        print(tag, ":", name)


def yuyijuesebiaozhu():
    seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
    srl = ltp.srl(hidden)
    print(srl)  # 包含了空

    srl = ltp.srl(hidden, keep_empty=False)
    print(srl)


def yicunjufafenxi():
    seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
    dep = ltp.dep(hidden)
    print(dep)


def yicunjufashu():
    seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
    sdp = ltp.sdp(hidden, graph=False)
    print(sdp)


def yicunjufafenxitu():
    seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
    sdp = ltp.sdp(hidden, graph=True)
    print(sdp)





if __name__ == '__main__':
    ltp = LTP()   # ltp = LTP(path = "base|small|tiny")  默认下载small

    # 1. 分句
    # fenju()

    # 2. 分词
    # fenci()

    # 3. 词性标注
    # cixingbiaozhu()

    # 4. 命名实体识别
    # mingmingshitishibie()

    # 5. 语义角色标注
    # yuyijuesebiaozhu()

    # 6. 依存句法分析
    # yicunjufafenxi()

    # 7. 依存句法树
    yicunjufashu()

    # 8. 依存句法分析(图)
    yicunjufafenxitu()









