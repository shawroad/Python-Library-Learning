"""
@file   : 002-日志控制台输出.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-21
"""
import logging  # 引入logging模块
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,   # 输出的最低级别
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
    # asctime是时间 filename是当前文件夹 lineno 行号  levelname 什么级别的错误  massage输出的信息
    # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
    logging.info('this is a loggging info message')
    logging.debug('this is a loggging debug message')
    logging.warning('this is loggging a warning message')
    logging.error('this is an loggging error message')
    logging.critical('this is a loggging critical message')
