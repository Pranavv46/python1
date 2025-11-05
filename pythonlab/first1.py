"""
          1.Write a program to print N rows in the following pattern  
            *  
            **  
            ***  
            ****
"""
#input
n =int(input("Enter the number of rows :"))

#loop
for i in range(1,n+1):
    print("*"*i)