import turtle
bob = turtle.Turtle()

r = 12
def circle(t,n):
for i in range(n):
t.fd(r)
angle = 360/n
t.lt(angle)

circle(bob,10)
turtle.mainloop()

import turtle
import math
bob = turtle.Turtle()

def circle(t,r):
circum = 2*math.pi*r
n = int((circum) / 2)
length = circum / n
angle = 360/n
for i in range(n):
t.fd(length)
t.lt(angle)

circle(bob,10)
turtle.mainloop()







