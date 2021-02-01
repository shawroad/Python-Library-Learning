"""
@file   : 004-线程池的使用.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-01
"""
import concurrent.futures
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


if __name__ == '__main__':
    # 待爬取的网页链接
    urls = [
        "https://www.cnblogs.com/sitehome/p/{}".format(page) for page in range(1, 50 + 1)
    ]

    # craw
    with concurrent.futures.ThreadPoolExecutor() as pool:
        htmls = pool.map(craw, urls)
        htmls = list(zip(urls, htmls))
        for url, html in htmls:
            print(url, len(html))
    print("craw over")

    # parse
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = {}
        for url, html in htmls:
            future = pool.submit(parse, html)
            futures[future] = url

        # for future, url in futures.items():
        #     print(url, future.result())

        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            print(url, future.result())
