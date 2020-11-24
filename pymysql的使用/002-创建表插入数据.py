"""
# -*- coding: utf-8 -*-
# @File    : 002-创建表插入数据.py
# @Time    : 2020/11/24 2:20 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
import pymysql

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect("localhost", "xxxxx", "xxxxxxx", "TESTDB")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    sql = '''CREATE TABLE EMPLOYEE (
                FIRST_NAME CHAR (20) NOT NULL,
                LAST_NAME CHAR (20),
                AGE INT,
                SEX CHAR (1),
                INCOME FLOAT 
                )
    '''
    cursor.execute(sql)

    # 接着插入数据
    insert_sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
                    VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    try:
        # 执行sql语句
        cursor.execute(insert_sql)
        # 提交到数据库执行
        db.commit()
    except:
        print('滚犊子,插不进去')
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()