import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("expenses.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                note TEXT DEFAULT '',
                date TEXT NOT NULL
            )
            """
        )


def add_expense(amount, category, note, date):
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
            (amount, category.lower(), note, date),
        )
        return cur.lastrowid


def list_expenses():
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM expenses ORDER BY date DESC, id DESC"
        ).fetchall()

def delete_expense(expense_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        return cur.rowcount > 0     

def summary_by_category():
    with get_conn() as conn:
        return conn.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
            """
        ).fetchall()    