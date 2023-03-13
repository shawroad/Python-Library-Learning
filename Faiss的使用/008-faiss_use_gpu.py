"""
@file   : 008-faiss_use_gpu.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-08-25
"""
import faiss
import numpy as np
import time


if __name__ == '__main__':
    d = 512   # 向量维度
    nb = 300000   # 向量库的大小
    nq = 100   # 用这100个向量进行检索

    np.random.seed(1234)

    # 随机产生一个向量库
    xb = np.random.random((nb,d)).astype('float32')
    xb[:, 0] += np.arange(nb) / 1000.

    # 随机产生100个query向量
    xq = np.random.random((nq,d)).astype('float32')
    xq[:, 0] += np.arange(nq) / 1000.

    quantizer = faiss.IndexFlatL2(d)
    nlist = 100   # 将数据库向量分割为多少了维诺空间
    index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)

    gpu_index = faiss.index_cpu_to_all_gpus(index)   # 使用gpu也就是这行代码就行了
    print(gpu_index.is_trained)
    gpu_index.train(xb)
    print(gpu_index.is_trained)

    gpu_index.add(xb)
    gpu_index.nprobe = 10   # 选择10个维诺空间进行索引
    k = 10    # 返回十个结果
    D, gt_nms = gpu_index.search(xq, k)
    print(gt_nms)