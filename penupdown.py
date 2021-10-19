import turtle
t= turtle.Turtle()

# Algorithm
pen_color = input("Enter pen color: ")
fill_color = input("Enter fill color: ")
t.color(pen_color, fill_color)

t.begin_fill()
for _ in range(3):
    t.fd(100)
    t.right(120)
t.end_fill()
t.left(135)
t.fd(100)


t.begin_fill()
for _ in range(3):
    t.fd(100)
    t.right(120)
t.end_fill()
