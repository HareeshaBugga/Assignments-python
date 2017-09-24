def square_root(a,x):
  while True:
    print (x)
    y=(x+a/x)/2
    if y==x:
      break
    x=y
a=input("Enter the value for a:")
a=int(a)
square_root(a,1)

