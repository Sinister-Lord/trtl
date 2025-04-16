import turtle

# Function to draw an equilateral triangle
def draw_triangle():
    turtle.penup()
    turtle.goto(-200, 100)  # Move to starting position for the triangle
    turtle.pendown()
    turtle.fillcolor("red")  # Set fill color
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(150)  # Length of each side of the triangle
        turtle.left(120)  # Angle for equilateral triangle
    turtle.end_fill()

# Function to draw a rectangle
def draw_rectangle():
    turtle.penup()
    turtle.goto(50, 100)  # Move to starting position for the rectangle
    turtle.pendown()
    turtle.fillcolor("blue")  # Set fill color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)  # Length of longer side
        turtle.left(90)
        turtle.forward(100)  # Length of shorter side
        turtle.left(90)
    turtle.end_fill()

# Function to draw a hexagon
def draw_hexagon():
    turtle.penup()
    turtle.goto(250, 100)  # Move to starting position for the hexagon
    turtle.pendown()
    turtle.fillcolor("green")  # Set fill color
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(100)  # Length of each side of the hexagon
        turtle.left(60)  # Angle for hexagon
    turtle.end_fill()

# Main function to set up the screen and draw the shapes
def main():
    # Set up the screen
    turtle.bgcolor("lightyellow")  # Set background color of the screen
    turtle.speed(3)  # Set turtle speed (1 is slow, 10 is fast)
    
    # Set pen color
    turtle.pencolor("black")
    
    # Draw shapes
    draw_triangle()
    draw_rectangle()
    draw_hexagon()

    # Hide the turtle after drawing
    turtle.hideturtle()
    
    # Finish the drawing and hold the window open
    turtle.done()

if __name__ == "__main__":
    main()
