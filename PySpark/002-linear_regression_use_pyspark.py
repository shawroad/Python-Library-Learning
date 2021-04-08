"""
@file   : 002-linear_regression_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-08
"""
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import corr
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression


def analyse_data(df):
    '''
    数据分析
    :param df:
    :return:
    '''
    # 打印数据格式
    print(df.printSchema())

    # 打印前十条数据
    print(df.head(10))

    # 看某个特征与输出的相关系数   var_1与output的相关系数
    print(df.select(corr('var_1', 'output')).show())   # 0.9187399607627283


def feature_process(df):
    '''
    特征工程
    :param df:
    :return:
    '''
    # 将var_1到var2合成一个向量，名字叫做features
    vec_assmebler = VectorAssembler(inputCols=['var_1', 'var_2', 'var_3', 'var_4', 'var_5'], outputCol='features')
    features_df = vec_assmebler.transform(df)
    # print(features_df.select('features').show(5))   # 看features的取值

    model_df = features_df.select('features', 'output')   # 将features和输出拿出来  进行模型训练
    # print(model_df.show(5))
    return model_df


if __name__ == '__main__':
    # 1. 加载数据集
    spark = SparkSession.builder.appName('lin_reg').getOrCreate()
    df = spark.read.csv('./data/Linear_regression_dataset.csv', inferSchema=True, header=True)
    # print('数据量:{}, 特征数:{}'.format(df.count(), len(df.columns)))   # 数据量:1232, 特征数:6

    # 2. 数据分析
    # analyse_data(df)   如果进行数据分析  执行该函数

    # 3. 特征工程
    model_df = feature_process(df)   # 将各个特征的值合并成一个向量
    # 划分数据
    train_df, test_df = model_df.randomSplit([0.7, 0.3])
    # print('训练集---数据量:{}, 特征数:{}'.format(train_df.count(), len(train_df.columns)))   # 数据量:868, 特征数:2
    # print('测试集---数据量:{}, 特征数:{}'.format(test_df.count(), len(test_df.columns)))   # 数据量:364, 特征数:2

    # 4. 模型训练
    lin_Reg = LinearRegression(labelCol='output')
    lr_model = lin_Reg.fit(train_df)

    # 5. 模型评价
    # 模型训练完毕 打印回归系数
    print(lr_model.coefficients)

    training_predictions = lr_model.evaluate(train_df)
    print('训练集的均方误差:', training_predictions.meanSquaredError)
    # 训练集的均方误差: 0.00014265219879599827

    testing_predictions = lr_model.evaluate(test_df)
    print('测试集的均方误差:', testing_predictions.meanSquaredError)
    # 测试集的均方误差: 0.00014983739298532136




























