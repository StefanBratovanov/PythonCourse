import turtle

side = 20
for k in range(8):
    for i in range(8):
        if i % 2 == 0:
            turtle.begin_fill()
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    turtle.penup()
    turtle.goto(0, - side * 2)
    turtle.pendown()

turtle.exitonclick()
