import turtle
pop = turtle.Turtle()
pop.color("yellow")
pop.width(5)

for side in [1, 2, 3, 4]:
    if side == 4:
        pop.color("black")
    pop.forward(100)
    pop.right(90)
