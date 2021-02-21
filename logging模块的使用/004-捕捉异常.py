"""
@file   : 004-捕捉异常.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-21
"""
import os.path
import time
import logging

if __name__ == '__main__':
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关

    # 创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    os.makedirs(log_path, exist_ok=True)
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    # 定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # 使用logger.XX来记录错误,这里的"error"可以根据所需要的级别进行修改
    try:
        open('/path/to/does/not/exist', 'rb')
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error('Failed to open file', exc_info=True)
