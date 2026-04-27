from db import connect

def seed_account():
    conn, cursor = connect()
    cursor.execute("SELECT COUNT(*) FROM accounts")
    count = cursor.fetchone()[0]

    if count == 0:
        default_accounts = [
            ("admin","admin123", "admin", None)
        ]
        cursor.executemany(
            "INSERT INTO accounts (username, password, \
                role, student_id) VALUES(?, ?, ?, ?)", default_accounts
        )
        conn.commit()
        print("Default account created!")
        print("admin / admin123 -> admin")

    conn.close()

def add_account(username, password, role, student_id=None):
    if role not in ("admin", "user"):
        print("Role must be  'admin' or 'user' ")
        return False
    
    conn, cursor = connect()
    try: 
        cursor.execute(
            "INSERT INTO accounts (username, password, \
                role, student_id) VALUES (?,?,?,?)",
                (username,password,role, student_id)
        )

        conn.commit()
        print("Account Created!")
        return True 
    
    except Exception:
        print(f"{username} already exist try a different onen")
        return False
    
    finally:
        conn.close()

def login(required_role=None):
    print()
    print(" _" * 20)
    print("Please log in to Nakscott Student Management System")
    print(" -" * 20)

    MAX_ATTEMPT = 3

    for attempt in range(1, MAX_ATTEMPT + 1):
        username = input("Username:  ").strip()
        password = input("password:  ").strip()

        conn, cursor = connect()
        cursor.execute(
            """SELECT id, username, role, student_id
            FROM accounts
            WHERE username = ? AND password = ?""",
            (username, password)
        )
        account = cursor.fetchone()
        conn.close()
        
        if not account:
            remaining = MAX_ATTEMPT - attempt
            if remaining > 0:
                print(f"Wrong Username or password {remaining} attempts left")
            else:
                print(f"Too many attempts Accepte denied")
            continue

        acc_id, acc_username, acc_role, acc_student_id = account

        if required_role and acc_role != required_role:
            print(f"This is portal is for {required_role} account only")
            return None
            
        print(f"Welcome {acc_username} Role: {acc_role} to Student Management Portal")
        return {
            "id": acc_id,
            "username": acc_username,
            "role": acc_role,
            "student_id": acc_student_id
        }
    return None
