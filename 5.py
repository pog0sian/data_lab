import turtle
import random

def tree(branchLen, t):
    if branchLen > 5:
        # Толщина ветви зависит от длины
        t.width(max(1, int(branchLen / 10)))
        # Цвет ветви: если короткая — зелёная (листья), иначе коричневая
        if branchLen < 20:
            t.color("green")
        else:
            t.color("saddlebrown")
        t.forward(branchLen)
        # Случайный угол
        angle = random.randint(15, 45)
        t.right(angle)
        # Случайное уменьшение длины
        reduction = random.randint(10, 20)
        tree(branchLen - reduction, t)
        t.left(angle * 2)
        reduction = random.randint(10, 20)
        tree(branchLen - reduction, t)
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("saddlebrown")
    tree(100, t)
    myWin.exitonclick()

main()
