import turtle

i = 10
turtle.color('green')
while True:
    if i % 2 == 0:
        turtle.forward(10)
        turtle.right(i % 24)
        turtle.forward(20)

        i += 1
    else:
        i += 1
