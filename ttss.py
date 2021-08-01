import turtle
t= turtle.Turtle()
def ballon(t, color):
    t.speed(5)
    t.color(color)

    for side in range(4):
         t.forward(100)
         t.right(90)



ballon (t, "green")

