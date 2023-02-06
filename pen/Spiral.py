import turtle
turtle.setup(width=600, height=500)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor('black')

c = 0
x = 0

colors = {
    #reddish colors
    (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.07, 0.00), (1.00, 0.10, 0.00), (1.00, 0.12,),
    #orangey colors
    (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00),(1.00, 0.62,),
    #yellowy colors
    (1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00), (0.80, 1.00, 0.00), (0.75, 1.00,),
 }

while x < 1000:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 1
    c = c + 0.1

turtle.exitonclick()