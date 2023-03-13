# 使用turtle绘制一个黑白的火柴人
#引入turtle库并且起一个名称t
import turtle as t  
t.pensize(5)     
t.fd(500)

t.begin_fill()
t.penup()
t.goto(250,200)
t.color('black','black')
t.pendown()
t.circle(35)
t.end_fill()
t.right(90)
t.fd(20)

t.right(60)
t.fd(40)

t.left(40)
t.fd(30)

t.penup()
t.goto(250,180)
t.pendown()
t.left(20)
t.fd(70)

t.penup()
t.goto(250,180)
t.pendown()
t.left(60)
t.fd(40)

t.right(30)
t.fd(30)

t.penup()
t.goto(250,110)
t.pendown()
t.left(30)
t.fd(45)

t.right(50)
t.fd(45)

t.penup()
t.goto(250,110)
t.pendown()
t.right(50)
t.fd(30)

t.left(20)
t.fd(45)

t.penup()
t.goto(180,60)
t.pendown()
t.left(60)
t.fd(30)

t.penup()
t.goto(200,40)
t.pendown()
t.left(50)
t.fd(150)

t.penup()
t.goto(350,40)
t.pendown()
t.left(30)
t.fd(30)

t.penup()
t.goto(250,6)
t.pendown()
t.circle(18)

t.penup()
t.goto(320,6)
t.pendown()
t.circle(18)

t.done() #停留
