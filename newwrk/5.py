#solve the quadratic equation
import cmath

a=1
b=5
c=6

#calculate the discriminant
d = (b**2) - (4*a*c)

#find the roots of the quadratic formula
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The two roots are {0} and {1}".format(sol1,sol2))
