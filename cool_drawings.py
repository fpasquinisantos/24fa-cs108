"""
Put here your custom function to draw something.
The figure shouldn't surpass a square of 200x200 points.
The turtle passed should be start AND END pointing left at the right-left corner of the figure.
"""

def orangesquare_Nation(turtle):
    """
    Author: Victoria Nation
    Draws simple 150x150 square
    """
    turtle.fillcolor('orange')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.end_fill()
    
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
    
def fractal_zuriel(t):
    """
    Author: Zuriel Olu-Silas
    Draws a pink Koch line fractal
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
    
    t.fillcolor('pink')
    t.begin_fill()
    unit, depth, poly_sides = 4, 3, 3
    length = (3**depth)*unit   # number is #segments
    for i in range(poly_sides):
        koch_line(length)
        t.right(360/poly_sides)
    t.end_fill()

def square_fernando(turtle):
    """
    Author: Fernando Santos
    Draws a simple 100x100 square
    """
    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
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
    
    
def redsqure_Rowan(turtle):
    '''
    Author: Rowan Jansen
    Draws a pink circle
    '''
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    
def yellosquare_jieun (turtle):
    """
    Author: Jieun Seo
    Draws a yellow square
    """
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()
    
def greentriangle_jake(turtle):
    """
    Author: Jake McClure
    Draws a green triangle
    """
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.penup()
    turtle.setposition(-100, -100)  # Start at bottom left corner
    turtle.pendown()
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()


def fractal_fernando(t):
    """
    Author: Fernando Santos
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
    
    
def purpletriangle_Abraham(turtle):
    """
    Author: Abraham Jeon
    A purple triangle
    """
    turtle.fillcolor('purple')
    turtle.begin_fill()
    turtle.penup()
    turtle.setposition(0, 0) #start at 0, 0
    turtle.pendown()
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()
    


def pizza_gustafson(turtle):

    """
    This draws a cheese pizza with 8 slices
    """
    turtle.shape('turtle')
    turtle.pensize(4)
    #possition turtle
    turtle.color('orange')
    turtle.right(45)
    turtle.forward(90)
    turtle.right(45)
    turtle.forward(90)
    turtle.left(90)
    #crust
    turtle.color('orange')
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.circle(90)
    turtle.left(90)
    turtle.end_fill()
    #thickness of crust
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.right(90)
    #sauce and cheese
    turtle.color('red')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    #turtle to center
    turtle.up()
    turtle.left(90)
    turtle.forward(80)
    turtle.down()
    #slices
    turtle.color('white')
    num_slices = 8
    num_cuts = int(num_slices/2)
    for i in range(num_cuts):
        turtle.right(360/num_slices)
        turtle.forward(90)
        turtle.right(90)
        turtle.right(90)
        turtle.forward(180)
        turtle.right(90)
        turtle.right(90)
        turtle.forward(90)
    #reposition turtle
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    
def bluesquare_Junha(turtle):
    """
    Author: Junha Kim
    Drawing a blue square
    """
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()

def purplesquare_Daniel (turtle):
    """
    Author: Daniel Ko
    Draws a purple square
    """
    turtle.fillcolor('purple')
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()

def new():
    pass

def bluesquare_Josh(turtle):
    """
    Author: Josh Stob
    Draw a blue square
    """
    turtle = Turtle.turtle
    turtle.fillcolor('blue')
    turtle.beginfill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.endfill()