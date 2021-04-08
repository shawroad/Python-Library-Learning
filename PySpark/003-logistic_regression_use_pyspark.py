"""
@file   : 003-logistic_regression_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-08
"""
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import OneHotEncoder
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator


def analyse_data(df):
    '''
    数据分析
    :param df:
    :return:
    '''
    # 打印数据的格式
    print(df.printSchema())

    # 打印前五条数据
    print(df.show(n=5))

    # 简单看一下各个特征的统计指标
    print(df.describe().show())   # 对于离散值 是不计算均值和方差的

    # 按国家特征进行聚合 看看那个国家样本多
    print(df.groupby('Country').count().show())

    # 看看搜索引擎用户数量谁最高
    print(df.groupby('Platform').count().show())


def feature_process(df):
    '''
    特征工程
    :param df:
    :return:
    '''
    # 这里需要将国家和搜索引擎两个特征转为数值特征
    search_engine_indexer = StringIndexer(inputCol="Platform", outputCol='Platform_Num').fit(df)
    df = search_engine_indexer.transform(df)
    # print(df.show(3))
    search_engine_encoder = OneHotEncoder(inputCol='Platform_Num', outputCol='Platform_Num_Vec').fit(df)
    df = search_engine_encoder.transform(df)
    # print(df.show(3))

    # print('*'*150)
    # 然后处理国家特征
    country_indexer = StringIndexer(inputCol="Country", outputCol='Country_Num').fit(df)
    df = country_indexer.transform(df)
    # print(df.show(3))
    country_encoder = OneHotEncoder(inputCol='Country_Num', outputCol='Country_Num_Vec').fit(df)
    df = country_encoder.transform(df)
    # print(df.show(3))

    df_assembler = VectorAssembler(
        inputCols=['Platform_Num_Vec', 'Country_Num_Vec', 'Age', 'Repeat_Visitor', 'Web_pages_viewed'],
        outputCol='features'
    )
    df = df_assembler.transform(df)
    model_df = df.select(['features', 'Status'])
    return model_df


if __name__ == "__main__":
    # 1. 加载数据
    spark = SparkSession.builder.appName('log_reg').getOrCreate()
    df = spark.read.csv('./data/Log_Reg_dataset.csv', inferSchema=True, header=True)
    # print('样本数:{}, 特征数:{}'.format(df.count(), len(df.columns)))  # 样本数:20000, 特征数:6

    # 2. 数据分析
    # analyse_data(df)

    # 3. 特征工程
    model_df = feature_process(df)
    # print(model_df.show(3))
    # 切分数据集
    training_df, test_df = model_df.randomSplit([0.75, 0.25])
    print('训练集的个数:', training_df.count())
    print('测试集的个数:', test_df.count())

    print('训练集的正负样本比例:')
    print(training_df.groupBy('Status').count().show())

    print('测试集的正负样本比例:')
    print(test_df.groupBy('Status').count().show())

    # 4. 训练模型
    log_reg = LogisticRegression(labelCol='Status').fit(training_df)

    # 5. 测试模型
    train_results = log_reg.evaluate(training_df).predictions
    correct_preds = train_results.filter(train_results['Status'] == 1).filter(train_results['prediction'] == 1).count()
    print('训练集的正确率:', float(correct_preds)/(training_df.filter(training_df['Status'] == 1).count()))

    # 在测试集上的表现
    results = log_reg.evaluate(test_df).predictions
    # 计算混淆矩阵
    true_postives = results[(results.Status == 1) & (results.prediction == 1)].count()
    true_negatives = results[(results.Status == 0) & (results.prediction == 0)].count()
    false_positives = results[(results.Status == 0) & (results.prediction == 1)].count()
    false_negatives = results[(results.Status == 1) & (results.prediction == 0)].count()
    recall = float(true_postives)/(true_postives + false_negatives)
    print('召回率:', recall)

    precision = float(true_postives) / (true_postives + false_positives)
    print('精确率:', precision)

    accuracy = float((true_postives+true_negatives) /(results.count()))
    print('准确率:', accuracy)






















