age = int(input("Enter your age: "))
day = input("Enter booking day: ")
final_price = 0

# if age < 18:
#     final_price += 8
# else: 
#     final_price += 12

# if age 18 and above then keep price as 12 else keep price as 8
final_price = 12 if age > 17 else 8 

if day == "wednesday":
    final_price -= 2
    print("\nYou got a discount of $2 !\n")

print("\nYour Movie ticket Price is $", final_price, end = "\n")