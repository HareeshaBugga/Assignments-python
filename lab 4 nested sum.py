t= [1,2,3,4,[2,3,4,5,6]]

my_list=[]
for item in t:
  my_list.append(item)
  list_of_list=[]
  my_sum=0
  while True:
    value = my_list.pop()
    if isinstance(value,int):
      my_sum+=value
    else:
      list_of_list.append(value)
    if len(my_list)==0:
      if len(list_of_list)==0:
        break
      else:
        my_list = list_of_list.pop()
        
print(my_sum)



