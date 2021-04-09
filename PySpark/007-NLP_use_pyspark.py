"""
@file   : 007-NLP_use_pyspark.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-04-09
"""
import findspark

findspark.init()

from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import HashingTF, IDF
from pyspark.sql.functions import length
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator


def basic_op():
    '''
    基本的操作
    :return:
    '''
    spark = SparkSession.builder.appName('nlp').getOrCreate()
    df = spark.createDataFrame([(1, 'I really liked this movie'),
                                (2, 'I would recommend this movie to my friends'),
                                (3, 'movie was alright but acting was horrible'),
                                (4, 'I am never watching that movie ever again')],
                               ['user_id', 'review'])
    # print(df.show())

    # 1. 将文本进行分词 做成新一个特征
    tokenization = Tokenizer(inputCol='review', outputCol='tokens')
    tokenized_df = tokenization.transform(df)
    # print(tokenized_df.show())

    # 2. 去除停用词
    stopword_removal = StopWordsRemover(inputCol='tokens', outputCol='refined_tokens')
    refined_df = stopword_removal.transform(tokenized_df)
    print(refined_df.select(['user_id', 'tokens', 'refined_tokens']).show(10))

    # 3. 统计向量  使用one-hot
    count_vec = CountVectorizer(inputCol='refined_tokens', outputCol='features')
    cv_df = count_vec.fit(refined_df).transform(refined_df)
    print(cv_df.select(['user_id', 'refined_tokens', 'features']).show(4))
    print('词表(注:去停用词之后的):', count_vec.fit(refined_df).vocabulary)

    # 4. 计算tf-idf
    hashing_vec = HashingTF(inputCol='refined_tokens', outputCol='tf_features')
    hashing_df = hashing_vec.transform(refined_df)  # 先进行一个hash计算
    print(hashing_df.select(['user_id', 'refined_tokens', 'tf_features']).show())

    tf_idf_vec = IDF(inputCol='tf_features', outputCol='tf_idf_features')
    tf_idf_df = tf_idf_vec.fit(hashing_df).transform(hashing_df)
    print(tf_idf_df.select(['user_id', 'tf_idf_features']).show(4))


def data_process(text_df):
    text_df = text_df.filter(((text_df.Sentiment == '1') | (text_df.Sentiment == '0')))
    print('清洗后的数据量:', text_df.count())

    print('正负样本的分布')
    print(text_df.groupBy('Sentiment').count().show())

    # 加入长度特征
    text_df = text_df.withColumn("Label", text_df.Sentiment.cast('float')).drop('Sentiment')

    # 分词
    text_df = text_df.withColumn('length', length(text_df['Review']))
    tokenization = Tokenizer(inputCol='Review', outputCol='tokens')
    tokenized_df = tokenization.transform(text_df)

    # 去停用词
    stopword_removal = StopWordsRemover(inputCol='tokens', outputCol='refined_tokens')
    refined_text_df = stopword_removal.transform(tokenized_df)

    len_udf = udf(lambda s: len(s), IntegerType())
    refined_text_df = refined_text_df.withColumn("token_count", len_udf(col('refined_tokens')))

    count_vec = CountVectorizer(inputCol='refined_tokens', outputCol='features')
    cv_text_df = count_vec.fit(refined_text_df).transform(refined_text_df)

    model_text_df = cv_text_df.select(['features', 'token_count', 'Label'])
    return model_text_df


if __name__ == '__main__':
    # basic_op()

    # 下面做一个简单的文本分类
    spark = SparkSession.builder.appName('text_classification').getOrCreate()
    text_df = spark.read.csv('./data/Movie_reviews.csv', inferSchema=True, header=True, sep=',')
    print('数据量:', text_df.count())  # 数据量: 7087

    model_text_df = data_process(text_df)
    df_assembler = VectorAssembler(inputCols=['features', 'token_count'], outputCol='features_vec')
    model_text_df = df_assembler.transform(model_text_df)

    # 切分数据集
    training_df, test_df = model_text_df.randomSplit([0.75, 0.25])

    # 模型训练
    log_reg = LogisticRegression(featuresCol='features_vec', labelCol='Label').fit(training_df)

    # 模型评估
    results = log_reg.evaluate(test_df).predictions

    # confusion matrix
    true_postives = results[(results.Label == 1) & (results.prediction == 1)].count()
    true_negatives = results[(results.Label == 0) & (results.prediction == 0)].count()
    false_positives = results[(results.Label == 0) & (results.prediction == 1)].count()
    false_negatives = results[(results.Label == 1) & (results.prediction == 0)].count()

    recall = float(true_postives) / (true_postives + false_negatives)
    print(recall)

    precision = float(true_postives) / (true_postives + false_positives)
    print(precision)

    accuracy = float((true_postives + true_negatives) / (results.count()))
    print(accuracy)
