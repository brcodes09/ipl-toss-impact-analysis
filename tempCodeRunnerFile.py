import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightgray")

t = turtle.Turtle()
t.speed(0)

# Function to draw a filled rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Function to draw a filled circle
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a filled triangle
def draw_triangle(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Create background design with geometric shapes
# Draw rectangles
draw_rectangle(-400, 300, 200, 150, "cyan")
draw_rectangle(100, 250, 250, 120, "yellow")
draw_rectangle(-150, -100, 180, 200, "lightgreen")

# Draw circles
draw_circle(-300, -200, 80, "salmon")
draw_circle(200, 100, 60, "plum")
draw_circle(0, 200, 100, "skyblue")
draw_circle(-100, 0, 50, "orange")

# Draw triangles
draw_triangle(300, 200, 100, "gold")
draw_triangle(-350, 100, 80, "pink")
draw_triangle(150, -250, 90, "lime")

# Draw more decorative circles
draw_circle(350, -150, 40, "violet")
draw_circle(-200, 250, 50, "khaki")

t.hideturtle()
turtle.done()