import turtle

def tringle_boogie(color,start):
    t= turtle.Turtle()
    t.color(color)
    t.speed(5)
    t.width(5)
    t.right(start)
    for shape in range(6):
        for side in range(4):
            t.forward(100)
            t.right(90)
        t.right(15)
    t.hideturtle()

# call that function three times

tringle_boogie("red",0)
tringle_boogie("black",90)
tringle_boogie("orange",180)
tringle_boogie("blue",270)
