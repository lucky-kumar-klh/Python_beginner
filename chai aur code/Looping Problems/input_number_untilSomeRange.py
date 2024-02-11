my_numbers = []
while True:
    num = int(input("Enter Number: "))
    if 1 <= num <= 10:
        break
    else:
        my_numbers.append(num)

print("Your entered numbers:", my_numbers)
