import turtle
jack = turtle.Turtle()
jack.color("green")

def draw_m(length):
    for side in range (4):
        jack.forward(length)
        jack.right(90)

draw_m(100)
draw_m(50)
draw_m(25)
