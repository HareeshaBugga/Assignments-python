def has_no_e(word):
  for letter in word:
    if letter == 'e':
      return (a+1,b)
    else:
      print word
      return (a+1,b+1)
fin = open(' words.txt' )
a=0
b=0
for line in fin:
  word = line.strip()
  (a,b)=has_no_e(word,a,b)
r=(b/a)*100
print ('Percentage of words with no e :', r)


