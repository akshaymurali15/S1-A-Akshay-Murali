n=int(input("enter your number"))
fact=1
for i in range(1,n+1):
  fact=fact*i
  print("factorial of {0} is : ".format(n), fact)
