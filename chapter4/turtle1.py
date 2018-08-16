import turtle

t = turtle.Turtle()
wn = turtle.Screen()

rocket = "rocket_icon.gif"
wn.register_shape(rocket)

t.shape(rocket)
t.speed(1)
t.forward(150)
t.left(90)
t.forward(75)

wn.exitonclick()
