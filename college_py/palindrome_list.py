list = [1, 2, 3, 2, 10]

isPalindrome = []

isPalindrome = list.copy()
isPalindrome.reverse()

'''
This is also correct
We can directly compare 2 lists using if condition
'''
# if (isPalindrome == list):
#     print("Palindrome List")
# else:
#     print("NOT a Palindrome")

flag = 1
for i in range(len(list)):
    if (list[i] != isPalindrome[i]):
        flag = 0
        break

if (flag): print("Palindrome List")
else: print("NOT a Palindrome List")
