import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the screen size
screen = turtle.Screen()
screen.setup(800, 600)

# Set the pen color and speed
pen.color("red")
pen.speed(5)

# Draw a cool graphics pattern
for _ in range(36):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(100)

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.exitonclick()
