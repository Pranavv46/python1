"""You are working on a simple attendance tracking system for a 5-day workshop.
 You have a list of the number of students present each day: attendance = [18, 20, 19, 15, 21] 
 Your tasks are: Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
 Count how many days the class was full. Calculate and print the total attendance for all 5 days.
"""
attendance = [18, 20, 19, 15, 21]
full_days = 0
total_attendance = 0

for students in attendance:
    if students >= 20:
        print(f"{students} students - Class was Full")
        full_days += 1
    else:
        print(f"{students} students - Class was Not Full")


    total_attendance += students
        
print("\nNumber of days class was full:", full_days)
print("Total attendance over 5 days:", total_attendance)