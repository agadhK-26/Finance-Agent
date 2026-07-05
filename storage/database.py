
import sqlite3

DB_NAME = "memory.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        session_id TEXT,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_message(user_id, session_id, role, content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO messages(user_id,session_id,role,content)
    VALUES(?,?,?,?)
    """,(user_id,session_id,role,content))

    conn.commit()
    conn.close()


def load_messages(user_id, session_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    SELECT role,content
    FROM messages
    WHERE user_id=? AND session_id=?
    ORDER BY id
    """,(user_id,session_id))

    rows=c.fetchall()

    conn.close()

    return [{"role":r,"content":c} for r,c in rows]


def get_sessions(user_id):
    conn=sqlite3.connect(DB_NAME)
    c=conn.cursor()

    c.execute("""
    SELECT DISTINCT session_id
    FROM messages
    WHERE user_id=?
    """,(user_id,))

    rows=[x[0] for x in c.fetchall()]

    conn.close()

    return rows