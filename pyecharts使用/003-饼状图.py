"""
@file   : 003-饼状图.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-17
"""
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


if __name__ == '__main__':
    # 生成假数据
    # a, b = Faker.choose(), Faker.values()
    # print(a)
    # print(b)
    # ['可乐', '雪碧', '橙汁', '绿茶', '奶茶', '百威', '青岛']
    # [97, 140, 75, 28, 89, 20, 143]
    pie = (
        Pie()
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))

            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])

            .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])  # 每个所占面积的颜色设置

            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))  # 标签显示的样子
    )
    pie.render("饼状图.html")
