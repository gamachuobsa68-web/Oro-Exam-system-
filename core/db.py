def get_results():
    conn = sqlite3.connect("exam.db")
    c = conn.cursor()

    c.execute("""
    SELECT student, score
    FROM results
    ORDER BY score DESC
    """)

    data = c.fetchall()

    conn.close()

    return data