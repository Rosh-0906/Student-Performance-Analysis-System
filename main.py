import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="details"
)

if con:
    print("Connected")
else:
    print("Not connected")

# CRUD OPERATIONS
def add(name, rollno, subject, mark, attendance):
    res = con.cursor()
    query = "insert into students (stud_name, stud_roll, sub_name, sub_mark, stud_atten) values (%s, %s, %s, %s, %s)"
    user = (name, rollno, subject, mark, attendance)
    res.execute(query, user)
    print("\nData inserted successfully :)")
    con.commit()
    print()

def update(name, rollno, subject, mark, attendance):
    res = con.cursor()
    query = "update students set stud_name = %s, sub_name = %s, sub_mark = %s, stud_atten = %s where stud_roll = %s"
    user = (name, subject, mark, attendance, rollno)
    res.execute(query, user)
    con.commit()
    print("\nData updated successfully :)")
    print()


def delete(rollno):
    res = con.cursor()
    query = "DELETE FROM students WHERE stud_roll = %s"
    user = (rollno,)
    res.execute(query, user)
    con.commit()
    print("\nData deleted successfully :)")
    print()

#Develope GPA, Grades

def fetch_students():
    res = con.cursor()
    res.execute("SELECT * FROM students")
    rows = res.fetchall()
    res.close()

    enriched = []
    for row in rows:
        name, rollno, subject, mark, attendance = row[0], row[1], row[2], row[3], row[4]
        grade, gpa = calculate_gpa(mark)
        enriched.append((name, rollno, subject, mark, attendance, grade, gpa))

    headers = ["Name", "Roll No", "Subject", "Mark", "Attendance", "Grade", "GPA"]
    print(tabulate(enriched, headers=headers, tablefmt="grid"))
    print()


def get_grade(mark):          
    if mark >= 91:
        return "O"
    elif mark >= 80:          
        return "A+"
    elif mark > 70:
        return "A"
    elif mark > 50:
        return "B+"
    else:
        return "F"

def calculate_gpa(mark):
    grade_points = {
        "O": 10, "A+": 9, "A": 8, "B+": 7, "F": 0
    }
    grade = get_grade(mark)
    return grade, grade_points[grade]

#chart
def create_dashboard():
    # Read data from MySQL
    df = pd.read_sql("SELECT * FROM students", con)

    # Create Grade Column
    def get_grade(mark):
        if mark >= 91:
            return "O"
        elif mark >= 80:
            return "A+"
        elif mark >= 70:
            return "A"
        elif mark >= 50:
            return "B+"
        else:
            return "F"

    df["Grade"] = df["sub_mark"].apply(get_grade)

    # Dashboard Window
    plt.figure(figsize=(15, 10))
    # -----------------------------
    # 1. Student Marks Bar Chart
    # -----------------------------
    plt.subplot(2, 2, 1)
    plt.bar(df["stud_name"], df["sub_mark"], color="red")
    plt.title("Student Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    # -----------------------------
    # 2. Attendance Chart
    # -----------------------------
    plt.subplot(2, 2, 2)
    attendance = df["stud_atten"].astype(float)
    plt.bar(df["stud_name"], attendance, color="green")
    plt.title("Attendance Percentage")
    plt.xlabel("Students")
    plt.ylabel("Attendance (%)")

    # -----------------------------
    # 3. Grade Distribution
    # -----------------------------
    plt.subplot(2, 2, 3)
    grade_count = df["Grade"].value_counts()
    plt.pie(
        grade_count,
        labels=grade_count.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("\n\nGrade Distribution")

while True:
    print("\n1. Add Details")
    print("2. Update Details")
    print("3. Delete Details")
    print("4. View all students")
    print("5. Performance Dashboard")
    print("6. Exit\n")

    choice = int(input("Enter Choice: "))
    print()

    if choice == 1:
        name = input("Enter Student Name : ")
        rollno = int(input("Enter roll no : "))
        subject = input("Enter Subject name : ")
        mark = int(input("Enter Mark : "))
        attendance = input("Attendance Percentage : ")

        add(name, rollno, subject, mark, attendance)

    elif choice == 2:
        rollno = int(input("Enter roll no : "))
        name = input("Enter Student Name : ")
        subject = input("Enter Subject name : ")
        mark = int(input("Enter Mark : "))
        attendance = input("Attendance Percentage : ")

        update(name, rollno, subject, mark, attendance)

    elif choice == 3:
        rollno = int(input("Rollno: "))
        delete(rollno)
        
    elif choice == 4:
        fetch_students()
        
    elif choice == 5:
        create_dashboard()
        plt.show()

    else:
        print("Exiting application...")
        break