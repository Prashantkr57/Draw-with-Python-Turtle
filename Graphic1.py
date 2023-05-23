import turtle

# Create a turtle instance
t = turtle.Turtle()

# Set the speed of the turtle (1 is the slowest, 10 is the fastest)
t.speed(3)

# Set the background color
turtle.bgcolor("black")

# Set the pen color and fill color
t.pencolor("white")
t.fillcolor("orange")

# Begin filling the shape
t.begin_fill()

# Draw a shape using turtle commands
for x in range(36):
    t.forward(200)
    t.left(170)

# End filling the shape
t.end_fill()

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()
