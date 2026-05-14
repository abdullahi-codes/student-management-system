from database import cursor, db


# Add Student
def add_student():

    regnum = int(input("Enter Registration Number: "))

    name = input("Enter Name: ")

    fname = input("Enter Father's Name: ")

    degprog = input("Enter Degree Program: ")

    marks = []

    for i in range(5):

        while True:

            mark = int(input(f"Enter Marks for Subject {i+1}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break

            else:
                print("Marks must be between 0 and 100.")

    while True:

        semnum = int(input("Enter Semester Number (1-8): "))

        if 1 <= semnum <= 8:
            break

        else:
            print("Invalid Semester Number.")

    while True:

        cgpa = float(input("Enter CGPA (0.0 - 4.0): "))

        if 0.0 <= cgpa <= 4.0:
            break

        else:
            print("Invalid CGPA.")

    query = """
    INSERT INTO students
    (
        regnum,
        name,
        fname,
        degprog,
        sub1,
        sub2,
        sub3,
        sub4,
        sub5,
        semnum,
        cgpa
    )

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        regnum,
        name,
        fname,
        degprog,
        marks[0],
        marks[1],
        marks[2],
        marks[3],
        marks[4],
        semnum,
        cgpa
    )

    cursor.execute(query, values)

    db.commit()

    print("Student added successfully!")


# Show Students
def show_students():

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    print("\n========== STUDENT RECORDS ==========\n")

    for student in students:

        print(f"""
ID: {student[0]}
Registration Number: {student[1]}
Name: {student[2]}
Father Name: {student[3]}
Degree Program: {student[4]}
Marks: {student[5]}, {student[6]}, {student[7]}, {student[8]}, {student[9]}
Semester: {student[10]}
CGPA: {student[11]}
=====================================
""")


# Search Student
def search_student():

    regnum = input("Enter Registration Number to Search: ")

    query = "SELECT * FROM students WHERE regnum = %s"

    cursor.execute(query, (regnum,))

    student = cursor.fetchone()

    if student:

        print(f"""
ID: {student[0]}
Registration Number: {student[1]}
Name: {student[2]}
Father Name: {student[3]}
Degree Program: {student[4]}
Marks: {student[5]}, {student[6]}, {student[7]}, {student[8]}, {student[9]}
Semester: {student[10]}
CGPA: {student[11]}
""")

    else:
        print("Student not found.")


# Delete Student
def delete_student():

    regnum = input("Enter Registration Number to Delete: ")

    query = "DELETE FROM students WHERE regnum = %s"

    cursor.execute(query, (regnum,))

    db.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")

    else:
        print("Student not found.")


# Update Student
def update_student():

    regnum = input("Enter Registration Number to Update: ")

    query = "SELECT * FROM students WHERE regnum = %s"

    cursor.execute(query, (regnum,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    print("Enter New Data")

    name = input("Enter New Name: ")

    fname = input("Enter New Father Name: ")

    degprog = input("Enter New Degree Program: ")

    marks = []

    for i in range(5):

        while True:

            mark = int(input(f"Enter New Marks for Subject {i+1}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break

            else:
                print("Invalid Marks.")

    semnum = int(input("Enter New Semester Number: "))

    cgpa = float(input("Enter New CGPA: "))

    query = """
    UPDATE students

    SET
        name=%s,
        fname=%s,
        degprog=%s,
        sub1=%s,
        sub2=%s,
        sub3=%s,
        sub4=%s,
        sub5=%s,
        semnum=%s,
        cgpa=%s

    WHERE regnum=%s
    """

    values = (
        name,
        fname,
        degprog,
        marks[0],
        marks[1],
        marks[2],
        marks[3],
        marks[4],
        semnum,
        cgpa,
        regnum
    )

    cursor.execute(query, values)

    db.commit()

    print("Student updated successfully!")


# Main Menu
while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")

    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")