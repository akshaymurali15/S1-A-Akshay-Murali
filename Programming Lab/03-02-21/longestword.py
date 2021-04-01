def str1(word):
  w=[]
  for n in word:
     w.append((len(n),n))
  w.sort()
  result=w[-1][0]
  result1=w[-1][1]
  print("longest word is : ",result1)
  print("length of the word is : ",result)

str1(['cronaldo', 'Beckham', 'ozil'])
