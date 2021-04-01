def fibi(num):
  n1 = 0
  n2 = 1
  for i in range(0, num):
      print(n1)
      fib = n1 + n2
      n1 = n2
      n2 = fib

fibi(15)
