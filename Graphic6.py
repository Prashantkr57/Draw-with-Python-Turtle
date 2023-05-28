import turtle

# Create a turtle object
t = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set the speed of the turtle
t.speed(10)

# Set the initial color
colors = ["red", "blue", "green", "orange", "purple"]

# Draw the spiral shape
for i in range(360):
    # Set the color based on the current angle
    t.pencolor(colors[i % len(colors)])

    # Move the turtle forward and turn it right
    t.forward(i)
    t.right(59)

# Hide the turtle
t.hideturtle()

# Exit the turtle graphics window when clicked
turtle.exitonclick()
