import turtle              # 1. import the modules
import random

def main():
    wn = turtle.Screen()       # 2. Create a screen
    wn.bgcolor('lightgreen')

    lance = turtle.Turtle()    # 3. Create two turtles
    andy = turtle.Turtle()
    craig = turtle.Turtle()
    lance.color('red')
    andy.color('blue')
    lance.shape('turtle')
    andy.shape('turtle')

    craig.hideturtle()
    andy.up()                  # 4. Move the turtles to their starting point
    lance.up()

    #draw finish line
    craig.up()
    craig.goto(100,200)
    craig.right(-90)
    craig.down()
    craig.forward(-400)

    #position turtles
    andy.goto(-100,20)
    lance.goto(-100,-20)

    #set distance counters
    andy_distance = 0
    lance_distance = 0

    # your code goes here
    while True:
        #generate a random number and add it to andys distance
        andy_distance += int(random.random() * 50)
        #reset andys location based in his new distance
        andy.goto(-100 + andy_distance,20)
        lance_distance += int(random.random() * 50)
        lance.goto(-100 + lance_distance, -20)

        #check for a winner
        if andy_distance > 200:
            wn.bgcolor("lightblue")
            print("andy wins")
            break
        if lance_distance > 200:
            wn.bgcolor("orange")
            print("lance wins")
            break


    wn.exitonclick()

if __name__ == '__main__':
    main()