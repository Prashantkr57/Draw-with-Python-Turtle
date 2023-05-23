import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the speed of the turtle (optional)
pen.speed(0)

# Set the background color
turtle.bgcolor("black")

# Set the initial position of the turtle
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Set the colors for the graphic
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Draw the cool graphic
for x in range(360):
    pen.pencolor(colors[x % 6])
    pen.width(x / 100 + 1)
    pen.forward(x)
    pen.left(59)

# Hide the turtle
pen.hideturtle()

# Exit on click (optional)
turtle.exitonclick()
