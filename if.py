import turtle
bob = turtle.Turtle()
bob.color("yellow")
bob.width(5)

for side in [1, 2, 3, 4]:
    if side == 4:
        bob.color("purple")
    # المؤشر يمر على اول خانة اذا كانت تساوي 4 يكون لون الخط موف اذا اي رقم اخر يكون اللون اصفر   
   
    bob.forward(100)
    bob.right(90)