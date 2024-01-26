import math

# radius = 20
radius = eval(input("Enter radius: "))

area = (math.pi)*radius**2
# print("type of rad: ",type(radius)," & area: ",type(area))

print("Area of circle is : ", area)
# print("Area of circle is : {area}") # Alternate way to print
# print("Area of circle is : {area: 0.1f}") # for precision

# Use dir() to get a list of all attributes (function, classes, etc)
# list_All = dir(math)
# print(list_All)

# some math functions
print(round(2.5))  # values >= 0.5 will be round to floor, rest ceil
# For rounding to 0.5, if int is odd -> ceil, even -> floor
print(round(3.5)) 
print(round(2.6))
print(round(3.1))

print(abs(-12))
print(abs(0))

print(pow(2,3))
print(pow(2,-3))
