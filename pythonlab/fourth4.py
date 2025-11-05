"""
Create a calculator program using OOPS. 
Make sure you create a class Calculator and use its object to access the 
calculator operations such as addition, subtraction, division and multiplication.
"""

class calculator:
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def divide(self,a,b):
        if b !=0:
            return a/b
        else:
            return "Error! Division by zero"

calc = calculator()

a=float(input("enter the first number : "))
b=float(input("enter the second number : ")) 

print("Addition",calc.add(a,b))
print("Subtraction",calc.subtract(a,b))
print("multiplication",calc.multiply(a,b))
print("divition",calc.divide(a,b))
