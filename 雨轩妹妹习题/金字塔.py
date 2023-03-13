from turtle import * 

for i in range(4):
    if(i<3):
        speed(1)
        h = i*120
        seth(h)
        forward(100)
    else:
        speed(1)
        h = i*120
        seth(h)
        forward(50)

for j in range(3):
    speed(1)
    k=60+j*120
    seth(k)
    forward(50)

from turtle import *
from math import *

def draw_triangle(t,a,k):
    t.color('orange')  
    t.penup()
    t.right(90)
    t.forward(a*sqrt(3)/2)  #向下走a倍根号3，然后再向左走a/2
    t.left(90)
    t.backward(a/2)
    for m in range(k):  #开始绘制每一行
        t.begin_fill()
        t.pendown()
        for i in range(3):
            t.forward(a)
            t.left(120)
        t.penup()
        t.end_fill()
        t.forward(a)
    t.backward(k*a)

t = getturtle()
for i in range(5):      #每次绘制一行，总共3行
    draw_triangle(t,30,i)

