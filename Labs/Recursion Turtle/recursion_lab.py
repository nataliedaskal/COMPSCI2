'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)


2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

# 1)
import turtle
my_hfractal = turtle.Turtle()
my_screen = turtle.Screen()
my_hfractal.goto(0, 0)
my_hfractal.setheading(180)
my_hfractal.shape("turtle")
my_screen.bgcolor('white')
my_hfractal.up()
my_hfractal.down()
my_hfractal.speed(0)

def draw_hfractal(length, depth):
    if depth > 0:
        my_hfractal.forward(length / 2)
        my_hfractal.right(90)
        my_hfractal.forward(length / 2)
        my_hfractal.left(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.left(90)
        my_hfractal.forward(length)
        my_hfractal.right(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.right(90)
        my_hfractal.forward(length / 2)
        my_hfractal.right(90)
        my_hfractal.forward(length)
        my_hfractal.left(90)
        my_hfractal.forward(length / 2)
        my_hfractal.left(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.left(90)
        my_hfractal.forward(length)
        my_hfractal.right(90)
        draw_hfractal(length / 2, depth - 1)
        my_hfractal.right(90)
        my_hfractal.forward(length / 2)
        my_hfractal.left(90)
        my_hfractal.forward(length / 2)
draw_hfractal(300, 4)
my_screen.clear()

# 2)
import turtle
def draw_triangle(vertices, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0], vertices[1][1])
    my_turtle.goto(vertices[2][0], vertices[2][1])
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.end_fill()

def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

def draw_fractal(vertices, level, my_turtle):
    colors = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]
    draw_triangle(vertices, colors[level], my_turtle)
    if level > 0:
        draw_fractal([vertices[0],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                     level - 1, my_turtle)
        draw_fractal([vertices[1],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[1], vertices[2])],
                     level - 1, my_turtle)
        draw_fractal([vertices[2],
                      midpoint(vertices[2], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                     level - 1, my_turtle)

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255)
vertices = [[-200, -100], [0, 200], [200, -100]]
level = 4
draw_fractal(vertices, level, my_turtle)
my_screen.clear()

# 3)
from turtle import *
def snowflake(lengths, levels):
    if levels == 0:
        forward(lengths)
        return
    lengths /= 3.0
    snowflake(lengths, levels - 1)
    left(60)
    snowflake(lengths, levels - 1)
    right(120)
    snowflake(lengths, levels - 1)
    left(60)
    snowflake(lengths, levels - 1)

if __name__ == "__main__":
    speed(0)
    length = 300
    up()
    backward(length / 2)
    down()
    for i in range(3):
        snowflake(length, 4)
        right(120)
    mainloop()

my_screen.exitonclick()