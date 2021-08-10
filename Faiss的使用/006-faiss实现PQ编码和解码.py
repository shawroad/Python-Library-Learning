"""
@file   : 006-faiss实现PQ编码和解码.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-08-09
"""
import faiss
import numpy as np


if __name__ == '__main__':
    # 数据
    n_data, d = 2000, 512
    np.random.seed(43)
    data = []
    mu, sigma = 3, 0.1
    for i in range(n_data):
        data.append(np.random.normal(mu, sigma, d))
    data = np.array(data).astype('float32')

    cs = 4  # code size (bytes)
    # 训练数据集
    x = data   # 原始的数据集

    x_train = data  # 训练集
    pq = faiss.ProductQuantizer(d, cs, 8)
    pq.train(x_train)

    # encode编码
    codes = pq.compute_codes(x)

    # decode解码
    x2 = pq.decode(codes)

    # 编码-解码后与原始数据的差
    avg_relative_error = ((x - x2)**2).sum() / (x ** 2).sum()
    print(avg_relative_error)