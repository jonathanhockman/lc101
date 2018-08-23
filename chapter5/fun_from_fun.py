"""The True Test"""
import turtle, math
#Creates one part of the curve
def s_time(s,size,angle):
    # TODO make one part of the S
    s.setheading(angle)
    s.forward(size)
    s.left(45)
    s.forward(math.sqrt(2)*size)
    s.right(45)
    s.forward(size)
    s.right(45)
    s.forward(math.sqrt(2)*size)
    s.right(90)
    s.forward(math.sqrt(2)*size)
    s.right(45)
    s.forward(size)
    s.right(45)
    s.forward(0.5*math.sqrt(2)*size)
    s.right(90)
    s.forward(0.5*math.sqrt(2)*size)

def main():
    canvas = turtle.Screen()
    canvas.bgcolor("white")
    #obviously needs to be named Chad
    chad = turtle.Turtle()
    chad.speed(6)
    chad.pensize(5)
    chad.pencolor("red")
    size = 50
    chad.begin_fill()
    s_time(chad,size,90)
    chad.up()
    chad.goto(0,0+3*size)
    chad.down()
    s_time(chad,size,270)
    chad.end_fill()
    canvas.exitonclick()


if __name__ == "__main__":
    main()