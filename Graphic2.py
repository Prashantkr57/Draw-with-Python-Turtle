import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")


# Define a function to draw a square
def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)


# Define a function to draw a circle of squares
def draw_circle_of_squares():
    for _ in range(36):
        draw_square()
        pen.right(10)


# Draw the circle of squares
draw_circle_of_squares()

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
