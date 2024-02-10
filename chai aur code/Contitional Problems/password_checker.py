password = input("Enter your password: ")

lower_case, upper_case, number, special_char = 0, 0, 0, 0


for i in password:
    temp = i
    if temp >= 'a' and temp <= 'z':   # lower case
        lower_case = 1
    elif temp <= 'A' and temp >= 'Z':   # upper case
        upper_case = 1 
    elif int(temp) >= 48 and int(temp) <= 57:   # numerics
        number = 1 
    elif int(temp) >= 33 and int(temp) <= 37:   # special charachters
        special_char = 1

pass_len = len(password)

if pass_len <= 10:
    print("Weak Password, Try again")
elif (pass_len > 10 and lower_case==1 and upper_case==1 and number==1 and special_char==1):
    print("Strong Password")
elif (pass_len > 10 and lower_case==1 and upper_case==1 and number==1 and special_char==0):
    print("No apecial Charachter, Please re enter password again")
else:
    print("Include all the given condition to set a password")