from db import connect


def view_my_assignment(student_id):
    print("\n  ── My Assignments ──────────────────────")

    conn, cursor = connect()
    cursor.execute(
        "SELECT name FROM students WHERE id = ?", 
        (student_id,)
    )
    student = cursor.fetchone()
    if not student:
        print("Student Record not found, please Contact Your admin")
        conn.close()
        return
    
    cursor.execute(
        """SELECT subject, title, score FROM assignments
        WHERE student_id = ?
        ORDER BY subject""",
        (student_id,)
    )
    records = cursor.fetchall()
    conn.close()

    print(f"Student: {student[0]}")
    if not records:
        print("No assignmen Yet yayyyyy")
        print("Contact your professor")
        return
    
    print(f"  {'Subject':<20} {'Title':<24} {'Score':<8} Grade")
    print(f"  {'───────':<20} {'─────':<24} {'─────':<8} ─────")

    for subject, title, score in records:
        if   score >= 90: letter = "A"
        elif score >= 80: letter = "B"
        elif score >= 70: letter = "C"
        elif score >= 60: letter = "D"
        else:             letter = "F"
        print(f"  {subject:<20} {title:<24} {score:<8} {letter}")

    # Summary
    avg = sum(s for _, _, s in records) / len(records)
    highest = max(s for _, _, s in records)
    lowest  = min(s for _, _, s in records)

    print(f"\n  {'─' * 55}")
    print(f"  Total Assignments : {len(records)}")
    print(f"  Average Score     : {avg:.2f}")
    print(f"  Highest Score     : {highest}")
    print(f"  Lowest Score      : {lowest}")
    print()
