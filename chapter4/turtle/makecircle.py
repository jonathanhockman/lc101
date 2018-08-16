
import turtle
import math

radius = int(input("Enter radius: "))
sides = int(input("Enter number of sides: "))

step_length = 2 * radius * math.sin(math.pi/sides)
inradius = step_length/(2 * math.tan(math.pi/sides))

print(step_length)
print(inradius)

wn = turtle.Screen()

center = turtle.Turtle()
center.shape("circle")
center.shapesize(1)
center.color("red")

circle = turtle.Turtle()
circle.up()
circle.goto(0, -radius)
circle.down()
circle.color("blue")
circle.circle(radius)
circle.speed(100)


timmy = turtle.Turtle()
3
timmy.up()
timmy.goto(-step_length/2, -inradius)
timmy.down()

for _ in range(sides):
    timmy.forward(step_length)
    timmy.left(360/sides)

wn.exitonclick()