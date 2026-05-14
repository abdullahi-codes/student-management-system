from services.student_service import *
from utils.validators import get_int, get_float


# =========================
# ADD STUDENT (UI ONLY)
# =========================
def add_student():

    regnum = get_int("Reg No: ")
    name = input("Name: ")
    fname = input("Father: ")
    degprog = input("Program: ")

    marks = []
    for i in range(5):
        mark = get_int(f"Mark {i+1}: ", 0, 100)
        marks.append(mark)

    semnum = get_int("Semester: ", 1, 8)

    add_student_data(regnum, name, fname, degprog, semnum, marks)

    print("Student added!")


# =========================
# SHOW STUDENTS
# =========================
def show_students():
    students = get_all_students()

    print("\n===== STUDENTS =====\n")
    for s in students:
        print(s)


# =========================
# SEARCH STUDENT
# =========================
def search_student():

    regnum = get_int("Reg No: ")

    student = find_student(regnum)

    if student:
        print(student)
    else:
        print("Not found")


# =========================
# DELETE STUDENT
# =========================
def delete_student():

    regnum = get_int("Reg No: ")

    student_id = get_student_id(regnum)

    if student_id:
        delete_student_data(student_id)
        print("Deleted")
    else:
        print("Not found")


# =========================
# UPDATE STUDENT
# =========================
def update_student():

    regnum = get_int("Reg No: ")

    student_id = get_student_id(regnum)

    if not student_id:
        print("Not found")
        return

    name = input("New Name: ")
    fname = input("New Father: ")
    degprog = input("New Program: ")
    semnum = get_int("New Semester: ", 1, 8)

    marks = []
    for i in range(5):
        mark = get_int(f"New Mark {i+1}: ", 0, 100)
        marks.append(mark)

    update_student_data(student_id, name, fname, degprog, semnum, marks)

    print("Updated")


# =========================
# MAIN MENU
# =========================
while True:

    print("\n===== STUDENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter choice: ")

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
        print("Goodbye")
        break

    else:
        print("Invalid choice")