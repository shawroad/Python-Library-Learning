"""
@file   : 001-日志级别的使用.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-21
"""
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)  # 这是级别 输出小于warning级别的信息
    logging.debug('数学')
    logging.info('英语')
    logging.warning('物理')
    logging.error('体育')
    logging.critical('政治')