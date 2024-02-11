str = input("Enter String: ")
reverse_str = ""
original_str = ""

for ch in str:
    reverse_str = ch + reverse_str
    original_str = original_str + ch

print("Reversed String is ", reverse_str) 
print("Original String is ", original_str)
