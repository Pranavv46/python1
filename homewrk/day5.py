"""
You are managing an online course portal that keeps track of student enrollments in two subjects: "Frontend" and "Backend".
Create two sets:
One with the names of students enrolled in the Frontend course
One with the names of students enrolled in the Backend course
Perform the following tasks:
Add a new student to the Backend course
Remove a student from the Frontend course
Display the list of students who are enrolled in both courses
Display the list of students who are enrolled only in Backend, but not in Frontend
Display the total number of unique students
Create a dictionary where:
Keys are course names ("Frontend", "Backend")
Values are the number of students enrolled in each
Print each course name with the number of students using a loop
Using dictionary comprehension, create a new dictionary that adds a "Fullstack" course by combining student counts from both existing courses.
"""

frontend={"Arjun", "Neha", "Ravi", "Meera"}
backend={"Ravi", "Kiran", "Divya"}

backend.add("suresh")
frontend.remove("Ravi")

both_courses=frontend.union(backend)
print("print all students in both courses:",both_courses)

only_backend=backend.difference(frontend)
print("sstudents only in backenet:",only_backend)

unique_students=frontend.union(backend) 
print("the total no of students:",unique_students)

courses={
    "Frontend":len(frontend),
    "Backend":len(backend)
}

for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")

    updated_courses = {
        **courses,
        "Fullstack": courses["Frontend"] + courses["Backend"]
    }
    print("Updated course list:", updated_courses)