import turtle

def draw_spiral():
    turtle.speed(0)
    turtle.bgcolor("black")
    colors = ["red", "yellow", "blue", "green"]

    for x in range(400):
        turtle.pencolor(colors[x % 4])
        turtle.width(x / 100 + 1)
        turtle.forward(x)
        turtle.left(91)

    turtle.exitonclick()

draw_spiral()
