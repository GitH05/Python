
# 🎓 ATTENDANCE ADMINISTRATION DESKTOP APPLICATION
## 📌 Project Overview

This is a **Python-based desktop application** built using **Tkinter** and **MySQL** to manage:

* Student records
* Daily attendance
* Attendance percentage calculation
* Automatic alerts for low attendance

The project is designed for **beginners** and **academic use**, demonstrating how a GUI application can interact with a database.

---

## 🛠️ Technologies Used

* **Python 3** – Core programming language
* **Tkinter** – GUI (Graphical User Interface)
* **MySQL** – Database
* **PyMySQL** – Python–MySQL connector

---

## ✨ Features

### 👨‍🎓 Student Management

* Add new students
* Store student details in MySQL
* Prevent duplicate email entries

### 📝 Attendance Management

* Record daily attendance
* Attendance status options:

  * Present
  * Absent
  * Late
  * Excused
* Prevent duplicate attendance for the same date

### ⚠️ Attendance Alerts

* Calculate attendance percentage automatically
* Compare attendance against a threshold
* Generate alerts for low attendance

### 🖥️ User Interface

* Simple and beginner-friendly GUI
* Dropdown selection for students
* Pop-up messages for success, warnings, and errors

---

## 🗄️ Database Structure

### 1️⃣ `students` Table

Stores student details.

| Column Name  | Type             | Description               |
| ------------ | ---------------- | ------------------------- |
| student_id   | INT (PK)         | Auto-increment student ID |
| name         | VARCHAR          | Student name              |
| email        | VARCHAR (UNIQUE) | Student email             |
| department   | VARCHAR          | Department name           |
| class        | VARCHAR          | Class name                |
| created_date | DATETIME         | Record creation time      |

---

### 2️⃣ `attendance_records` Table

Stores daily attendance.

| Column Name     | Type     | Description                       |
| --------------- | -------- | --------------------------------- |
| id              | INT (PK) | Auto-increment ID                 |
| student_id      | INT (FK) | Reference to students             |
| attendance_date | DATE     | Attendance date                   |
| status          | VARCHAR  | Present / Absent / Late / Excused |

---

### 3️⃣ `attendance_thresholds` Table

Stores minimum attendance percentage.

| Column Name      | Type     | Description          |
| ---------------- | -------- | -------------------- |
| id               | INT (PK) | Auto-increment ID    |
| percentage_limit | FLOAT    | Minimum attendance % |
| effective_from   | DATE     | Effective date       |

---

### 4️⃣ `alerts_log` Table

Stores attendance alerts.

| Column Name | Type     | Description       |
| ----------- | -------- | ----------------- |
| id          | INT (PK) | Auto-increment ID |
| student_id  | INT (FK) | Student reference |
| alert_type  | VARCHAR  | Alert reason      |
| status      | VARCHAR  | sent / pending    |
| created_at  | DATETIME | Alert timestamp   |

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Packages

```bash
pip install pymysql
```

---

### 2️⃣ Configure Database

Update the database credentials in the Python file:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'college_db'
}
```

---

### 3️⃣ Create Database & Tables

Ensure all required tables are created in MySQL before running the program.

---

### 4️⃣ Run the Application

```bash
python main.py
```

---

## 🧠 Application Workflow

1. Launch the application
2. Add students using the **Add Student** section
3. Record attendance daily
4. Click **Check Attendance Alerts** to detect low attendance
5. Alerts are shown and logged automatically

---

## ⚠️ Important Notes

* Do **not** use `TRUNCATE` on production data
* Always keep a database backup
* Use `DATETIME` for date-related fields instead of `VARCHAR`

---

## 📚 Learning Outcomes

* Understanding Tkinter GUI layouts
* Connecting Python with MySQL
* Executing SQL queries from Python
* Handling exceptions and validations
* Basic database design concepts

---

## 📄 License

This project is for **educational purposes** only.
You are free to modify and enhance it for learning or academic projects.

---

## 🙌 Author

Developed as a **College Management Mini Project** using Python & MySQL.

---

✨ *Happy Coding!*
