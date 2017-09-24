import turtle
import math
bob = turtle.Turtle()

def circle(t,r):
circum = 2*math.pi*r

n = int(circum)
length = circum / n
angle = 180/n
for i in range(n):
t.fd(length)
t.lt(angle)

circle(bob,20)
turtle.mainloop()







