import turtle
t= turtle.Turtle()

for x in range (10):
    if x % 2 ==0:
     t.color("red")
    else:
     t.color("black")
    bead(t)
    t.forward(40)
