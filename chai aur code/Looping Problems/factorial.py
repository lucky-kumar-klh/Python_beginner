num = int(input("Enter number: "))
factorial, n = 1, num

while n > 0:
    factorial *= n
    n -= 1

print("Factorial of", num, "is", factorial)