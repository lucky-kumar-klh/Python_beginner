num = int(input("Enter number: "))
limit = int(input("Enter table limit: "))
# Printing Multiplication table but skip the 5th iteration
for i in range(1, limit+1):
    if i == 5:
        continue   # continue will skip the below part and continues with next iteration 
    print(num, "x", i, "=", num*i)
