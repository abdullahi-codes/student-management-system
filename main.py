from database import cursor, db

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"

values = (name, age, course)

cursor.execute(query, values)

db.commit()

print("Student added successfully!")