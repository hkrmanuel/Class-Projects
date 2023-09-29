import turtle
import math

wn = turtle.Screen()
wn.bgcolor("green")

def square(t, length):
    for i in range (4) :
        t.forward(length)
        t.left(90)

bob = turtle.Turtle()
bob.shape("turtle")


square(bob, 10)


def polygon (t, length, n):
    turn_angle = 360/n
    for i in range (n) :
        t.forward(length)
        t.left(turn_angle)

poly = turtle.Turtle()
poly.shape("turtle")

polygon(poly, 50, 5)

#Number 4

def circle(t, r):
    circum = 2 * math.pi* r
    length = circum/ r
    
    polygon(t, length, r)


circ = turtle.Turtle()
circ.shape("turtle")

circle(circ, 60)

def arc(t, r, angle):
    circum = 2 * math.pi * r
    length = int(angle / 360 * circum)
    n= 50 
    step_length = length/ n
    step_angle = angle/n
    
    for i in range (n) :
        t.forward(step_length)
        t.left(step_angle)
    
    



    

circ2 = turtle.Turtle() 
circ2.shape("turtle")

arc(circ2, 100, 270)