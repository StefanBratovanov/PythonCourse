import sys
import json
import turtle
from typing import List, Dict
import os
from JSONLoader import JSONLoader

from figures.base import Figure
from figures.simple import Circle, Square
from figures.complex import Rectangle, RegularPolygon

FIGURE_TYPES = {
    "circle": Circle,
    "square": Square,
    "rectangle": Rectangle,
    "regular": RegularPolygon
}


def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2


def load_input_data(input_filename):
    # os.path.splitext връща tuple с 2 стойности - име и разширение на файла
    filename, extension = os.path.splitext(input_filename)
    loader = None
    if extension == '.json':
        loader = JSONLoader(input_filename)
    elif extension == '.yaml':
        # ... тук по същия начин ще се добави обработване на YAML файлове
        pass

    if loader is not None:
        return loader.load()
    else:
        raise ValueError("Unsupported file format: {}".format(extension))


def create_figures(input_data: dict) -> List[Figure]:
    result = []
    for f_info in input_data:
        figure_type = f_info['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**f_info))
        else:
            raise ValueError("Unsupported figure")
    return result


def draw_figures(figures: List[Figure]):
    for figure in figures:
        t = turtle.Turtle()
        t.speed('slow')
        figure.draw(t)
    turtle.exitonclick()


if __name__ == "__main__":
    sys.exit(main())