import turtle




def ballon(t, color):
    t.speed(0)
    t.color(color)

    # Draw ballon body.
    for side in range(30): # 30 ضلع 
        t.forward(10)
        t.left(12)         # قسمنا 360/30 

    # Draw ballon knot. العقدة
    t.right(60)
    for side in range (3):
        t.forward(10)
        t.right(120)

    # Draw ballon string.
    t.color ("gray")
    t.right(30)            # الخط الرصاصي تحت الدائرة
    t.forward (100)        # طول الخط الرصاصي

t = turtle.Turtle()

t.penup()                 # يخفي الخط اللي يرسمه المؤشر
t.back(100)
t.pendown()               # يظهر المؤشر 
ballon(t, "red")

t.penup()                 # move without drawing
t.home()                  # used to move the turtle to origin coordinates 
t.pendown()
ballon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
ballon(t, "purple")

t.penup()
t.home()
t.forward(200)
t.pendown()
ballon(t, "green")

t.hideturtle()


