from db import connect

def add_assignment():
    print("\n  ── Add Assignment ──────────────────────")
    from admin.student_CRUD import list_students
    list_students()

    try:
        student_id = int(input("Enter Student ID:  ").strip())
    except ValueError:
        print("Invalid Student ID please Enter a number:")
        return
    
    conn, cursor = connect()
    cursor.execute(
        "SELECT name FROM students WHERE id = ?",
        (student_id,)
    )
    student = cursor.fetchone()

    if not student:
        print(f"No student found with ID {student_id}")
        conn.close()
        return
    
    subject = input("Subject:  ").strip()
    title = input("Title:  ").strip()

    if not subject or not title:
        print("Subject and title are required ")
        conn.close()
        return
    
    try:
        score = float(input("Score:").strip())
    except ValueError:
        print("Invalid score Please enter a number:")
        conn.close()
        return
    
    cursor.execute(
        "INSERT INTO assignments (student_id, subject, title, score) VALUES (?, ?, ?, ?)",
        (student_id, subject, title, score)
    )
    conn.commit()
    conn.close()

    print(f"Assignment Added - {student[0]} | {subject} | {title} | {score}")

def view_all_assignment():
    print("\n  ── All Assignment Records ──────────────")

    conn, cursor = connect()
    cursor.execute("SELECT id, name FROM students ORDER BY id")
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("  No students in the database yet.\n")
        return
    
    for student_id, name in students:
        conn, cursor = connect()
        cursor.execute(
            """SELECT subject, title, score FROM assignments
            WHERE student_id = ?
            ORDER BY subject""",
            (student_id,)
        )
        records = cursor.fetchall()
        conn.close()

        print(f"\n  {name} (ID: {student_id})")
        print(f"  {'─' * 55}")

        if not records:
            print("    No assignments yet.")
        else:
            print(f"  {'Subject':<20} {'Title':<22} {'Score'}")
            print(f"  {'───────':<20} {'─────':<22} {'─────'}")
            for subject, title, score in records:
                print(f"  {subject:<20} {title:<22} {score}")

            avg = sum(s for _, _, s in records) / len(records)
            print(f"  {'─' * 55}")
            print(f"  Average Score : {avg:.2f}")

    print()