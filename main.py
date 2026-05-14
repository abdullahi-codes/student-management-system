from services.student_service import *
from utils.validators import get_int, get_regno, get_name, get_program
from utils.grades import calculate_cgpa


# =========================
# ADD STUDENT (UI ONLY)
# =========================
def add_student():

    regnum = get_regno("Reg No: ")
    name = get_name("Name: ")
    fname = get_name("Father Name: ")
    degprog = get_program("Program: ")

    marks = []

    for i in range(5):
        print(f"\nSubject {i+1}")

        subject = input("Subject Name: ").strip()
        mark = get_int("Mark: ", 0, 100)
        credit = get_int("Credit Hours: ", 1, 4)

        marks.append((subject, mark, credit))

    semnum = get_int("Semester: ", 1, 8)

    add_student_data(regnum, name, fname, degprog, semnum, marks)

    print("Student added successfully!")


# =========================
# SHOW STUDENTS
# =========================
def show_students():

    students = get_students_with_marks()

    print("\n===== STUDENTS WITH MARKS & CGPA =====\n")

    for sid, s in students.items():

        print(f"Reg No: {s['regnum']}")
        print(f"Name: {s['name']}")
        print(f"Father Name: {s['fname']}")
        print(f"Degree Program: {s['degprog']}")
        print(f"Semester: {s['semnum']}")

        print("\nMarks:")

        cgpa_marks = []

        for subject, mark, credit in s["marks"]:

            if credit is None or credit <= 0:
                credit = 0

            print(f"  {subject}: {mark} (Credit: {credit})")
            cgpa_marks.append((subject, mark, credit))

        cgpa = calculate_cgpa(cgpa_marks) if cgpa_marks else 0
        print(f"\nCGPA: {cgpa}")

        print("-" * 40)


# =========================
# SEARCH STUDENT
# =========================
def search_student():

    regnum = get_regno("Reg No: ")

    student = find_student(regnum)

    if student:
        print(student)
    else:
        print("Not found")


# =========================
# DELETE STUDENT
# =========================
def delete_student():

    regnum = get_regno("Reg No: ")

    student_id = get_student_id(regnum)

    if student_id:
        delete_student_data(student_id)
        print("Deleted successfully")
    else:
        print("Not found")


# =========================
# UPDATE STUDENT
# =========================
def update_student():

    regnum = get_regno("Reg No: ")

    student_id = get_student_id(regnum)

    if not student_id:
        print("Not found")
        return

    name = get_name("New Name: ")
    fname = get_name("New Father Name: ")
    degprog = get_program("New Degree Program: ")
    semnum = get_int("New Semester: ", 1, 8)

    marks = []

    for i in range(5):
        print(f"\nSubject {i+1}")

        subject = input("Subject Name: ").strip()
        mark = get_int("Mark: ", 0, 100)
        credit = get_int("Credit Hours: ", 1, 4)

        marks.append((subject, mark, credit))

    update_student_data(student_id, name, fname, degprog, semnum, marks)

    print("Updated successfully")


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