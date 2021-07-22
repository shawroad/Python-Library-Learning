"""
@file   : pinyin_test.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2021-07-22
"""
from pypinyin import pinyin, lazy_pinyin, Style

if __name__ == '__main__':
    print(pinyin('新浪微博'))   # 输出: [['xīn'], ['làng'], ['wēi'], ['bó']]

    print(lazy_pinyin('新浪微博'))   # 输出: ['xin', 'lang', 'wei', 'bo']

    # 将拼音用数字表示 然后跟在拼音的后面
    style = Style.TONE3    # 1代表一声、2代表二声、3代表三声、4代表四声
    print(lazy_pinyin('新浪微博', style=style))

