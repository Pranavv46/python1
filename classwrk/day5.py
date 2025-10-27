"""
you are creating a basic system to manage students enrolled in various courses.
Create two sets: one for students enrolled in "Python" and one for "Data Science".
Add a new student to the Python set.
Remove one student from the Data Science set.
Find and display the names of students who are enrolled in both courses.
Find students who are only in the Python course but not in Data Science.
Display the combined list of all students in either course (no duplicates).
Create a dictionary with course names as keys and number of students as values.
Using a loop, print the course name and number of students in the format:
Course: Python, Students: 3
Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled (to simulate expected growth)
"""
python_students = {"Arjun", "Neha", "Ravi"}
data_sci_students = {"Ravi", "Meera", "Kiran"}

python_students.add("divya")
data_sci_students.remove("Kiran")

both_courses=python_students.intersection(data_sci_students)
print("students in both course :",both_courses)

only_python=python_students.difference(data_sci_students)
print("students only in pytho course:",only_python)

all_students=python_students.union(data_sci_students)
print("all students in either courses:",all_students)

course_= {
    "python":len(python_students),
    "data science":len(data_sci_students)
}
for course, count in course_.items():
    print(f"Course: {course}, Students: {count}")
growth_forecast = {course: count * 2 for course, count in course_.items()}
print("Expected growth:", growth_forecast)
