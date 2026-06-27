# Student Performance Analysis System

## About the Project

The Student Performance Analysis System is a Python-based application developed to manage student academic records and analyze their performance. It allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student data stored in a MySQL database.

Apart from managing records, the application calculates each student's grade and GPA based on their marks. It also provides a simple performance dashboard using Pandas and Matplotlib to visualize student marks, attendance, grade distribution, and subject-wise average marks.

This project was built as a learning project to improve my understanding of Python programming, SQL database integration, data analysis, and data visualization.

---

## Features

- Add new student records
- Update existing student details
- Delete student records
- View all student records
- Calculate Grades and GPA automatically
- Generate a performance dashboard
- Analyze attendance percentages
- Display subject-wise average marks
- Visualize grade distribution using charts

---

## Technologies Used

- Python
- MySQL
- Pandas
- Matplotlib
- mysql-connector-python
- Tabulate

---

## Project Structure

```
Student-Performance-Analysis-System/
│
├── main.py
├── students.sql
├── README.md
└── screenshots/
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Student-Performance-Analysis-System.git
```

### 2. Navigate to the project folder

```bash
cd Student-Performance-Analysis-System
```

### 3. Install the required libraries

```bash
pip install mysql-connector-python pandas matplotlib tabulate
```

### 4. Import the database

Import the `students.sql` file into your MySQL server.

### 5. Update the database connection

Open `main.py` and update the following details according to your MySQL setup:

```python
host="localhost"
user="root"
password="your_password"
database="details"
```

### 6. Run the project

```bash
python main.py
```

---

## Dashboard

The application provides a simple dashboard that includes:

- Student Marks
- Attendance Percentage
- Grade Distribution
- Subject-wise Average Marks

These charts are created using Pandas and Matplotlib to make student performance easier to understand.

---

## What I Learned

While building this project, I learned how to:

- Connect Python with MySQL
- Perform CRUD operations using SQL
- Work with Pandas DataFrames
- Create visualizations using Matplotlib
- Organize a Python project
- Handle and analyze student data

---

## Future Improvements

- Student Rank Calculation
- Export reports to PDF and Excel
- Search student by Roll Number
- User Login System
- GUI using Tkinter
- Better dashboard with more analytics

---

## Author
**Roshni**
