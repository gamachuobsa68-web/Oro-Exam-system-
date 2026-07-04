import sqlite3

DB_NAME = "exam.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student TEXT,
        score INTEGER,
        total INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_result(student, score, total):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO results (student, score, total)
    VALUES (?, ?, ?)
    """, (student, score, total))

    conn.commit()
    conn.close()


def get_results():

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    SELECT student, score, total
    FROM results
    ORDER BY score DESC
    """)

    data = c.fetchall()

    conn.close()
    return data