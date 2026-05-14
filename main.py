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

    print("1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Exit")

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

        student_id = input("Enter student ID to delete: ")
    
        query = "DELETE FROM students WHERE id = %s"
    
        cursor.execute(query, (student_id,))
    
        db.commit()
    
        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "4":

        print("Program exited.")
        break

    else:
        print("Invalid choice.")
