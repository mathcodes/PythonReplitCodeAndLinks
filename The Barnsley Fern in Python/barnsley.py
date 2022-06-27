import turtle
import random
import time

turtle.bgcolor("#222")
turtle.colormode(255)
pen = turtle.Turtle()
pen.speed(200)
time.sleep(7)


pen.penup()

x = 0
y = 5
for n in range(11000):
    r = 0
    g = 255
    b = 0
    rgb = (r,g,b)
    pen.color(rgb)
    pen.goto(65 * x, 37 * y - 252)  # scale the fern to fit nicely inside the window
    pen.pendown()
    pen.dot(random.randint(3,4))
    pen.penup()
    # pen.penup()
    r = random.random()
    if r < 0.01:
        x, y =  0.00 * x + 0.00 * y,  0.00 * x + 0.16 * y + 0.00
    elif r < 0.86:
        x, y =  0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
    elif r < 0.93:
        x, y =  0.20 * x - 0.26 * y,  0.23 * x + 0.22 * y + 1.60
    else:
        x, y = -0.15 * x + 0.28 * y,  0.26 * x + 0.24 * y + 0.44