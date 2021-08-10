"""
@file   : 005-faiss实现pca降维.py
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

    mat = faiss.PCAMatrix(512, 64)  # 从512维降为64维
    mat.train(data)
    assert mat.is_trained
    tr = mat.apply_py(data)
    print(tr.shape)
    print(tr)

