"""
@file   : 001-plot_zhexiantu.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-12-29
"""
# 安装pandas以及pandas_bokeh   # pip install pandas_bokeh pandas
import numpy as np
import pandas as pd
import pandas_bokeh

# 注意  文件名字不要夹带中文

if __name__ == '__main__':
    np.random.seed(55)
    df = pd.DataFrame({"宁德时代": np.random.randn(100)+0.2,
                       "贵州茅台": np.random.randn(100)+0.17},
                      index=pd.date_range('1/1/2021', periods=100))
    df = df.cumsum()   # 累加
    df = df + 50
    df.plot_bokeh.line(
        figsize=(800, 450),   # 图片的大小
        title="宁德时代 vs 贵州茅台",   # 表名
        xlabel="日期",    # 横坐标的名字
        ylabel="股票价格 [$]",   # 纵坐标的名字
        # yticks=[0, 100, 200, 300, 400],   #  y轴的虚线  可以不带
        ylim=(45, 80),   # y轴范围
        xlim=("2021-01-01", "2021-04-01"),  # x轴的范围
        colormap=["red", "blue"],
        plot_data_points=True,   # 标记每个值
        plot_data_points_size=5,
        marker="asterisk")
