"""
@file   : 002-plot_sandiantu.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-12-29
"""
import pandas as pd
import pandas_bokeh

if __name__ == '__main__':
    # 随便造一些数据
    df = pd.DataFrame({
        'length': [5.1, 4.9, 4.7, 4.6, 5., 5.4, 4.6, 5., 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7],
        'width': [3.5, 3., 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3., 3., 4., 4.4],
        'label': [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1]
    })

    p_scatter = df.plot_bokeh.scatter(
        x="length",
        y="width",
        category="label",   # 如果有类别 还可以jia
        title="随便一画",
        show_figure=True,
    )