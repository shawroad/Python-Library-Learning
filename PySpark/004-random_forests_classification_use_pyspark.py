"""
@file   : 004-random_forests_classification_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-08
"""
import findspark

findspark.init()

from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


def analyse_data(df):
    '''
    数据分析
    :param df:
    :return:
    '''
    print(df.show(5))

    # 看看每个特征的统计信息 如均值方差等
    print(df.describe().select('summary', 'rate_marriage', 'age', 'yrs_married', 'children', 'religious').show())

    # 人们对婚姻打分比例
    print(df.groupBy('rate_marriage').count().show())

    # 以孩子和事务为键  然后聚合。 可以发现数据集中 没孩子 没事务的人最多
    print(df.groupBy('children', 'affairs').count().orderBy('children', 'affairs', 'count', ascending=True).show())


def feature_process(df):
    '''
    特征工程
    :param df:
    :return:
    '''
    df_assembler = VectorAssembler(inputCols=['rate_marriage', 'age', 'yrs_married', 'children', 'religious'],
                                   outputCol="features")
    df = df_assembler.transform(df)
    model_df = df.select(['features', 'affairs'])
    return model_df


if __name__ == '__main__':
    # 1. 加载数据集
    spark = SparkSession.builder.appName('random_forest').getOrCreate()
    df = spark.read.csv('./data/affairs.csv', inferSchema=True, header=True)
    print((df.count(), len(df.columns)))

    # 2. 数据分析
    analyse_data(df)

    # 3. 特征工程
    model_df = feature_process(df)
    # 切分数据集
    train_df, test_df = model_df.randomSplit([0.75, 0.25])
    print('训练集条数:', train_df.count())
    print('训练集标签的统计:')
    print(train_df.groupBy('affairs').count().show())

    print('测试集条数:', test_df.count())
    print('测试集标签的统计:')
    print(test_df.groupBy('affairs').count().show())

    # 4. 训练模型
    rf_classifier = RandomForestClassifier(labelCol='affairs', numTrees=50).fit(train_df)

    # 5. 模型评估
    rf_predictions = rf_classifier.transform(test_df)

    rf_accuracy = MulticlassClassificationEvaluator(labelCol='affairs', metricName='accuracy').evaluate(rf_predictions)
    print('测试集的准确率:', rf_accuracy)

    rf_precision = MulticlassClassificationEvaluator(labelCol='affairs', metricName='weightedPrecision').evaluate(
        rf_predictions)
    print('测试集的精确率:', rf_precision)

    rf_auc = BinaryClassificationEvaluator(labelCol='affairs').evaluate(rf_predictions)
    print('测试集的AUC值:', rf_auc)

    # 看一下在分类中  每个特征所起的重要性
    print(rf_classifier.featureImportances)

    # 保存模型
    rf_classifier.save("./RF_model")

    # 下次使用， 则按照下面的方式加载
    rf = RandomForestClassificationModel.load("./RF_model")
    model_preditions = rf.transform(test_df)
    model_preditions.show()

