import sqlite3

from app.database.db import get_connection


def create_users_table():
    with get_connection() as conn:
        cursor = conn.cursor()
    """
    Create the users table if it does not already exist.
    """

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'analyst',
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def get_user_by_username(username: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,),
    )

    user = cursor.fetchone()

    conn.close()

    return user

def create_user(
    username: str,
    full_name: str,
    email: str,
    password_hash: str,
    role: str = "analyst",
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            full_name,
            email,
            password_hash,
            role
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            username,
            full_name,
            email,
            password_hash,
            role,
        ),
    )

    conn.commit()
    conn.close()