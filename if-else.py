# if/elif statements
grade = int(input("Enter the student's grade: "))
if grade >= 90:
    print("Student got an A")
elif grade >= 80:
    print("Student got a B")
elif grade >= 70:
    print("Student got a C")
elif grade >= 60:
    print("Student got a D")
else:
    print("Student got an F")
