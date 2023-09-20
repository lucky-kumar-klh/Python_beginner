n = int(input('Enter any number :' ))
num = n 
sum = 0
while n != 0 :
    digit = n % 10
    sum = sum + digit**3
    n = n // 10
if ( sum == num ): print('Yes, It is Amstrong Number')
else : print('No, Not an Amstrong Number')
