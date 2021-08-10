"""
@file   : 002-倒排表快速索引.py
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

    nlist = 50  # 将数据库向量分割为多少了维诺空间
    k = 10
    quantizer = faiss.IndexFlatL2(d)  # 量化器
    index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)  # METRIC_L2计算L2距离, 或faiss.METRIC_INNER_PRODUCT计算内积
    assert not index.is_trained  # 倒排表索引类型需要训练
    index.train(data)  # 训练数据集应该与数据库数据集同分布
    assert index.is_trained

    index.add(data)
    index.nprobe = 2  # 选择n个维诺空间进行索引,
    dis, ind = index.search(query, k)
    print(dis)
    print(ind)
