"""
@file   : 008-协程爬虫.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-01
"""
import asyncio
import aiohttp
import time


async def async_craw(url):
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")


if __name__ == '__main__':
    urls = [
        "https://www.cnblogs.com/sitehome/p/{}".format(page) for page in range(1, 50 + 1)
    ]

    loop = asyncio.get_event_loop()   # 获取超级循环
    tasks = [loop.create_task(async_craw(url)) for url in urls]  # 建立任务
    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))   # 开始执行
    end = time.time()
    print("use time seconds: ", end - start)