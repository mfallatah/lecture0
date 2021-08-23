import turtle
t= turtle.Turtle()
def ballon(t, color):
    t.speed(5)
    t.color(color)

    for side in range(8):
         t.forward(36)
         t.right(60)
         t.forward(12)
         t.right(90)
         t.forward(12)
         t.right(60)
         t.forward(36)



ballon (t, "green")

