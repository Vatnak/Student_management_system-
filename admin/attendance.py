from db import connect

def add_attendance():
    print("\n  ── Add Attendance ──────────────────────")


    from admin.student_CRUD import list_students
    list_students()

    try:
        student_id = int(input("Enter student ID:").strip())
    except ValueError:
        print("Invalid Student_Error please Enter a number")
        return
    
    conn, cursor = connect()
    cursor.execute(
        "SELECT name FROM students WHERE id= ?", (student_id,)
    )
    student = cursor.fetchone()

    if not student:
        print(f"Student not found with ID {student_id}")
        conn.close()
        return
    
    date = input("DATE(YYYY-MM-DD):  ").strip()
    if not date:
        print("date is required ")
        conn.close()
        return

    print("Status option: [1]: Present, [2]:Absent")
    status_choice = input("Please Select (1 or 2):")

    if status_choice == "1":
        status = "Present"
    elif status_choice == "2":
        status = "Absent"
    else:
        print("Invalid Choice Pleae select 1 or 2")
        conn.close()
        return
    
    cursor.execute(
        "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
        (student_id, date, status)
    )
    conn.commit()
    conn.close()
    print(f"Attendance Recored {student[0]}| {date}| {status}")

def vieww_all_attendance():
    print("\n  ── All Attendance Records ──────────────")
    conn, cursor = connect()
    cursor.execute(
        "SELECT id, name FROM students ORDER BY id"
    )
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("No students in the databased yet")
        return
    
    for student_id, name in students:
        conn, cursor = connect()
        cursor.execute(
            """SELECT date, status FROM attendance
            WHERE student_id = ?
            ORDER BY date""",
            (student_id,)
        )
        records = cursor.fetchall()
        conn.close()

        print(f"\n  {name} (ID: {student_id})")
        print(f"  {'─' * 35}")

        if not records:
            print("    No attendance records yet.")
        else:
            present_count = sum(1 for _, s in records if s == "Present")
            absent_count  = sum(1 for _, s in records if s == "Absent")

            print(f"  {'Date':<16} {'Status'}")
            print(f"  {'────':<16} {'──────'}")
            for date, status in records:
                print(f"  {date:<16} {status}")

            print(f"  {'─' * 35}")
            print(f"  Present: {present_count}  |  Absent: {absent_count}")

    print()
