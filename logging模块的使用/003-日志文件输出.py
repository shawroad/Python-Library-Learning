"""
@file   : 003-日志文件输出.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-21
"""
import logging  # 引入logging模块
import os.path
import time

if __name__ == '__main__':
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    os.makedirs(log_path, exist_ok=True)   # 创建文件夹
    log_name = log_path + rq + '.log'   # 日志名
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)

    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)

    # 日志
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')