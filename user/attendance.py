from db import connect

def view_my_attedance(student_id):
    print("\n  ── My Attendance ───────────────────────")

    conn, cursor = connect()
    cursor.execute(
        "SELECT name FROM students WHERE id = ?", 
        (student_id,)
    )
    student = cursor.fetchone()

    if not student:
        print("Student Record not found, Contact your admin")
        conn.close()
        return
    
    cursor.execute(
        """SELECT date, status FROM attendance
        WHERE student_id = ?
        ORDER BY date""",
        (student_id,)
    )
    records = cursor.fetchall()
    conn.close()

    print(f"Studnet : {student[0]}")

    if not records:
        print("No attendance Recorded Yet ")
        print("Contact your admin")
        return
    
    print(f"  {'Date':<16} {'Status'}")
    print(f"  {'────':<16} {'──────'}")
    for date, status in records:
        print(f"  {date:<16}  {status}") 
    # Summary
    present_count = sum(1 for _, s in records if s == "Present")
    absent_count  = sum(1 for _, s in records if s == "Absent")
    total         = len(records)
    percentage    = (present_count / total) * 100

    print(f"\n  {'─' * 35}")
    print(f"  Total    : {total}")
    print(f"  Present  : {present_count}")
    print(f"  Absent   : {absent_count}")
    print(f"  Rate     : {percentage:.1f}%")
