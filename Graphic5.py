import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set turtle properties
my_turtle.speed(10)
my_turtle.color("red")

# Draw a spiral
for i in range(100):
    my_turtle.forward(i * 5)
    my_turtle.right(144)

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.done()
