import turtle
jack = turtle.Turtle()
jack.color("red")

def draw_s():
  for side in range(4):

   jack.forward(100)
   jack.right(90)
draw_s()
jack.forward(100)
draw_s()
jack.back(200)
draw_s()

