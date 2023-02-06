import turtle
import turtle as r
import colorsys


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
