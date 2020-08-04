# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 15:04
# @Author  : xiaolu
# @FileName: 001-创建库并插入数据.py
# @Software: PyCharm
from elasticsearch import Elasticsearch


es = Elasticsearch()

# result = es.indices.delete(index='point_type', ignore=[400, 404])  # 删除索引(库)
# exit()


mapping = {
    "settings": {
        "analysis": {
            "filter": {
                "jieba_stop": {
                    "type": "stop",
                    "stopwords_path": "stopwords/stopwords.txt"
                    },
                "jieba_synonym": {
                    "type": "synonym",
                    "synonyms_path": "synonyms/synonyms.txt"
                },
                "my_shingle_filter": {
                    "type": "shingle",
                    "min_shingle_size": 2,
                    "max_shingle_size": 2,
                    "output_unigrams": False
                }
            },
            "analyzer": {
                "word_ans": {
                    "tokenizer": "jieba_search",   # 采用结巴分词
                    "filter": "jieba_stop"      # 采用结巴停用词过滤
                },
                "char_ana": {
                    "tokenizer": "standard",   # 对于字符 采用标准的分词方式  就是按字分割
                    "filter": "jieba_stop"    # 也采用jieba停用词过滤
                },
                "char_bigram_ana": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": [
                        "jieba_stop",
                        "my_shingle_filter"
                    ]
                },
                "word_bigram_ana": {
                    "type": "custom",
                    "tokenizer": "jieba_search",
                    "filter": [
                        "jieba_stop",
                        "my_shingle_filter"
                    ]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "keyword"
            },
            "author": {
                "type": "keyword"
            },
            "dynasty": {
                "type": "keyword"
            },
            "words": {
                "type": "integer"
            },
            "content": {
                "analyzer": "word_ana",
                "search_analyzer": "word_ana",
                "type": "text"
            }
        }
    }
}
# 相当于将content入库时，会进行分词，然后采用jieba的停用词过滤方式。  当通过内容去查找时，也是先将问题分词，然后停用词过滤，在进行匹配。

# es.indices.create(index='point_type', body=mapping)

# 然后插入数据
data = [
    {
        "title": "静夜思",
        "author": "李白",
        "dynasty": "唐",
        "words": "20",
        "content": "床前明月光，疑是地上霜。举头望明月，低头思故乡。"
    },

    {
        "title": "观沧海",
        "author": "曹操",
        "dynasty": "东汉末年",
        "words": "56",
        "content": "东临碣石，以观沧海。水何澹澹，山岛竦峙。树木丛生，百草丰茂。秋风萧瑟，洪波涌起。日月之行，若出其中。星汉灿烂，若出其里。幸甚至哉，歌以咏志。"
    },

    {
        "title": "咏鹅",
        "author": "骆宾王",
        "dynasty": "唐",
        "words": "18",
        "content": "鹅鹅鹅，曲项向天歌。白毛浮绿水，红掌拨清波。"
    },

    {
        "title": "将进酒",
        "author": "陈陶",
        "dynasty": "唐",
        "words": "14",
        "content": "银鸭金鹅言待谁，隋家岳渎皇家有"
    },

    {
        "title": "春雪",
        "author": "白居易",
        "dynasty": "唐",
        "words": "10",
        "content": "大似落鹅毛，密如飘玉屑"
    }
]
for d in data:
    es.index(index='point_type', body=d)
