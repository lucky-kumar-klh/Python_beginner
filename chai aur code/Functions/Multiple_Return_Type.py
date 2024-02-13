import math

def circle_stats(rad):

    area = math.pi * (rad**2)
    circumference = math.pi * 2 * rad

    return area, circumference

A, C = circle_stats(5)
print("Area:", A, " Circumference:", C)