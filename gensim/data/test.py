# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 10:18
# @Author  : xiaolu
# @FileName: test.py
# @Software: PyCharm
import linecache


path = 'answer.txt'
for i in range(5):
    answer = linecache.getline(path, i)
    answer = answer.strip()
    print(answer)