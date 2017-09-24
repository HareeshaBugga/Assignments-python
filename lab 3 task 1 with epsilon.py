def square_root(a,x):
  epsilon=0.0000001
  while True:
    print (x)
    y=(x+a/x)/2
    if abs(y-x)<epsilon:
      break
    x=y
a=input("Enter the value for a:")
a=int(a)
square_root(a,1)

