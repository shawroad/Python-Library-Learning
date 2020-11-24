"""
# -*- coding: utf-8 -*-
# @File    : 005-删除.py
# @Time    : 2020/11/24 2:43 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
import pymysql

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect("localhost", "xxxxxx", "xxxxx", "TESTDB")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()