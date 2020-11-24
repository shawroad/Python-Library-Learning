"""
# -*- coding: utf-8 -*-
# @File    : 004-更新.py
# @Time    : 2020/11/24 2:41 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
import pymysql

if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.connect("localhost", "xxxxxx", "xxxxxx", "TESTDB")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句  给男性加1岁
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()