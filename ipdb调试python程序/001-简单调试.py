# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 10:04
# @Author  : xiaolu
# @FileName: 001-简单调试.py
# @Software: PyCharm
from ipdb import set_trace


if __name__ == "__main__":
    a = 0
    b = 1
    for i in range(1, 100, 2):
        a += i
        b *= i
        set_trace()


# ipdb> print(a)
# 1
# ipdb> print(b)
# 1
# 接下来输入n   每输入一次 往后执行一行

# 假设输入两次n  此时的a=4   b=1    输三次n 此时的a=4  b=3
