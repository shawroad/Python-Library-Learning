# 使用turtle画出一个奥运五环图
import turtle as t #引入turtle库并且起一个名称t
t.pensize(15)  #设置划线宽度，定段粗

t.penup()
t.goto(-150,0)
t.color('blue')
t.pendown()
t.circle(100)

t.penup()
t.goto(0,0)
t.color('black')
t.pendown()
t.circle(100)

t.penup()
t.goto(150,0)
t.color('red')
t.pendown()
t.circle(100)

t.penup()
t.goto(-120,-130)
t.color('yellow')
t.pendown()
t.circle(100)

t.penup()
t.goto(120,-130)
t.color('green')
t.pendown()
t.circle(100)

t.done() #停留

import turtle as t #引入turtle库并且起一个名称t
def drawCircle(x,y,c='red'):
    t.pu()# 抬起画笔
    t.goto(x,y) # 绘制圆的起始位置
    t.pd()# 放下画笔
    t.color(c)# 绘制c色圆环
    t.circle(100,360) #绘制圆：半径，角度

t.pensize(3) # 画笔尺寸设置3

drawCircle(0,0,'blue')
drawCircle(120,0,'black')
drawCircle(220,0,'red')
drawCircle(120,-30,'green')
drawCircle(30,-30,'yellow')

t.done()