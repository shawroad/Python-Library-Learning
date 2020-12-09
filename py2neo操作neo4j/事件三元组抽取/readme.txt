--------------2020-12-9 更新----------------------
这里不建议用ltp做三元组抽取，最近学习了一个深度学习模型进行三元组抽取  在我的另一个仓库

[链接](https://github.com/shawroad/NLP_pytorch_project/tree/master/relation_extraction/lstm_cnn_information_extract)


--------------2020-11-28 更新----------------------
迪哥使用的是pyltp。 这里我不推荐用pyltp，这个包目前已经不更新了。已经是老古董了。加载的模型估计也过时了。

这里我推荐使用ltp

安装: pip install ltp -i https://pypi.douban.com/simple/

测试安装成功与否: from ltp import LTP

安装成功后   下载模型 直接执行下面的代码  就可以下载了
from ltp import LTP
ltp = LTP()    # ltp = LTP(path = "base|small|tiny") 可以指定参数  默认下载的是small  180m左右


这些操作完成以后  建议先看看ltp的使用方法
可以看代码  ltp的使用.py  或者看官方文档:http://ltp.ai/docs/quickstart.html
然后在去看三元组的抽取
