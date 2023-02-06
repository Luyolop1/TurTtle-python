import turtle
from turtle import *
import turtle as r
import colorsys

speed(10)
bgcolor("white")
pencolor("red")
penup()
goto(-150, -100)
right(45)
pensize(3)
pendown()


forward(150)
left(135)
forward(150)

right(45)
forward(150)
left(135)
forward(160)
right(50)
forward(140)
left(150)
forward(150)
right(50)
forward(160)
left(134)
forward(125)
hideturtle()

bgcolor("black")
pensize(10)
pencolor("green")


penup()
goto(-80, 200)
right(140)
pendown()
forward(350)
right(200)
forward(450)
right(170)
forward(500)
right(200)
forward(500)
left(200)
forward(200)

penup()

goto(200, -30)
showturtle()
pendown()
right(100)
forward(200)

pensize(1)
t = turtle.Turtle()
s = turtle.Screen()


t.pencolor("white")
t.speed(0)
c = 0
while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(5)
    c +=1
    if c>= 360/5:
        break

t.hideturtle()


r.speed(0)
r.bgcolor('black')
r.pencolor('violet')
for a in range(155):
    r.rt(a)
    r.circle(125,a)
    r.fd(a)
    r.rt(90)
r.done()


t.tracer(78)
t.pensize(3)
h = 0
n = 489
for i in range(668):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    t.color(c)
    t.up()
    t.goto(-8, 145)
    t.down()
    t.bk(i)
    t.fillcolor(c)
    t.begin_fill
    t.circle(90, 100)
    t.end_fill()
    t.It(189)
t.done
exitonclick()
