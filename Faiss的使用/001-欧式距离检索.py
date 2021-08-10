"""
@file   : 001-欧式距离检索.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-08-09
"""
import faiss
import numpy as np


if __name__ == '__main__':
    n_data, d = 1000, 512   # 检索库中的向量个数, 每个向量的维度
    np.random.seed(43)   # 随机种子 为了多次执行结果一致

    # 检索库的构造
    data = []
    mu, sigma = 3, 0.1   # 这里时通过高斯分布随机产生若干向量，这两个参数为均值和方差
    for i in range(n_data):
        data.append(np.random.normal(mu, sigma, d))
    data = np.array(data).astype('float32')   # faiss只支持32位的浮点数

    # 检索向量的生成
    query = []
    n_query = 10   # 生成10个query向量
    mu, sigma = 3, 0.1
    np.random.seed(12)
    for i in range(n_query):
        query.append(np.random.normal(mu, sigma, d))
    query = np.array(query).astype('float32')

    # 构建索引  记住要传入向量维度d
    index = faiss.IndexFlatL2(d)
    # print(index.is_trained)    # 这里若是false就要训练  后面讲

    # 添加数据
    index.add(data)
    # print(index.ntotal)   # 总的数据量

    # 开始检索
    k = 10   # 指定让其返回10个距离最近的

    # 这里我们选取data中的前五个 容易看到结果，因为自己跟自己距离肯定为0 所以最相关的肯定是自己
    query_self = data[:5]

    dis, ind = index.search(query_self, k=k)
    print(dis)   # 每条数据代表了当前这个query 与最相关的十个数据的距离
    print(ind)   # 每条数据代表了当前这个query 最相关的十条数据的索引
    """
    [[0.        8.55197   8.634906  8.683499  8.698736  8.821949  8.902446
      8.943979  8.9516735 8.972908 ]
     [0.        8.369204  8.482748  8.53028   8.581224  8.680499  8.684254
      8.697291  8.719812  8.753435 ]
     [0.        8.209936  8.392483  8.456179  8.473589  8.480727  8.551348
      8.553277  8.576391  8.592704 ]
     [0.        8.473689  8.621014  8.827385  8.883725  8.980131  8.99064
      9.015673  9.017438  9.027972 ]
     [0.        8.268832  8.349455  8.597895  8.611757  8.658188  8.675722
      8.685029  8.70588   8.707612 ]]
    [[  0 877 502  42 606 366 348 923 563  56]
     [  1 849 974 106 348 364 877 242 280 173]
     [  2 877 127 655 253 233 558 678  13 208]
     [  3 421  94 348 502 402 536 646 563 735]
     [  4 986 230 209 446 889 974 241 550 248]]
     """



