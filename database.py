import mysql.connector


# =========================
# CONNECTION FACTORY
# =========================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Edris@2299",
        database="student_db",
        autocommit=False
    )