import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)
        t.right(120)
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)

screen = turtle.Screen()
screen.setup(800, 400)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300, 0)
t.pendown()

koch_curve(t, 3, 1)

turtle.done()
