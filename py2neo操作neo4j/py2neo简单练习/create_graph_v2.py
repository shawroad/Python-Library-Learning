"""
# -*- coding: utf-8 -*-
# @File    : create_graph_v2.py
# @Time    : 2020/11/23 9:54 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
"""
# -*- coding: utf-8 -*-
# @File    : create_graph_v1.py
# @Time    : 2020/11/23 6:52 下午
# @Author  : xiaolu
# @Email   : luxiaonlp@163.com
# @Software: PyCharm
"""
from py2neo import Graph, Node, Relationship, NodeMatcher
import pandas as pd
from pdb import set_trace


def load_data():
    # 加载数据
    data = pd.read_excel('./santi.xlsx')
    # data = pd.read_excel('./mingchaonaxieshier.xlsx')
    # data = pd.read_excel('./test.xlsx')
    start = data['S'].tolist()
    relation = data['P'].tolist()
    end = data['O'].tolist()
    start_list = [str(i) for i in start]
    relation_list = [str(i) for i in relation]
    end_list = [str(i) for i in end]
    link_dict = dict()
    link_dict['start'] = start_list
    link_dict['relation'] = relation_list
    link_dict['end'] = end_list
    df_data = pd.DataFrame(link_dict)
    return df_data


class DataToNeo4j:
    def __init__(self):
        link = Graph()
        self.graph = link

        self.start = 'start'
        self.end = 'end'

        self.graph.delete_all()   # 将之前的图  全部删除
        self.matcher = NodeMatcher(link)   # 为了查找

    def create_node(self, start, end):
        # 创建节点
        temp = []
        temp.extend(start)
        temp.extend(end)
        temp = list(set(temp))
        for t in temp:
            node = Node(self.start, name=t)
            self.graph.create(node)


        # for name in start:
        #     node = Node(self.start, name=name)
        #     self.graph.create(node)
        #
        # for name in end:
        #     node = Node(self.end, name=name)
        #     self.graph.create(node)

    def create_relation(self, df_data):
        m = 0
        for m in range(0, len(df_data)):
            # print(list(self.matcher.match(self.start).where('_.name=' + "'" + df_data['start'][m] + "'")))
            # 相当于在'start'标签下找   name=某个名字的节点
            # print(list(self.matcher.match(self.end).where('_.name=' + "'" + df_data['end'][m] + "'")))
            # 相当于在'end'标签下找   name=某个名字的节点'
            # 然后为这两个节点创建关系
            try:
                rel = Relationship(
                    self.matcher.match(self.start).where('_.name=' + "'" + df_data['start'][m] + "'").first(),
                    df_data['relation'][m],
                    self.matcher.match(self.start).where('_.name=' + "'" + df_data['end'][m] + "'").first()
                )
                self.graph.create(rel)
            except AttributeError as e:
                print(e, m)


def data_extraction(df_data):
    node_start = []
    for i in df_data['start'].tolist():
        node_start.append(i)

    node_end = []
    for i in df_data['end'].tolist():
        node_end.append(i)

    # 去重
    node_start = list(set(node_start))
    node_end = list(set(node_end))
    return node_start, node_end


if __name__ == '__main__':
    df_data = load_data()
    # print(df_data.head())
    node_start, node_end = data_extraction(df_data)
    # 创建图
    create_data = DataToNeo4j()
    # 节点
    create_data.create_node(node_start, node_end)
    # 关系
    create_data.create_relation(df_data)












