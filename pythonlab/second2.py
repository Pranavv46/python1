"""
2.Write a program to accept a number and print its multiplication table till 10 rows.
"""
#input
num=int(input("Enter a number :"))
print(f"The multiplication of {num} is :")

#loop
for i in range(1,11):
    print(f" {num}  x {i} = {num*i}")