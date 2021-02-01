"""
@file   : 003-多线程锁机制.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-01
"""
import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    with lock:
        if account.balance >= amount:
            # time.sleep(0.1)   # 如果不加锁，这里休息0.1秒，每次都会出问题，因为这里会引起线程阻塞，一定会切换
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)
        else:
            print(threading.current_thread().name,
                  "取钱失败，余额不足")


if __name__ == "__main__":
    account = Account(1000)    # 金额

    # 启动两个线程  分别去800块
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))

    ta.start()
    tb.start()