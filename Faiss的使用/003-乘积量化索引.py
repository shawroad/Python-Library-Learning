"""
@file   : 003-乘积量化索引.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-08-09
"""
import numpy as np
import faiss

if __name__ == '__main__':
    n_data, d = 1000, 512  # 检索库中的向量个数, 每个向量的维度
    np.random.seed(43)  # 随机种子 为了多次执行结果一致

    # 检索库的构造
    data = []
    mu, sigma = 3, 0.1  # 这里时通过高斯分布随机产生若干向量，这两个参数为均值和方差
    for i in range(n_data):
        data.append(np.random.normal(mu, sigma, d))
    data = np.array(data).astype('float32')  # faiss只支持32位的浮点数

    # 检索向量的生成
    query = []
    n_query = 10  # 生成10个query向量
    mu, sigma = 3, 0.1
    np.random.seed(12)
    for i in range(n_query):
        query.append(np.random.normal(mu, sigma, d))
    query = np.array(query).astype('float32')

    nlist = 50
    m = 8  # 列方向划分个数，必须能被d整除
    k = 10
    quantizer = faiss.IndexFlatL2(d)
    index = faiss.IndexIVFPQ(quantizer, d, nlist, m, 4)   # 4 表示每个子向量被编码为 4 bits

    index.train(data)
    index.add(data)
    index.nprobe = 50
    dis, ind = index.search(data[:10], k)  # 查询自身
    print(dis)
    print(ind)

    dis, ind = index.search(query, k)  # 真实查询
    print(dis)
    print(ind)
