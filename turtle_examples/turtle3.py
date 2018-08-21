import turtle              # 1. import the modules
import random

def main():
    wn = turtle.Screen()       # 2. Create a screen
    wn.bgcolor('lightblue')

    lance = turtle.Turtle()    # 3. Create two turtles
    andy = turtle.Turtle()
    lance.color('red')
    andy.color('blue')
    lance.shape('turtle')
    andy.shape('turtle')
    lance.speed(2)
    andy.speed(2)

    andy.up()                  # 4. Move the turtles to their starting point
    lance.up()
    andy.goto(-100,20)
    lance.goto(-100,-20)
    finish= 60
    andy_dist= 0
    lance_dist= 0

    # your code goes here
    # how would you utilize randomization
    # how would you implement the for loop?

    for distance in range(0,60):

        # create a random step for each turtle
        andy_step = random.randrange(0,10)
        lance_step = random.randrange(0,10)

        andy_dist += andy_step
        lance_dist += lance_step

        if andy_dist >= finish and andy_dist > lance_dist:
            print("Andy is the winner!")
            break
        elif lance_dist >= finish and lance_dist > andy_dist:
            print("Lance is the winner!")
            break
        #elif andy_dist >= finish and lance_dist >= finish and andy_dist=lance_dist:
            #print("It's a tie!!")
            #break


        # move each turtle for that random distance
        andy.forward(andy_dist)
        lance.forward(lance_dist)




    wn.exitonclick()