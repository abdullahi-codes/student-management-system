import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Edris@2299",
    database="student_db"
)

cursor = db.cursor()