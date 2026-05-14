# =========================
# GRADE POINT FUNCTION
# =========================
def calculate_grade_point(mark):

    if mark >= 80:
        return 4.0
    elif mark >= 75:
        return 3.5
    elif mark >= 70:
        return 3.0
    elif mark >= 65:
        return 2.5
    elif mark >= 60:
        return 2.0
    elif mark >= 55:
        return 1.5
    elif mark >= 50:
        return 1.0
    else:
        return 0.0
    

# =========================
# CGPA CALCULATION
# =========================
def calculate_cgpa(marks):

    total_quality_points = 0
    total_credits = 0

    for subject, mark, credit in marks:

        if credit is None or credit <= 0:
            continue

        gp = calculate_grade_point(mark)

        total_quality_points += gp * credit
        total_credits += credit

    if total_credits == 0:
        return 0

    return round(total_quality_points / total_credits, 2)