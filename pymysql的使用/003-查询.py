"""
# -*- coding: utf-8 -*-
# @File    : 003-查询.py
# @Time    : 2020/11/24 2:34 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
import pymysql

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect("localhost", "xxxxxx", "xxxxxxx", "TESTDB")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
    try:
        cursor.execute(sql)

        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print('fname: {}, lname:{}, age:{}, sex:{}, income:{}'.format(fname, lname, age, sex, income))
    except:
        print("啥也找不到")

    # 关闭数据库连接
    db.close()