"""
@file   : 003-plot_zhuzhuangtu.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-12-29
"""
import pandas as pd
import pandas_bokeh


if __name__ == '__main__':
    data = {
        'fruits':
        ['苹果', '梨', '草莓', '西瓜', '葡萄', '香蕉'],
        '2015': [2, 1, 4, 3, 2, 4],
        '2016': [5, 3, 3, 2, 4, 6],
        '2017': [3, 2, 4, 4, 5, 3]
    }
    df = pd.DataFrame(data).set_index("fruits")   # 设置水果为索引

    p_bar = df.plot_bokeh.bar(
        ylabel="每斤的的价格 [￥]",
        title="水果每年的价格",
        alpha=0.6)