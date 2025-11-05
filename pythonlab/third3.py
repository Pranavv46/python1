"""
 Consider the following array  
   [{id:1, name:"rajesh"},{id:2, name: "rahul"},{id:3, name: "srujith"}]  
   Write a program to accept a number and print the name of the student with that id.

"""
students=[
    {"id":1, "name":"rajesh"},
    {"id":2, "name": "rahul"},
    {"id":3, "name": "srujith"}
]

search=int(input("Enter the id:"))

for student in students:
    if student["id"]==search:
        print(f"Name  ::  {student["name"]}")
        break
else:
    print("the given id not found!")
