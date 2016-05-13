import turtle
side=40
for i in range(8):
    if i % 2==0:
        turtle.begin_fill()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.end_fill()
    turtle.forward(side)
turtle.exitonclick()

