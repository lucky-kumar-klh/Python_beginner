# list = ['Lucky', 'a', 'w']
# print([i.upper() for i in list])

# try:
#     n = int(input("Enter number: "))
# except:
#     print("Enter valid Number!")

# for i in range (n);
#     for j in range (n):
#         if j <= i:
#             print('*', end = " ")
#     print()

# n = int(input("Enter Number: "))
# [print('*'*i) for i in range(1, n+1)]

def fact(n):
    if n < 2:
        return 1
    return n * fact(n-1)

n = 4
print(fact(n))

