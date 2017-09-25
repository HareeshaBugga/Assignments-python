def capitalize_all():
  a=['python','is tricky', ['i know right!']]
  for i in a :
    if type(i) == list:
      for k in i:
        b=k.upper()
    else:
      b=i.upper()
    print (b)
    
capitalize_all()


