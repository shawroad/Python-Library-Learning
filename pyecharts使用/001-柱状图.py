"""
@file   : 001-柱状图.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-17
"""
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


bar = (
    Bar({"theme": ThemeType.MACARONS})   # 设置主题
    # Bar()
        .set_global_opts(
        title_opts=opts.TitleOpts(title="各种衣服价格", subtitle="VS"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))  # 名字倾斜15度
    )

        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [5, 20, 36, 10, 75, 90])

)
bar.render('柱状图.html')