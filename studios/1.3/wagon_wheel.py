import turtle
import math

def get_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    return t

def draw_line(length, angle):
    mike = get_turtle()
    mike.left(angle)
    mike.forward(length / 2)
    mike.forward(-length)

def draw_square(length, angle):
    smike = get_turtle()
    smike.up()
    smike.left(angle + 45)
    smike.forward(math.sqrt((length/2)**2 * 2))
    smike.left(180 - 45)
    smike.down()

    for _ in range(4):
        smike.forward(length)
        smike.left(90)

def draw_shape(length, angle):
    draw_line(length, angle)
    draw_line(length, angle + 90)
    draw_square(length, angle)

def main():
    boxes = int(input("How man boxes whould you like to draw? "))
    diameter = int(input("How wide would you like the boxes to be? "))
    wn = turtle.Screen()
    for angle in range(0, 90, int(90/boxes)):
        draw_shape(diameter, angle)

    wn.exitonclick()

if __name__ == '__main__':
    main()
