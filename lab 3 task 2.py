import math
def square_root(a,x):
  while True:
    y=(x+a/x)/2
    if y==x:
      print (a,x,math.sqrt(a),(abs(x-math.sqrt(a))))
      break
    x=y
a=input("Enter the value for a:")
a=int(a)
square_root(a,1)

