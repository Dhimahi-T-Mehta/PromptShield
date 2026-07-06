from app.database.db import get_connection
from app.database.users import create_users_table

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attack_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prompt TEXT,
            attack_type TEXT,
            confidence REAL,
            risk_score INTEGER,
            action TEXT,
            explanation TEXT
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    create_users_table()
    print("Database initialized successfully.")