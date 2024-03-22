import cool_drawings, turtle

functions = [getattr(cool_drawings, func) for func in dir(cool_drawings) if callable(getattr(cool_drawings, func))]

pen = turtle.Turtle()
pen.speed(0)

for i, func in enumerate(functions):
    pen.penup()
    pen.goto(-350+(i%7)*200, 350-(i//7)*200)
    pen.pendown()
    func(pen)
    
turtle.exitonclick()
