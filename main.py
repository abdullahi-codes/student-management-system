from database import cursor, db

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"

values = (name, age, course)

cursor.execute(query, values)

db.commit()

print("Student added successfully!")

print("\nStudent Records:\n")

query = "SELECT * FROM students"

cursor.execute(query)

students = cursor.fetchall()

for student in students:
    print(student)

from database import cursor, db

while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"

        values = (name, age, course)

        cursor.execute(query, values)

        db.commit()

        print("Student added successfully!")

    elif choice == "2":

        query = "SELECT * FROM students"

        cursor.execute(query)

        students = cursor.fetchall()

        print("\nStudent Records:\n")

        for student in students:
            print(student)

    elif choice == "3":

        print("Program exited.")
        break

    else:
        print("Invalid choice.")
