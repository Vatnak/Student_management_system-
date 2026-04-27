from db import connect
from auth import add_account

def add_students():
    print("\n  ── Add Student ─────────────────────────")
    name  = input("  Name  : ").strip()
    major = input("  Major : ").strip()
    age   = input("  Age   : ").strip()
    email = input("  Email : ").strip()

    if not name or not major:
        print("Name and Major Require")
        return None
    

    conn, cursor = connect()
    cursor.execute(
        "INSERT INTO students (name, major, age, email) VALUEs (?,?,?,?)",
        (name, major, age, email)
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    print(f"Student Added - {name} (ID:{student_id})")

    username = name.lower()
    password = name.lower() + "123"
    add_account(username, password, "user", student_id)
    print(f"Account created - Username: {username}, Password: {password}")
    return student_id


def list_students():
    conn, cursor = connect()
    cursor.execute(
        "SELECT id, name, major, age, email FROM students ORDER BY id"
    )
    rows = cursor.fetchall()
    conn.close()

    print()
    if not rows:
        print("No student in the database")
        return
    
    print(f"  ── All Students ({'─' * 40}")
    print(f"  {'ID':<6} {'Name':<20} {'Major':<22} {'Age':<6} {'Email'}")
    print(f"  {'──':<6} {'────':<20} {'─────':<22} {'───':<6} {'─────'}")
    for row in rows:
        print(f"  {row[0]:<6} {row[1]:<20} {row[2]:<22} {str(row[3]):<6} {row[4] or '—'}")
    print()


def delete_students():
    print("\n  ── Delete Student ──────────────────────")
    list_students()

    try:
        student_id = int(input("Enter student ID to delete:  ").strip())
    except ValueError:
        print("Invalid ID, Please enter a number")
        return

    conn, cursor = connect()

    cursor.execute(
        "SELECT name FROM students WHERE id = ?", 
        (student_id,)
    )
    student = cursor.fetchone()

    if not student:
        print(f"No student found in the databased with that ID {student_id}")
        conn.close()
        return
    

    confirm = input(f"Are you sure you want to delete this student name: {student[0]} (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Delete action cancelled!")
        return
    

    cursor.execute("DELETE FROM attendance  WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM assignments WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM accounts    WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM students    WHERE id = ?",         (student_id,))

    conn.commit()
    conn.close()
    print(f"Succesfully delete student name: {student[0]} From the database")

def search_students():
    print("\n  ── Search Student ──────────────────────")
    keyword = input("  Enter name to search : ").strip()

    if not keyword:
        print("Please Enter the name of the student to search:")
        return
    
    conn, cursor = connect()
    cursor.execute(
        """SELECT id, name, major, age, email
        FROM students
        WHERE name LIKE ?
        ORDER BY name""",
        (f"%{keyword}%",) 
    )
    results = cursor.fetchall()
    conn.close()

    print()
    if not results:
        print(f"  No students found matching '{keyword}'.\n")
        return

    print(f"  Found {len(results)} result(s) for '{keyword}':")
    print(f"  {'─' * 60}")
    print(f"  {'ID':<6} {'Name':<20} {'Major':<22} {'Age':<6} {'Email'}")
    print(f"  {'──':<6} {'────':<20} {'─────':<22} {'───':<6} {'─────'}")
    for row in results:
        print(f"  {row[0]:<6} {row[1]:<20} {row[2]:<22} {str(row[3]):<6} {row[4] or '—'}")
    print()
