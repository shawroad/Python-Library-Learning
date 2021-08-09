"""
@file   : 002-IndexIVFFlat检索.py
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

    nlist = 100
    k = 4
    quantizer = faiss.IndexFlatL2(d)
    # 量化器索引
    index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)
    # 指定用L2距离进行搜索，若不指定默认为內积
    assert not index.is_trained
    index.train(xb)
    # 索引训练
    assert index.is_trained
    index.add(xb)
    # 向量添加
    D, I = index.search(xq, k)
    # 检索
    print(I[:5])
