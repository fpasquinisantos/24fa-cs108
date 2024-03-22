"""
Put here your custom function to draw something.
The figure shouldn't surpass a square of 200x200 points.
The turtle passed should be start AND END pointing left at the right-left corner of the figure.
"""
import turtle


def bluepolygon_sofie(turtle):
    """
    Author: Sofie Schumerth
    Draws a blue polygon similar to a spirograph
    """
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(12):
        turtle.forward(108)
        turtle.right(150)
    turtle.end_fill()
    
def bluesquare_fernando(turtle):
    """
    Author: Fernando Santos
    Draws a simple 100x100 square
    """
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.end_fill()

def square_fernando(turtle):
    """
    Author: Levi Suter
    Draws a simple 100x100 square
    """
    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.end_fill()
def greenoctogan_ryan(turtle):
    """
    Author: Ryan Halberg
    Draws a Green Octogan
    """
    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(100)
        turtle.right(360/8)
    turtle.end_fill()
    
def pinksqure_anneka(turtle):
    '''
    Author: Anneka Bos
    Draws a pink circle
    '''
    turtle.fillcolor('pink')
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    
def pinksqure_anneka(turtle):
    '''
    Author: Anneka Bos
    Draws a pink circle
    '''
    turtle.fillcolor('pink')
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def yellowtriange_emma(t):
    """
    Author: Emma Staub
    Draws a yellow triange
    """
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(3):
        t.forward(75)
        t.right(120)
    t.end_fill()
    
def fractal_fernando(t):
    """
    Author: Levi Suter
    Draws a Koch line fractal
    """
    def koch_line(l):
        if l > unit:
            koch_line(l/3)
            t.left(60)
            koch_line(l/3)
            t.right(120)
            koch_line(l/3)
            t.left(60)
            koch_line(l/3)
        else:
            t.forward(unit)
    
    t.fillcolor('blue')
    t.begin_fill()
    unit, depth, poly_sides = 4, 3, 3
    length = (3**depth)*unit   # number is #segments
    for i in range(poly_sides):
        koch_line(length)
        t.right(360/poly_sides)
    t.end_fill()

def draw_something():
    screen = turtle.Screen()
    screen.setup(200, 200)
    screen.tracer(0)
    
    t = turtle.Turtle()
    t.penup()
    t.goto(-100, 100)  # Starting position
    t.pendown()
    t.left(180)  # Start and end pointing left
    
    square_fernando(t)
    fractal_fernando(t)

    screen.update()
    screen.mainloop()

draw_something()