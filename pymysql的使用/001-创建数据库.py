"""
# -*- coding: utf-8 -*-
# @File    : 001-创建数据库.py
# @Time    : 2020/11/24 1:59 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
import pymysql

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect('localhost', 'xxxxx', 'xxxxxx')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 创建数据库
    db_name = 'TESTDB'
    sql = "CREATE DATABASE {}".format(db_name)   # 创建数据库
    cursor.execute(sql)

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用fetchone()方法获取单条数据
    data = cursor.fetchone()
    print("数据库的版本: ", data)
    # 关闭数据库连接
    db.close()