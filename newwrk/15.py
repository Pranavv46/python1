n=int(input("enter the lower limit:"))
a=0
b=1
c=""

print("the sequence is ")
while a<=n:
    print(a,end=" ")
    c=c+str(a)
    nxtnum = a + b
    a = b
    b = nxtnum
    f = open("testfile.txt", "w")
    f.write(c)