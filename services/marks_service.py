from utils.grades import calculate_grade_point


# =========================
# ADD MARKS
# =========================
def add_marks(cursor, student_id, marks):

    for subject, mark, credit in marks:

        grade_point = calculate_grade_point(mark)

        cursor.execute("""
            INSERT INTO marks
            (
                student_id,
                subject,
                mark,
                credit_hours,
                grade_point
            )
            VALUES (%s,%s,%s,%s,%s)
        """, (
            student_id,
            subject,
            mark,
            credit,
            grade_point
        ))


# =========================
# DELETE MARKS
# =========================
def delete_marks(cursor, student_id):

    cursor.execute(
        "DELETE FROM marks WHERE student_id=%s",
        (student_id,)
    )


# =========================
# GET MARKS
# =========================
def get_marks(cursor, student_id):

    cursor.execute("""
        SELECT
            subject,
            mark,
            credit_hours
        FROM marks
        WHERE student_id=%s
    """, (student_id,))

    return cursor.fetchall()