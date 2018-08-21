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

    andy.up()                  # 4. Move the turtles to their starting point
    lance.up()
    andy.goto(-100,20)
    lance.goto(-100,-20)

    # your code goes here
    a=0
    b=0

    finish=turtle.Turtle()
    finish.forward(100)
    finish.left(90)
    finish.forward(100)
    finish.right(180)
    finish.forward(200)

    for x in range(0, 100):
        andy_r=int(random.random()*100)
        lance_r=int(random.random()*100)
        andy.forward(andy_r)
        lance.forward(lance_r)
        a+=andy_r
        b+=lance_r
        if a>=200 and b<200:
            print("Andy Wins!")
            break
        if b>=200 and a<200:
            print("Lance Wins!")
            break
        if b>=200 and a>=200:
            if b>a:
                print("Lance Wins!")
                break
            if b>a:
                print("Lance Wins!")
                break
            if a==b:
                print("Tie!")
                break

    wn.exitonclick()