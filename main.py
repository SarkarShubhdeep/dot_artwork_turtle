import random
import turtle
from turtle import Turtle, Screen
import colorgram


foli = Turtle()
turtle.colormode(255)
foli.speed('fastest')
foli.pu()


def set_initial_position():
    foli.color((255, 255, 255))
    foli.left(180)
    for _ in range(5):
        foli.forward(40)
        foli.dot(20)
    foli.left(90)
    for _ in range(4):
        foli.forward(40)
        foli.dot(20)
    foli.left(90)
    foli.color((0, 0, 0))


def get_image_colors(image):
    ls = []
    colors_from_picture = colorgram.extract(image, 25)
    for colors in colors_from_picture:
        clr = tuple([colors.rgb.r, colors.rgb.g, colors.rgb.b])
        ls.append(clr)
    return ls


color_list = get_image_colors('green.jpg')



def make_dot_line_right():
    for _ in range(10):
        foli.color(random.choice(color_list))
        foli.dot(20)
        foli.forward(40)
    foli.left(90)
    foli.forward(40)
    foli.left(90)
    foli.forward(60)

def make_dot_line_left():
    for _ in range(9):
        foli.color(random.choice(color_list))
        foli.dot(20)
        foli.forward(40)
    foli.right(90)
    foli.forward(40)
    foli.right(90)
    foli.forward(20)






set_initial_position()
for i in range(5):
    make_dot_line_right()
    make_dot_line_left()










screen = Screen()
screen.exitonclick()

