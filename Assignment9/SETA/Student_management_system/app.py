
from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5433"
    )

def create_table():
    con = db_connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100)
        )
    """)
    con.commit()
    cur.close()
    con.close()

@app.route("/", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("Name")
        course = request.form.get("Course")

        con = db_connect()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Student (Name, Course) VALUES (%s, %s)",
            (name, course)
        )
        con.commit()
        cur.close()
        con.close()
        return redirect("/")

    return render_template("add.html")

@app.route("/update", methods=["GET", "POST"])
def update():
    con = db_connect()
    cur = con.cursor()

    if request.method == "POST":
        student_id = request.form.get("Student_ID")
        new_course = request.form.get("New_Course")

        cur.execute(
            "UPDATE Student SET Course = %s WHERE Student_ID = %s",
            (new_course, student_id)
        )
        con.commit()

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()
    cur.close()
    con.close()

    return render_template("update.html", students=students)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
