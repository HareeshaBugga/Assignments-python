import turtle
bob = turtle.Turtle()

def polygon(t,n):
for i in range(n):
t.fd(100)
angle = 360/n
t.lt(angle)

polygon(bob,20)
turtle.mainloop()






