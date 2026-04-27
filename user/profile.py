from db import connect

def view_profile(student_id):

    print("\n  ── My Profile ──────────────────────────")
    conn, cursor = connect()
    cursor.execute(
        "SELECT id, name, major, age, email FROM students WHERE id = ?",
        (student_id,)
    )
    student = cursor.fetchone()
    conn.close()

    if not student:
        print("Profile not found, contact your admin for registar.")
        return
    

    print(f"  {'ID'    :<10} {student[0]}")
    print(f"  {'Name'  :<10} {student[1]}")
    print(f"  {'Major' :<10} {student[2]}")
    print(f"  {'Age'   :<10} {student[3] or '—'}")
    print(f"  {'Email' :<10} {student[4] or '—'}")
    print()


def update_profile(student_id):
    print("\n  ── Update Profile ──────────────────────")

    view_profile(student_id)
    conn, cursor = connect()
    cursor.execute(
        "SELECT name, major, age, email FROM students WHERE id = ?",
        (student_id,)
    )
    current_info = cursor.fetchone()

    if not current_info:
        print("Profile Not found Please Contact your ADMIN for support")
        conn.close()
        return

    current_name, current_major, current_age, current_email = current_info

    print("Press ENTER to keep current value")

    name = input(f"Name {current_name} :  ").strip() or current_name
    major = input(f"major {current_major} :  ").strip() or current_major
    age = input(f"age {current_age} :  ").strip() or current_age
    email = input(f"email {current_email} :  ").strip() or current_email

    cursor.execute(
        """UPDATE students
        SET name = ?, major = ?, age = ?, email = ?
        WHERE id = ?""",
        (name, major, age, email, student_id)
    )
    conn.commit()
    conn.close()

    print("Profile Updated!!")
    view_profile(student_id)


    
