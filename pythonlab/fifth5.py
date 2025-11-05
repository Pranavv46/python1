#calculato using operator as input

class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."


calc = calculator()

while True:

  a = float(input("Enter first number :"))
  b = float(input("Enter second number :"))
  oper = input("Enter operator (+, -, *, /) or 'exit' to quit :")
  if oper =="exit":
     print("_______________bye_______________")
     break
  elif oper == '+':
    print("Result:", calc.add(a, b))
  elif oper == '-':
    print("Result:", calc.subtract(a, b))
  elif oper == '*':
    print("Result:", calc.multiply(a, b))
  elif oper == '/':
    print("Result:", calc.divide(a, b))
  else:
    print("Invalid operator!")
