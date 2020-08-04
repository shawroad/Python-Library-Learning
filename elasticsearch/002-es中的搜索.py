# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 15:52
# @Author  : xiaolu
# @FileName: 002-es中的搜索.py
# @Software: PyCharm
from elasticsearch import Elasticsearch


if __name__ == '__main__':
    es = Elasticsearch()
    querys = '东临碣石'
    dsl = {
        'query': {
            'match': {
                'title': '咏鹅'
            }
        }
    }
    results = es.search(index='point_type', body=dsl)['hits']['hits']  # 搜索多条结果的话 这里可能是一个列表

    res = []
    for result in results:
        res.append(result['_source'])
    print(res)

