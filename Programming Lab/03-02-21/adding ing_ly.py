def ing(str1):
   length = len(str1)
   if length> 1:
       if str1[-3:] == 'ing':
           str1=str1+'ly'
       else:
           str1=str1+'ing'
   return str1
print(ing('help'))

print(ing('helping'))
