"""
@file   : 001-多线程.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-01
"""
import threading
import time
import requests


def craw(url):
    # 这是个爬虫
    r = requests.get(url)
    print(url, r.status_code)


def single_thread():
    # 单线程爬虫
    print('single_thread start')
    for url in urls:
        craw(url)
    print('single_thread end')


def multi_thread():
    # 多线程爬虫
    print("multi_thread begin")
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))   # url, 之所以加逗号 是因为这里必须为元组
        )

    # 启动多线程
    for thread in threads:
        thread.start()

    # 等待结束
    for thread in threads:
        thread.join()
    print("multi_thread end")


if __name__ == '__main__':
    # 爬50页的内容
    urls = ['https://www.cnblogs.com/sitehome/p/{}'.format(page) for page in range(1, 50 + 1)]

    # 单线程走起
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    # 多线程走起
    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")