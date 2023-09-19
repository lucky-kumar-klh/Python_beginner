def isPrime( a ):
  
  for i in range(2,a-1):
    if a % i==0:
      return True
  return False

x = int(input('Enter any number : '))
if isPrime(x):
  print(str(x)+" is Composite Number")
else : print(str(x)+" is a Prime Number")
