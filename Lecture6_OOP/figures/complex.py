from .base import Figure


class Rectangle(Figure):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw(self, turtle):
        half_w = self.width / 2
        half_h = self.height / 2
        left = self.center_x - half_w
        top = self.center_y - half_h

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()

        turtle.color(self.color)

        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)


class RegularPolygon(Figure):
    def __init__(self, radius, number_of_sides, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.number_of_sides = number_of_sides

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)
        turtle.pendown()
        angle = 360 / self.number_of_sides
        for i in range(self.number_of_sides):
            turtle.left(90)
            turtle.forward(self.radius)
            turtle.left(90)
            turtle.forward(self.radius)
