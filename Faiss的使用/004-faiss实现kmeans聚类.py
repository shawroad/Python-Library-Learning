"""
@file   : 004-faiss实现kmeans聚类.py
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

    # 聚类
    n_centroids = 1024    # 聚类中心个数
    d = data.shape[1]
    kmeans = faiss.Kmeans(d, n_centroids)
    kmeans.train(data)
    # 输出聚类中心
    # print(kmeans.centroids)
    # print(len(kmeans.centroids))

    # 看data中的前五个向量属于那个类(最有可能的两个类)
    D, I = kmeans.index.search(data[:5], k=2)
    print(D)   # 与每个类的距离
    print(I)   # 类的编号
    """
    输出:
    [[4.1553707 5.2924204]
     [1.9329664 4.930997 ]
     [4.537619  4.8509283]
     [4.6700296 5.2252126]
     [2.101182  4.9292693]]
    [[478 568]
     [767 697]
     [568 527]
     [999 568]
     [175 853]]
    """

    print('*'*100)
    # 计算每个中心最近的若干条向量
    k = 5
    index = faiss.IndexFlatL2(d)
    index.add(data)
    D, I = index.search(kmeans.centroids, k)
    print(D)
    print(I)



