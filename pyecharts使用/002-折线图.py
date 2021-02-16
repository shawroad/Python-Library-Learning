"""
@file   : 002-折线图.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-02-17
"""
from pyecharts.charts import Line
from pyecharts import options as opts


if __name__ == "__main__":
    x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # x_data = [1, 2, 3, 4, 5, 6, 7]
    y_data = [820, 932, 901, 934, 1290, 1330, 1320]
    y_data2 = [237, 132, 401, 534, 290, 1230, 1120]

    line = (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True),
            title_opts=opts.TitleOpts(title="收入大比拼", pos_left="center"),  # 标题
            legend_opts=opts.LegendOpts(pos_left="right"),   # 线条示例放在右上角
            xaxis_opts=opts.AxisOpts(type_="category", name="星期"),   # 横轴的类型与名字
            # 注意横轴type_等于value 和category的区别
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="收入",
                splitline_opts=opts.SplitLineOpts(is_show=True),   # 是否显示横向格子线
                is_scale=True,
            ),    # 纵轴的类型与名字
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            is_smooth=True,   # 是否进行平滑处理
            series_name="小花收入",    # 标识每条线
            y_axis=y_data,
            symbol="emptyCircle",
            linestyle_opts=opts.LineStyleOpts(width=2),   # 设置线宽
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=True),   # is_show显示是否需要标注数据
        )
            .add_yaxis(
            series_name="王五",    # 标识每条线
            y_axis=y_data2,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=True),   # is_show显示是否需要标注数据

            # 自定义标记
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="自定义标记点", coord=[x_data[2], y_data2[2]], value=y_data2[2])]
            ),
        )

    )
    line.render('折线图.html')
