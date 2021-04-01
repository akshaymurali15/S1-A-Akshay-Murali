def pyr():
   n = int(input("Enter the number : "))
   i = 1
   for i in range(1, n + 1):
       j = 1
       for j in range(1, i + 1):
           temp = i * j;
           print(temp, end=" ")
       print("")

pyr()
