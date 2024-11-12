import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create the turtle for drawing the cake
cake_turtle = turtle.Turtle()
cake_turtle.speed(10)

# Function to draw a rectangle (for cake layers)
def draw_rectangle(t, width, height, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
    t.setheading(0)  # Reset direction

# Function to draw icing drips
def draw_icing_drips(t, width):
    t.color("white")
    t.penup()
    t.goto(-width // 2, 0)
    t.setheading(0)
    t.pendown()
    for _ in range(width // 40):
        t.circle(6, 180)
        t.forward(10)
    t.penup()
    t.setheading(0)  # Reset direction after drawing

# Function to draw a candle
def draw_candle(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.end_fill()
    
    # Draw the flame
    t.penup()
    t.goto(x + 5, y + 40)
    t.color("orange")
    t.shape("circle")
    t.stamp()
    t.goto(x + 5, y + 50)
    t.color("yellow")
    t.stamp()
    t.penup()
    t.setheading(0)

# Function to draw sprinkles
def draw_sprinkle(t, x, y, color):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.dot(5)

# Draw cake layers
cake_turtle.penup()
cake_turtle.goto(-140, -150)

# Bottom layer
cake_turtle.pendown()
draw_rectangle(cake_turtle, 280, 70, "saddlebrown")
cake_turtle.goto(-130, -80)
cake_turtle.pendown()
draw_icing_drips(cake_turtle, 280)

# Middle layer
cake_turtle.goto(-130, -80)
cake_turtle.pendown()
draw_rectangle(cake_turtle, 260, 70, "hotpink")
cake_turtle.goto(-120, -10)
cake_turtle.pendown()
draw_icing_drips(cake_turtle, 260)

# Top layer
cake_turtle.goto(-120, -10)
cake_turtle.pendown()
draw_rectangle(cake_turtle, 240, 70, "lightyellow")
cake_turtle.goto(-110, 60)
cake_turtle.pendown()
draw_icing_drips(cake_turtle, 240)

# Draw candles on the top layer
candle_positions = [-60, -30, 0, 30, 60]
for pos in candle_positions:
    draw_candle(cake_turtle, pos, 60)

# Sprinkle colors
sprinkle_colors = ["blue", "red", "purple", "green", "orange", "white"]

# Add sprinkles to the bottom layer
for _ in range(15):
    x = random.randint(-140, 140)
    y = random.randint(-150, -80)
    draw_sprinkle(cake_turtle, x, y, random.choice(sprinkle_colors))

# Add sprinkles to the middle layer
for _ in range(12):
    x = random.randint(-130, 130)
    y = random.randint(-80, -10)
    draw_sprinkle(cake_turtle, x, y, random.choice(sprinkle_colors))

# Add sprinkles to the top layer
for _ in range(10):
    x = random.randint(-120, 120)
    y = random.randint(-10, 60)
    draw_sprinkle(cake_turtle, x, y, random.choice(sprinkle_colors))

# Add "Happy Birthday" text
cake_turtle.penup()
cake_turtle.goto(0, 120)
cake_turtle.color("purple")
cake_turtle.write("Happy Birthday!", align="center", font=("Arial", 24, "bold"))

# Hide the turtle and finish
cake_turtle.hideturtle()
turtle.done()
