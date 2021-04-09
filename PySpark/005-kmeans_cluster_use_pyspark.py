"""
@file   : 005-kmeans_cluster_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-08
"""
import findspark
findspark.init()
import pyspark
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import rand, randn
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import ClusteringEvaluator

def analyse_data(df):
    '''
    数据分析
    :param df:
    :return:
    '''
    print('总共的标签数:', df.select('species').distinct().count())

    # 每类数据集的样本数
    print(df.groupBy('species').count().orderBy('count', ascending=False).show())


def feature_process(df):
    '''
    特征工程
    :param df:
    :return:
    '''
    input_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    vec_assembler = VectorAssembler(inputCols = input_cols, outputCol='features')
    final_data = vec_assembler.transform(df)
    return final_data


if __name__ == '__main__':
    # 加载鸢尾花的数据
    spark = SparkSession.builder.appName('k_means').getOrCreate()
    df = spark.read.csv('./data/iris_dataset.csv',inferSchema=True,header=True)
    print((df.count(),len(df.columns)))

    analyse_data(df)

    final_data = feature_process(df)

    errors=[]

    for k in range(2, 10):
        kmeans = KMeans(featuresCol='features', k=k)
        model = kmeans.fit(final_data)

        # Make predictions
        predictions = model.transform(final_data)
        evaluator = ClusteringEvaluator()
        silhouette = evaluator.evaluate(predictions)   # 欧式距离

        # 打印聚类的中心
        centers = model.clusterCenters()
        print("Cluster Centers: ")
        for center in centers:
            print(center)




