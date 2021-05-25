import turtle
jack = turtle.Turtle()
jack.color("red")

def draw_squre():
    for side in range(4):
        jack.forward(100)
        jack.right(90)
jack.penup()
jack.back(100)
jack.pendown()

draw_squre()
jack.forward(100)
draw_squre()
jack.forward(100)
draw_squre()
      


     



