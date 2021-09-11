import turtle

def bead(tur):
    tur.right(90)
    for _ in range(3):
        tur.forward(40)
        tur.left(120)
    tur.left(90)
    

t = turtle.Turtle()
t.speed(5)
t.width(3)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(5):
    if n == 3:
        t.color("blue")
    else:
        t.color("red")
    bead(t)
    t.forward(40)