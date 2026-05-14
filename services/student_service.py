from database import cursor, db


# =========================
# ADD STUDENT
# =========================
def add_student_data(regnum, name, fname, degprog, semnum, marks):
    cursor.execute("""
        INSERT INTO students (regnum, name, fname, degprog, semnum)
        VALUES (%s,%s,%s,%s,%s)
    """, (regnum, name, fname, degprog, semnum))

    student_id = cursor.lastrowid

    for i, mark in enumerate(marks):
        cursor.execute("""
            INSERT INTO marks (student_id, subject, mark)
            VALUES (%s,%s,%s)
        """, (student_id, f"Subject {i+1}", mark))

    db.commit()


# =========================
# READ OPERATIONS
# =========================
def get_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def find_student(regnum):
    cursor.execute("SELECT * FROM students WHERE regnum=%s", (regnum,))
    return cursor.fetchone()


# ⭐ NEW: GET STUDENT ID (IMPORTANT FOR CLEAN ARCHITECTURE)
def get_student_id(regnum):
    cursor.execute("SELECT id FROM students WHERE regnum=%s", (regnum,))
    result = cursor.fetchone()

    if result:
        return result[0]
    return None


# =========================
# DELETE STUDENT
# =========================
def delete_student_data(student_id):
    cursor.execute("DELETE FROM marks WHERE student_id=%s", (student_id,))
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    db.commit()


# =========================
# UPDATE STUDENT
# =========================
def update_student_data(student_id, name, fname, degprog, semnum, marks):
    cursor.execute("""
        UPDATE students
        SET name=%s, fname=%s, degprog=%s, semnum=%s
        WHERE id=%s
    """, (name, fname, degprog, semnum, student_id))

    cursor.execute("DELETE FROM marks WHERE student_id=%s", (student_id,))

    for i, mark in enumerate(marks):
        cursor.execute("""
            INSERT INTO marks (student_id, subject, mark)
            VALUES (%s,%s,%s)
        """, (student_id, f"Subject {i+1}", mark))

    db.commit()