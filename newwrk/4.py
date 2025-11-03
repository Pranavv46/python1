#calculate the area of a triangle

import math

a=float(input("enter the first side: "))
b=float(input("enter the second side: "))
c=float(input("enter the third side: "))

s=(a+b+c)/2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"The semi perimeter is {s:.2f} and the area is {area:.2f}")