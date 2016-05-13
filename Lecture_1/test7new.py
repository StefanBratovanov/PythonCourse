import turtle

side = 20
for j in range(8):
    for i in range(8):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    turtle.penup()
    turtle.goto(0, - side * (j + 1))
    turtle.pendown()

turtle.exitonclick()
