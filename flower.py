import turtle
import colorsys

# Setup
screen = turtle.Screen()
screen.bgcolor("#ffcce6")  # soft pink background
screen.tracer(0)

t = turtle.Turtle()
t.width(2)
t.speed(0)
t.hideturtle()

hue = 0.0

# Blooming petals (increasing radius)
for size in range(10, 180, 2):
    t.clear()
    hue += 0.01
    color = colorsys.hsv_to_rgb(hue % 1, 1, 1)
    t.color(color)

    t.penup()
    t.goto(0, 0)
    t.pendown()

    # 🟣 Full flower — rotate petals around center
    for angle in range(0, 360, 45):  # 8 petals
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()

        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(120)

    screen.update()

# Keep the final frame
turtle.done()



