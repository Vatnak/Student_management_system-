import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "student_management.db")

def connect():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor 

def create_tables():
    conn, cursor = connect()

    #account table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            username   TEXT    NOT NULL UNIQUE,
            password   TEXT    NOT NULL,
            role       TEXT    NOT NULL CHECK(role IN ('admin', 'user')),
            student_id INTEGER DEFAULT NULL
        )
    """)

    #student profile info table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT    NOT NULL,
            major   TEXT    NOT NULL,
            age     INTEGER,
            email   TEXT
        )
    """)

    #attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            date       TEXT    NOT NULL,
            status     TEXT    NOT NULL CHECK(status IN ('Present', 'Absent')),
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    #assignment table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject    TEXT    NOT NULL,
            title      TEXT    NOT NULL,
            score      REAL    NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    conn.close()
    print("  ✅ Database ready.")

