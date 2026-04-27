import os
from db import create_tables
from auth import seed_account, login

from admin.student_CRUD import (
    add_students,
    delete_students,
    search_students,
    list_students
)

from admin.attendance import(
    add_attendance, 
    vieww_all_attendance
)
from admin.assignment  import (
    add_assignment,
    view_all_assignment
)
from user.profile import (
    view_profile, 
    update_profile
)
from user.attendance import view_my_attedance
from user.assignment import view_my_assignment


def admin_menu(account):
    while True:
        print(f"  ADMIN MENU  |  Logged in as: {account['username']}")
        print("  [1] Add Student")
        print("  [2] Delete Student")
        print("  [3] Search Student")
        print("  [4] List All Students")
        print("  [5] Add Attendance")
        print("  [6] View All Attendance")
        print("  [7] Add Assignment")
        print("  [8] View All Assignments")
        print("  [0] Logout")
        print("=" * 50)

        choice = input("  Choose : ").strip()
        
        if   choice == "1": add_students()
        elif choice == "2": delete_students()
        elif choice == "3": search_students()
        elif choice == "4": list_students()
        elif choice == "5": add_attendance()
        elif choice == "6": vieww_all_attendance()
        elif choice == "7": add_assignment()
        elif choice == "8": view_all_assignment()
        elif choice == "0":
            print(f"\n  Logged out. Goodbye, {account['username']}!")
            break
        else:
            print("  Invalid choice. Please enter a number from the menu.")

def user_menu(account):
    student_id = account["student_id"]
 
    # Safety check — account must be linked to a student
    if not student_id:
        print("   Your account is not linked to a student record.")
        print("     Please contact your admin.\n")
        return
 
    while True:
        print("=" * 50)
        print(f"  STUDENT MENU  |  Logged in as: {account['username']}")
        print("=" * 50)
        print("  [1] View My Profile")
        print("  ─" * 25)
        print("  [2] Update My Profile")
        print("  ─" * 25)
        print("  [3] View My Attendance")
        print("  ─" * 25)
        print("  [4] View My Assignments")
        print("  ─" * 25)
        print("  [0] Logout")
        print("=" * 50)
 
        choice = input("  Choose : ").strip()
 
        if   choice == "1": view_profile(student_id)
        elif choice == "2": update_profile(student_id)
        elif choice == "3": view_my_attedance(student_id)
        elif choice == "4": view_my_assignment(student_id)
        elif choice == "0":
            print(f"\n  Logged out. Goodbye, {account['username']}!\n")
            break
        else:
            print("  Invalid choice. Please enter a number from the menu.\n")


def main():
    # ── First run setup ──────────────────────────────────────────────
    # Make sure data/ folder exists
    os.makedirs(
        os.path.join(os.path.dirname(__file__), "data"),
        exist_ok=True
    )
    create_tables()   # create all tables
    seed_account()   # create default logins

    # ── Main loop ────────────────────────────────────────────────────
    while True:
        print()
        print("=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("  [1] Admin Portal")
        print("  [2] Student Portal")
        print("  [0] Exit")
        print("=" * 50)

        choice = input("  Choose : ").strip()

        if choice == "1":
            account = login(required_role="admin")
            if account:
                admin_menu(account)

        elif choice == "2":
            account = login(required_role="user")
            if account:
                user_menu(account)

        elif choice == "0":
            print("\n  Goodbye!\n")
            break
 
        else:
            print("  Invalid choice. Enter 1, 2, or 0.\n")



if __name__ == "__main__":
    main()

    