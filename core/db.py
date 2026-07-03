import sqlite3

def init_db():
    conn = sqlite3.connect("exam.db")
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
    conn = sqlite3.connect("exam.db")
    c = conn.cursor()

    c.execute("INSERT INTO results (student, score, total) VALUES (?,?,?)",
              (student, score, total))

    conn.commit()
    conn.close()


def get_results():
    conn = sqlite3.connect("exam.db")
    c = conn.cursor()

    c.execute("SELECT student, score FROM results ORDER BY score DESC")
    data = c.fetchall()

    conn.close()
    return data