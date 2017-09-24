def triangle(a,b,c):
  if a+b<c or b+c<a or c+a<b:
    print ('No it doesnt form a triangle')
  else:
    print('Yes it forms a triangle')
a=input('Enter a positive integer value for a:')
a=int(a)
b=input('Enter a positive integer value for b:')
b=int(b)
c=input('Enter a positive integer value for c:')
c=int(c)
triangle(a,b,c)


