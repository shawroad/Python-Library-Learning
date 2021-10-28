"""
@file   : 定时任务.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-10-27
"""
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job(text):
    print('{}'.format(text), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    sched = BlockingScheduler()
    # sched.add_job(my_job, 'interval', days=0, hours=24, minutes=0, seconds=0)  # 每隔24小时执行一次
    # sched.add_job(my_job, 'interval', seconds=5, args=['北京时间:'])   # 每个5秒执行 用interval

    # 指定某个时间点执行一次
    sched.add_job(my_job, 'date', run_date=datetime(2021, 10, 27, 17, 8, 5), args=['北京时间:'])
    sched.start()