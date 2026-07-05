import sqlite3

DB_NAME = "memory.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_message(session_id, role, content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
        (session_id, role, content)
    )

    conn.commit()
    conn.close()


def load_messages(session_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "SELECT role, content FROM messages WHERE session_id=? ORDER BY id",
        (session_id,)
    )

    rows = c.fetchall()

    conn.close()

    return [{"role": r, "content": c} for r, c in rows]


def get_sessions():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT DISTINCT session_id FROM messages")

    sessions = [x[0] for x in c.fetchall()]

    conn.close()

    return sessions