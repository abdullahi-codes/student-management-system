from database import get_connection
from services.marks_service import add_marks, delete_marks
from utils.grades import calculate_cgpa


# =========================
# ADD STUDENT
# =========================
def add_student_data(regnum, name, fname, degprog, semnum, marks):

    db = get_connection()
    cursor = db.cursor()

    try:

        cursor.execute("""
            INSERT INTO students
            (regnum, name, fname, degprog, semnum)

            VALUES (%s,%s,%s,%s,%s)
        """, (
            regnum,
            name,
            fname,
            degprog,
            semnum
        ))

        student_id = cursor.lastrowid

        add_marks(cursor, student_id, marks)

        db.commit()

        return True

    except Exception as e:

        db.rollback()

        print(f"[ERROR] Add Student Failed: {e}")

        return False

    finally:

        cursor.close()
        db.close()


# =========================
# GET ALL STUDENTS
# =========================
def get_all_students():

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    result = cursor.fetchall()

    cursor.close()
    db.close()

    return result


# =========================
# FIND STUDENT
# =========================
def find_student(regnum):

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE regnum=%s",
        (regnum,)
    )

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result


# =========================
# GET STUDENT ID
# =========================
def get_student_id(regnum):

    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "SELECT id FROM students WHERE regnum=%s",
        (regnum,)
    )

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result[0] if result else None


# =========================
# DELETE STUDENT
# =========================
def delete_student_data(student_id):

    db = get_connection()
    cursor = db.cursor()

    try:

        delete_marks(cursor, student_id)

        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (student_id,)
        )

        db.commit()

        return True

    except Exception as e:

        db.rollback()

        print(f"[ERROR] Delete Student Failed: {e}")

        return False

    finally:

        cursor.close()
        db.close()


# =========================
# UPDATE STUDENT
# =========================
def update_student_data(
    student_id,
    name,
    fname,
    degprog,
    semnum,
    marks
):

    db = get_connection()
    cursor = db.cursor()

    try:

        cursor.execute("""
            UPDATE students

            SET
                name=%s,
                fname=%s,
                degprog=%s,
                semnum=%s

            WHERE id=%s
        """, (
            name,
            fname,
            degprog,
            semnum,
            student_id
        ))

        delete_marks(cursor, student_id)

        add_marks(cursor, student_id, marks)

        db.commit()

        return True

    except Exception as e:

        db.rollback()

        print(f"[ERROR] Update Student Failed: {e}")

        return False

    finally:

        cursor.close()
        db.close()


# =========================
# GET STUDENTS WITH MARKS
# =========================
def get_students_with_marks():

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            s.id,
            s.regnum,
            s.name,
            s.fname,
            s.degprog,
            s.semnum,
            m.subject,
            m.mark,
            m.credit_hours

        FROM students s

        LEFT JOIN marks m
        ON s.id = m.student_id
    """)

    rows = cursor.fetchall()

    cursor.close()
    db.close()

    students = {}

    for row in rows:

        student_id = row["id"]

        if student_id not in students:

            students[student_id] = {
                "regnum": row["regnum"],
                "name": row["name"],
                "fname": row["fname"],
                "degprog": row["degprog"],
                "semnum": row["semnum"],
                "marks": []
            }

        if row["subject"] is not None:

            students[student_id]["marks"].append(
                (
                    row["subject"],
                    row["mark"],
                    row["credit_hours"]
                )
            )

    for sid in students:

        students[sid]["cgpa"] = calculate_cgpa(
            students[sid]["marks"]
        )

    return students