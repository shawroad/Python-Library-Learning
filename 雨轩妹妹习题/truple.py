# 使用turtle绘制催眠图
import turtle as t   #引入turtle库并且起一个名称t
t.pensize(2)
t.color('black')
for i in range(0,40):   #循环范围
    t.fd(i*10)          
    t.left(90)
t.done() #停留