# 📚 Student Management System
> A command-line application built with **Python** and **SQLite**

---

## 👥 Team Members

| Name | Role |
|------|------|
| **Nak** | Database Architect & Admin Module |
| **Dara** | User Module & Testing |

**Course:** Computer Science Survey
**University:** American University of Phnom Penh (AUPP)  
**Year:** 2026

---

## 📋 Project Description
This is a Course Final Project submitted by 2 students from the
American University of Phnom Penh (AUPP).

The Student Management System is a terminal-based application that allows an **admin** to manage students, attendance, and assignments, while **students (users)** can view their own profile, attendance, and assignments after logging in.

All data is stored locally in an SQLite database — no internet or external server required.

---

## 🗂️ File Structure

```
Student_management__CSSurvey_project/
│
├── main.py                  ← Run this file to start the program
├── db.py                    ← Database connection + table setup
├── auth.py                  ← Login system for admin and user
├── seed.py                  ← Run once to load sample data
│
├── admin/
│   ├── __init__.py          ← Marks folder as a Python package
│   ├── student_crud.py      ← Add, Delete, Search, List students
│   ├── attendance.py        ← Add and view all attendance
│   └── assignment.py        ← Add and view all assignments
│
├── user/
│   ├── __init__.py          ← Marks folder as a Python package
│   ├── profile.py           ← View and update own profile
│   ├── attendance.py        ← View own attendance
│   └── assignment.py        ← View own assignments
│
└── data/
    └── student_management.db   ← SQLite database (auto-created)
```

---

## 🗄️ Database Tables

| Table | Description |
|-------|-------------|
| `accounts` | Stores login credentials (username, password, role) |
| `students` | Stores student info (name, major, age, email) |
| `attendance` | Stores attendance records (date, Present/Absent) |
| `assignments` | Stores assignments (subject, title, score) |

---

## 🔐 Role Permissions

| Feature | Admin | User |
|---------|:-----:|:----:|
| Login | ✅ | ✅ |
| Add Student | ✅ | ❌ |
| Delete Student | ✅ | ❌ |
| Search Student | ✅ | ❌ |
| List All Students | ✅ | ❌ |
| Add Attendance | ✅ | ❌ |
| View All Attendance | ✅ | ❌ |
| Add Assignment | ✅ | ❌ |
| View All Assignments | ✅ | ❌ |
| View Own Profile | ✅ | ✅ |
| Update Own Profile | ❌ | ✅ |
| View Own Attendance | ❌ | ✅ |
| View Own Assignments | ❌ | ✅ |

---

## ⚙️ Requirements

- Python 3.x
- No external libraries needed — uses only built-in `sqlite3` module

---

## 🚀 How to Run

**Step 1 — Clone or download the project folder**

**Step 2 — Open terminal and navigate to the project folder:**
```bash
cd Student_management__CSSurvey_project
```

**Step 3 — Run seed.py once to set up the database and load sample data:**
```bash
python seed.py
```

**Step 4 — Run the program:**
```bash
python main.py
```

---

## 🔑 Default Login Credentials

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | Admin |
| `nak` | `nak123` | Student |
| `dara` | `dara123` | Student |
| `mia` | `mia123` | Student |

> **Note:** When admin adds a new student, an account is automatically created.  
> Username = student's name in lowercase  
> Password = name + "123" (e.g. `sokha` / `sokha123`)

---

## 📺 Demo Flow

```
python main.py
│
├── [1] Admin Portal
│     Login: admin / admin123
│     ├── Add Student
│     ├── Delete Student
│     ├── Search Student
│     ├── List All Students
│     ├── Add Attendance
│     ├── View All Attendance
│     ├── Add Assignment
│     ├── View All Assignments
│     └── Logout
│
└── [2] Student Portal
      Login: nak / nak123
      ├── View My Profile
      ├── Update My Profile
      ├── View My Attendance
      ├── View My Assignments
      └── Logout
```

---

## 🛡️ Security Features

- **Role-based access** — admin cannot log into student portal and vice versa
- **3 login attempts** — locked out after 3 wrong passwords
- **Parameterized SQL queries** — prevents SQL injection attacks
- **student_id binding** — users can only access their own data

---

## 📝 Sample Data (loaded by seed.py)

**Students:**
| ID | Name | Major | Age | Email |
|----|------|-------|-----|-------|
| 1 | Nak | Artificial Intelligence | 20 | nak@aupp.edu.kh |
| 2 | Dara | Computer Science | 21 | dara@aupp.edu.kh |
| 3 | Mia | Data Science | 19 | mia@aupp.edu.kh |
