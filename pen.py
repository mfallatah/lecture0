import turtle
def draw_squar(who, length):
  for side in range(4):  
    who.forward(length)
    who.right(90)

def draw_flower(size, petals):
    doodler=turtle.Turtle()
    doodler.color=("orange")
    doodler.width=(3)
    for petal in range (petals):
        draw_squar(doodler, size)
        doodler.right(360 / petals)
draw_flower(100,7)



