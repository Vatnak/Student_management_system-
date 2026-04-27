from db import create_tables
from auth import seed_account
from db import connect
import os

os.makedirs('data', exist_ok=True)
create_tables()
seed_account()

conn, cursor = connect()

students = [
    ('Nak',  'Artificial Intelligence', 20, 'nak@aupp.edu.kh'),
    ('Dara', 'Computer Science',        21, 'dara@aupp.edu.kh'),
    ('Mia',  'Data Science',            19, 'mia@aupp.edu.kh'),
]
cursor.executemany(
    'INSERT INTO students (name, major, age, email) VALUES (?,?,?,?)',
    students
)

user_accounts = [
    ('nak',  'nak123',  'user', 1),
    ('dara', 'dara123', 'user', 2),
    ('mia',  'mia123',  'user', 3),
]
cursor.executemany(
    'INSERT INTO accounts (username, password, role, student_id) VALUES (?,?,?,?)',
    user_accounts
)

conn.commit()
conn.close()
print('Done! Sample data loaded.')