def avoids(word, forbidden,a):
  for letter in word:
    if letter in forbidden:
      return a
    return a+1
    
forbidden=input('Enter the forbidden letters')
fin = open(' words.txt' )
a=0
for line in fin:
  word = line.strip()
  a=avoids(word,forbidde,a)
print ('Number of words without forbidden letters : ', a)

