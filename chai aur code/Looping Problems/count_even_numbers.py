num = int(input("Enter Number: "))
even_sum = 0 
for i in range(num+1):
    if (i%2 == 0):
        even_sum += i
print("Even Sum: ", even_sum)