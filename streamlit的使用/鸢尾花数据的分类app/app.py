"""
@file   : app.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-06-09
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def get_dataset(name):
    # 加载数据集
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X, y


def add_parameter_ui(clf_name):
    # 针对每个分类器 可以调节的超参数
    params = dict()
    if clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)    # 滑动条
        params['C'] = C
    elif clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)    # 滑动条
        params['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)     # 滑动条
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)    # 滑动条
        params['n_estimators'] = n_estimators
    return params


def get_classifier(clf_name, params):
    # 实例化分类器
    clf = None
    if clf_name == 'SVM':
        clf = SVC(C=params['C'])
    elif clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'],
                                     max_depth=params['max_depth'], random_state=1234)
    return clf


def plot_result():
    pca = PCA(2)
    X_projected = pca.fit_transform(X)
    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]
    fig = plt.figure()
    plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')

    plt.xlabel('feature_1')
    plt.ylabel('feature_2')
    plt.colorbar()
    st.pyplot(fig)


if __name__ == '__main__':
    # 启动该项目，命令行: streamlit run app.py
    st.title('鸢尾花数据集的分类')
    st.write('''
    # 支持选择不同的分类器(SVM/Random Forest/KNN)
    哪一个分类器更好呢？''')   # 支持markdown

    # 1. 可以选择不同的数据集  是一个下拉选择框
    dataset_name = st.sidebar.selectbox(
        '数据集的选择',
        ('Iris', 'Breast Cancer', 'Wine')
    )

    st.write('## {} 数据集'.format(dataset_name))   # 选择好数据集  这里显示

    # 2. 可以选择不同的分类器， 是一个下拉选择框
    classifier_name = st.sidebar.selectbox(
        '分类器的选择',
        ('KNN', 'SVM', 'Random Forest')
    )

    X, y = get_dataset(dataset_name)
    st.write('数据集的形状:', X.shape)
    st.write('数据集的类别数:', len(np.unique(y)))

    params = add_parameter_ui(classifier_name)

    clf = get_classifier(classifier_name, params)

    # 模型训练
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)   # 准确率

    st.write('选择的分类器为: ', classifier_name)
    st.write('准确率: ', acc)

    # 画图
    plot_result()
