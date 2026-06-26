import json
from datetime import datetime

from app.database.db import get_connection


def log_attack(
    prompt,
    attack_type,
    confidence,
    risk_score,
    action,
    explanation,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attack_logs (
            timestamp,
            prompt,
            attack_type,
            confidence,
            risk_score,
            action,
            explanation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            prompt,
            attack_type,
            confidence,
            risk_score,
            action,
            json.dumps(explanation),
        ),
    )

    conn.commit()
    conn.close()