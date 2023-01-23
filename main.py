import turtle
from random import choice
color_list = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147),
              (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37),
              (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221),
              (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39),
              (154, 208, 221), (115, 46, 43)]  # tuples with RGB values
timmy = turtle.Turtle()
timmy.speed("fastest")
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.goto(-300, -300)
for _ in range(5):
    for _ in range(10):
        timmy.forward(50)
        timmy.dot(20, choice(color_list))
    timmy.sety(timmy.ycor()+50)
    for _ in range(10):
        timmy.dot(20, choice(color_list))
        timmy.backward(50)
    timmy.sety(timmy.ycor()+50)
screen = turtle.Screen()
screen.exitonclick()

# ----------
# PRACTICE
# ----------
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return r, g, b


# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dotted line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Different shapes
# number_of_sides = 3
# timmy_colors = ["midnight blue", "orange", "sea green", "coral1", "blue", "magenta4", "red", "gold2", "aquamarine4",
#                 "gray7"]
# color_index = 0
# while number_of_sides < 11:
#     for _ in range(number_of_sides):
#         timmy.color(timmy_colors[color_index])
#         timmy.forward(100)
#         timmy.right(360 / number_of_sides)
#     number_of_sides += 1
#     color_index += 1

# Random walk
# direction = [0, 90, 180, 270]
# timmy.speed("fastest")
# timmy.pensize(15)
# for _ in range(100):
#     timmy.forward(30)
#     timmy.setheading(choice(direction))
#     timmy.color(random_color())


# Spirograph
# def draw_spiral(num):
#     tilt = 360 / num
#     for _ in range(num):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(tilt)
#         tilt += 360 / num
# #
# #
# draw_spiral(100)

# Colorgram
# Color scheme inspired by Damien Hirst's Spot Paintings
# import colorgram
# all_colors = colorgram.extract('image.jpg', 30)
# colors = []
# for color in all_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     final_color = (r, g, b)
#     colors.append(final_color)
