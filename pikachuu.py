import turtle

screen = turtle.Screen()
screen.bgcolor("white")
pikachu = turtle.Turtle()
pikachu.speed(0)

def draw_circle(color, radius, x, y):
    pikachu.penup()
    pikachu.goto(x, y)
    pikachu.pendown()
    pikachu.color(color)
    pikachu.begin_fill()
    pikachu.circle(radius)
    pikachu.end_fill()

def draw_pikachu():
    # Ears
    pikachu.penup()
    pikachu.goto(-20, 100)
    pikachu.color("black", "yellow")
    pikachu.begin_fill()
    pikachu.goto(-20, 100)
    pikachu.goto(-40, 170)
    pikachu.goto(-10, 160)
    pikachu.goto(-20, 100)
    pikachu.end_fill()

    pikachu.begin_fill()
    pikachu.goto(20, 100)
    pikachu.goto(40, 170)
    pikachu.goto(10, 160)
    pikachu.goto(20, 100)
    pikachu.end_fill()

    # Face
    draw_circle("yellow", 60, 0, 20)

    # Eyes
    draw_circle("white", 10, -20, 60)
    draw_circle("black", 5, -20, 65)
    draw_circle("white", 10, 20, 60)
    draw_circle("black", 5, 20, 65)

    # Cheeks
    draw_circle("red", 8, -35, 40)
    draw_circle("red", 8, 35, 40)

    # Nose
    draw_circle("black", 3, 0, 50)

    # Mouth
    pikachu.penup()
    pikachu.goto(-10, 35)
    pikachu.setheading(-60)
    pikachu.pendown()
    pikachu.circle(10, 120)

    # Body
    draw_circle("yellow", 50, 0, -50)

    # Arms
    draw_circle("yellow", 15, -40, -10)
    draw_circle("yellow", 15, 40, -10)

    # Legs
    draw_circle("yellow", 15, -25, -90)
    draw_circle("yellow", 15, 25, -90)

    # Tail (simple zigzag)
    pikachu.penup()
    pikachu.goto(50, -30)
    pikachu.color("gold")
    pikachu.pensize(10)
    pikachu.setheading(90)
    pikachu.pendown()
    pikachu.forward(40)
    pikachu.left(135)
    pikachu.forward(30)
    pikachu.right(135)
    pikachu.forward(40)

draw_pikachu()
pikachu.hideturtle()
turtle.done()
