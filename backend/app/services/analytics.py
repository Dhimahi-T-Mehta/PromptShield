import json
from collections import Counter

from app.database.db import get_connection

def get_total_requests():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM attack_logs"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_blocked_requests():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM attack_logs
        WHERE action='BLOCK'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_allowed_requests():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM attack_logs
        WHERE action='ALLOW'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_attack_distribution():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT attack_type, COUNT(*)
        FROM attack_logs
        GROUP BY attack_type
    """)

    rows = cursor.fetchall()

    conn.close()

    result = {}

    for attack_type, count in rows:
        result[attack_type] = count

    return result


def get_recent_attacks(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            timestamp,
            attack_type,
            confidence,
            risk_score,
            action,
            explanation
        FROM attack_logs
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    attacks = []

    for row in rows:

        explanation = {}

        if row[5]:
            try:
                explanation = json.loads(row[5])
            except json.JSONDecodeError:
                explanation = {}

        attacks.append({

            "timestamp": row[0],

            "attack_type": row[1],

            "confidence": round(row[2], 4),

            "risk_score": row[3],

            "action": row[4],

            "explanation": explanation

        })

    return attacks

def get_threat_trends():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            DATE(timestamp),
            COUNT(*),
            SUM(CASE WHEN action='BLOCK' THEN 1 ELSE 0 END),
            SUM(CASE WHEN action='ALLOW' THEN 1 ELSE 0 END)
        FROM attack_logs
        GROUP BY DATE(timestamp)
        ORDER BY DATE(timestamp)
    """)

    rows = cursor.fetchall()

    conn.close()

    trends = []

    for row in rows:

        trends.append({
            "date": row[0],
            "requests": row[1],
            "blocked": row[2] or 0,
            "allowed": row[3] or 0,
        })

    return trends

def get_threat_intelligence():

    conn = get_connection()
    cursor = conn.cursor()

    # Average Risk Score
    cursor.execute("""
        SELECT AVG(risk_score)
        FROM attack_logs
    """)
    average_risk = cursor.fetchone()[0] or 0

    # Total Incidents
    cursor.execute("""
        SELECT COUNT(*)
        FROM attack_logs
    """)
    total_incidents = cursor.fetchone()[0]

    # Blocked Requests
    cursor.execute("""
        SELECT COUNT(*)
        FROM attack_logs
        WHERE action='BLOCK'
    """)
    blocked = cursor.fetchone()[0]

    blocked_percentage = (
        round((blocked / total_incidents) * 100, 2)
        if total_incidents > 0
        else 0
    )

    # Most Frequent Attack
    cursor.execute("""
        SELECT attack_type, COUNT(*)
        FROM attack_logs
        GROUP BY attack_type
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    most_frequent_attack = row[0] if row else "None"

    # Latest Attack
    cursor.execute("""
        SELECT attack_type
        FROM attack_logs
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    latest_attack = row[0] if row else "None"

    conn.close()

    # Threat Level Logic
    if average_risk >= 85:
        threat_level = "CRITICAL"
    elif average_risk >= 70:
        threat_level = "HIGH"
    elif average_risk >= 50:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    return {

        "current_threat_level": threat_level,

        "average_risk_score": round(average_risk, 2),

        "most_frequent_attack": most_frequent_attack,

        "latest_attack": latest_attack,

        "total_incidents": total_incidents,

        "blocked_percentage": blocked_percentage,

    }