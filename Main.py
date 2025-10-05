from turtle import *
from random import randint
import time
import threading

def winer(t):
    t.goto(-150,100)
    goto(-120, 80)
    pendown()
    write('- Winer!', move=False, align="left", font=("Arial", 20, "normal"))

def dance(t):
    t.pendown()
    for i in range(350):
        t.forward(randint(4,40))
        t.right(randint(20,70))


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

t1.speed(20)
t2.speed(20)
t3.speed(20)
t4.speed(20)

t1.penup()
t2.penup()
t3.penup()
t4.penup()

t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')
t4.shape('turtle')

t1.color('red')
t2.color('green')
t3.color('blue')
t4.color('black')#nigga

penup()
goto(-300,65)
right(90)
pendown()
forward(180)
penup()

t1.goto(-300,50)
t2.goto(-300,0)
t3.goto(-300,-50)
t4.goto(-300,-100)

penup()
goto(100,65)
pendown()
forward(180)
penup()


while t1.xcor()<100 and t2.xcor()<100 and t3.xcor()<100 and t4.xcor()<100:
    t1.forward(randint(1,10))
    t2.forward(randint(1, 10))
    t3.forward(randint(1, 10))
    t4.forward(randint(1, 10))


win = max(t1.xcor(),t2.xcor(),t3.xcor(),t4.xcor())
if win == t1.xcor():
    winer(t1)
    time.sleep(8)
    dance(t1)
if win == t2.xcor():
    winer(t2)
    time.sleep(8)
    dance(t2)
if win == t3.xcor():
    winer(t3)
    time.sleep(8)
    dance(t3)
if win == t4.xcor():
    winer(t4)
    time.sleep(8)
    dance(t4)

exitonclick()