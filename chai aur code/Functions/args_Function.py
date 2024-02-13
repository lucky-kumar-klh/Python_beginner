def find_sum(*args):
    print(*args)  # All arguments
    for i in args:
        print(i,"", end = "")
    print(args)  # Tuples
    return sum(args)

# print(find_sum(1, 2))
print(find_sum(1, 2, 3, 4))
# print(find_sum(1, 2, 3, 4, 5, 6))