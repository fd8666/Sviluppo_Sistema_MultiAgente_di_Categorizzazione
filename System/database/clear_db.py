from workflow.database.db import get_connection


def clear_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM events_processed;")
    conn.commit()

    conn.close()

if __name__ == "__main__":
    clear_db()

