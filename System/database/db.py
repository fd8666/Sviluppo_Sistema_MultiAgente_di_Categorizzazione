import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "events.db"



def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS events_processed (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER,
            slug TEXT,
            title TEXT,
            description TEXT,
            summary TEXT,
            themes TEXT,
            category_final TEXT,
            category_score REAL,
            category_attempts INTEGER,
            category_excluded TEXT,
            loop_success INTEGER,
            errors TEXT,
            raw_event TEXT,
            UNIQUE(event_id, slug)
        );
    """)

    conn.commit()
    conn.close()
