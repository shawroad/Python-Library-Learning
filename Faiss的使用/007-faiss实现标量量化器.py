"""
@file   : 007-faiss实现标量量化器.py
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

    x = data
    # 训练集
    x_train = data
    # QT_8bit allocates 8 bits per dimension (QT_4bit also works)
    sq = faiss.ScalarQuantizer(d, faiss.ScalarQuantizer.QT_8bit)
    sq.train(x_train)

    # encode 编码
    codes = sq.compute_codes(x)

    # decode 解码
    x2 = sq.decode(codes)

    # 计算编码-解码后与原始数据的差
    avg_relative_error = ((x - x2)**2).sum() / (x ** 2).sum()
    print(avg_relative_error)