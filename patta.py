import turtle
import colorsys

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Colors
hue = 0

# Draw colorful spiral flower
for i in range(120):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(i * 3)

    # Change color
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(r, g, b)
    hue += 0.008

    # Draw petal
    for _ in range(4):
        t.forward(150)
        t.right(90)

    t.right(10)

turtle.done()
