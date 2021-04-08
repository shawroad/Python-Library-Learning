"""
@file   : 001-data_processing_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-08
"""
import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, DoubleType, IntegerType
from pyspark.sql.functions import udf
from pyspark.sql.functions import pandas_udf, PandasUDFType


def price_range(brand):
    if brand in ['Samsung', 'Apple']:
        return 'High Price'
    elif brand == 'MI':
        return 'Mid Price'
    else:
        return 'Low Price'


def remaining_yrs(age):
    yrs_left = 100-age
    return yrs_left


if __name__ == '__main__':
    # 1. 创建会话对象
    spark = SparkSession.builder.appName('data_processing').getOrCreate()

    # 2. 加载数据
    df = spark.read.csv('./data/sample_data.csv', inferSchema=True, header=True)
    print(df.columns)   # 打印所有特征名: ['ratings', 'age', 'experience', 'family', 'mobile']
    print(df.count())   # 总的数据量: 33

    # 打印数据格式
    print(df.printSchema())

    # 打印前五条数据
    print(df.show(n=5))

    # 打印某两列  的前三条数据
    print(df.select('ratings', 'mobile').show(n=3))

    # 打印数据统计量  也就是每个特征的均值、方差等。
    print(df.describe().show())

    # 新建一列数据
    print(df.withColumn("age_after_10_yrs", (df["age"]+10)).show(5))

    # 将某列数据转换类型  编程新的一列数据
    print(df.withColumn('age_double', df['age'].cast(DoubleType())).show(3, False))

    # 过滤: 指定某个属性的取值，找出该属性取该值的全部数据
    print(df.filter(df['mobile'] == 'Vivo').select('age', 'ratings', 'mobile').show())

    # 多条件过滤
    print(df.filter((df['mobile'] == 'Vivo') & (df['experience'] > 10)).show())

    # 将某个特征下的值去重后，然后显示出来
    print(df.select('mobile').distinct().show())
    print('去重后的取值数:', df.select('mobile').distinct().count())

    # 根据某个特征的取值进行分组
    print(df.groupBy('mobile').count().show())   # 分组统计个数
    print(df.groupBy('mobile').mean().show())   # 分组后 计算每个特征的均值
    print(df.groupBy('mobile').sum().show())    # 分组后 计算每个特征的和
    print(df.groupBy('mobile').agg({'experience': 'sum'}).show())   # 分组后，只对experience特征求和
    print(df.groupBy('mobile').max().show())    # 分组后 计算每个特征的最大值
    print(df.groupBy('mobile').min().show())    # 分组后 计算每个特征的最小值

    # 普通UDF
    # 用户自定义数据函数UDF
    brand_udf = udf(price_range, StringType())  # 两个参数: 用户自定的函数，传输的数据类型
    print(df.withColumn('price_range', brand_udf(df['mobile'])).show())  # 将udf应用在mobile特征上

    # 或者采用lambda表达式
    age_udf = udf(lambda age: "young" if age <= 30 else "senior", StringType())
    print(df.withColumn("age_group", age_udf(df.age)).show())

    # 去掉重复的记录
    print(df.count())
    df = df.dropDuplicates()
    print('去掉重复记录后的数据数:', df.count())

    # 删除某列
    df_new = df.drop('mobile')
    print(df_new.show(5))


















