from turtle import *
from random import *

speed(0)
colors=['pink','red','green','yellow','purple']
for i in range(200,0,-1):
    shuffle(colors)
    pencolor(colors[i%5])
    forward(i)
    left(90)
    up()
    right(45)
    down()
