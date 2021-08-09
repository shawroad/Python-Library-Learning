"""
@file   : 001-使用欧式距离和内积的方式检索.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-08-09
"""
import faiss
import numpy as np


if __name__ == '__main__':
    nb, d = 100, 64    # 100个64维的向量
    np.random.seed(1234)
    xb = np.random.random((nb, d)).astype('float32')
    # print(xb[:2])

    # 为了使随机产生的向量有较大区别进行人工调整向量
    xb[:, 0] += np.arange(nb).astype('float32') / 1000
    # print(xb[:2])

    nq = 10   # 生成十个待查询的向量
    xq = np.random.random((nq, d)).astype('float32')
    xq[:, 0] += np.arange(nq).astype('float32') / 1000   # 同理 为了有区分度 加点噪声

    # 建立索引    IndexFlatL2使用欧式距离
    index = faiss.IndexFlatL2(d)  # 这里要传入向量的维度信息
    # print(index.is_trained)   # index是否被训练

    index.add(xb)   # 添加向量
    print(index.ntotal)   # 看看加入了多少行

    k = 4
    D, I = index.search(xb[:5], k)
    print(D)
    print('*'*100)
    print(I)
    '''
    [[0.        7.2511625 7.9736595 8.278999 ]    # 第一个向量与最相关的前四个向量的L2距离
     [0.        7.4973536 7.647169  7.9029927]
     [0.        7.2815123 8.11772   8.547238 ]
     [0.        7.5279865 7.790914  8.373755 ]
     [0.        7.5328097 7.75144   7.786872 ]]
    ****************************************************************************************************
    [[ 0 78 85 41]   # 对应的索引  第0个向量肯定与它自己最近  看上面的距离 也可以看出其距离就是0  
     [ 1 77 88 98]
     [ 2 13 43 46]
     [ 3 18 64 74]
     [ 4 18 52 61]]
    '''

    index = faiss.IndexFlatIP(d)   # 使用内积的方式
    index.add(xb)
    k = 4
    D, I = index.search(xb[:5], k)
    print(D)
    print('*'*100)
    print(I)
