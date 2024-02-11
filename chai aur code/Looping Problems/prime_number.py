num = int(input("Enter Number: "))
isPrime = True

for i in range(2, num):
    if (num % i) == 0:
        isPrime = False
        break

if isPrime:
    print(num, "is a Prime Number")
else:
    print(num,"is NOT a Prime Number, as it is divisible by")
