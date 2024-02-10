age = int(input("Enter Age: "))

if age < 13:
    print("User is Child")
elif age < 20:
    print("User is Teenager")
elif age < 60:
    print("User is an Adult")
else:
    print("User is a Senior Citizen")