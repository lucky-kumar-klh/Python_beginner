str = input("Enter String: ")

for char in str:
    if str.count(char) == 1:
        print("1st Non-Repeated cha is ", char)
        break
