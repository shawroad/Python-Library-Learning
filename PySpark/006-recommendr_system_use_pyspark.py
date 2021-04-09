"""
@file   : 006-recommendr_system_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-09
"""
import findspark

findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import rand
from pyspark.ml.feature import StringIndexer, IndexToString
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator


def analyse_data(df):
    '''
    数据分析
    :param df:
    :return:
    '''
    print(df.printSchema())  # 查看数据格式

    # 看前5条数据
    print(df.show(5))

    print(df.orderBy(rand()).show(5))  # 将数据打乱 看前五条

    # 与用户进行聚合，看每个用户都看过多少电影  前五名最爱看电影的人
    print(df.groupBy('userId').count().orderBy('count', ascending=False).show(5))

    # 显示前五个最热门的电影
    print(df.groupBy('title').count().orderBy('count', ascending=False).show(5))


def feature_process(df):
    '''
    特征工程
    :param df:
    :return:
    '''
    # 1. 将title转为数字  也就是多加了一列特征
    stringIndexer = StringIndexer(inputCol="title", outputCol="title_new")
    model = stringIndexer.fit(df)
    indexed = model.transform(df)
    print(indexed.show(5))
    return indexed


if __name__ == '__main__':
    # 1. 加载数据
    spark = SparkSession.builder.appName('rc').getOrCreate()
    df = spark.read.csv('./data/movie_ratings_df.csv', inferSchema=True, header=True)
    # print((df.count(), len(df.columns)))    # (100000, 3)

    # 2. 数据分析
    analyse_data(df)

    # 3. 特征工程
    model_df = feature_process(df)
    # 切分数据集
    train, test = model_df.randomSplit([0.75, 0.25])
    print('训练集条数:', train.count())
    print('测试集条数:', test.count())
    # 训练集条数: 74996
    # 测试集条数: 25004

    # 4. 模型训练
    rec = ALS(maxIter=10, regParam=0.01, userCol='userId',
              itemCol='title_new', ratingCol='rating',
              nonnegative=True, coldStartStrategy="drop")
    rec_model = rec.fit(train)

    # 5. 模型评估
    predicted_ratings = rec_model.transform(test)
    print(predicted_ratings.printSchema())

    # 计算预测和rating的均方误差
    evaluator=RegressionEvaluator(metricName='rmse',predictionCol='prediction',labelCol='rating')
    rmse=evaluator.evaluate(predicted_ratings)
    print(rmse)

