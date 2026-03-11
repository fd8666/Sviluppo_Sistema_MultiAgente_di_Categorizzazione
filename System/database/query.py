import sqlite3
import json
from workflow.database.db import get_connection


def get_all_events():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events_processed")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_by_category(category: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events_processed WHERE category_final=?", (category,))
    rows = cur.fetchall()
    conn.close()
    return rows
