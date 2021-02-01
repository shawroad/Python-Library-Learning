"""
@file   : 002-生产者消费者实现多线程爬虫.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-01
"""
import queue
import time
import random
import threading
import requests
from bs4 import BeautifulSoup


def craw(url):
    # 爬取网页内容
    r = requests.get(url)
    return r.text


def parse(html):
    # 解析其中的内容
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]   # 那链接和标题拿出来


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    '''
    生产者
    :param url_queue: url的队列  生产者从中拿出链接  去爬虫
    :param html_queue:  生产者将爬取的内容放到这里
    :return:
    '''
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)
        print('线程名: ', threading.current_thread().name,
              "url_queue.size=", url_queue.qsize())   # 获取url队列中还有多少待爬取的
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    '''
    消费者
    :param html_queue: 生产者生产出的内容
    :param fout: 消费者将内容解析出来  存到fout中
    :return:
    '''
    while True:
        html = html_queue.get()
        results = parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print('线程名: ', threading.current_thread().name,
              "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    # 待爬取的网页链接
    urls = [
        "https://www.cnblogs.com/sitehome/p/{}".format(page) for page in range(1, 50 + 1)
    ]

    url_queue = queue.Queue()
    html_queue = queue.Queue()

    # 将url放进队列中
    for url in urls:
        url_queue.put(url)

    # 启动三个线程去做生产者
    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name="craw{}".format(idx))
        t.start()

    fout = open("data.txt", "w")
    # 启动两个线程去做消费者
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name="parse{}".format(idx))
        t.start()
