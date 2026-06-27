import json
from collections import Counter
from datetime import datetime, timedelta
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
            prompt,
            attack_type,
            confidence,
            risk_score,
            action,
            explanation
        FROM attack_logs
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    attacks = []

    for row in rows:

        explanation = {}

        if row[6]:

            try:

                explanation = json.loads(row[6])

            except json.JSONDecodeError:

                explanation = {}

        attacks.append({

            "timestamp": row[0],
            "prompt": row[1],
            "attack_type": row[2],
            "confidence": row[3],
            "risk_score": row[4],
            "action": row[5],
            "explanation": explanation

        })

    return attacks



def get_threat_trends():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            DATE(timestamp) AS day,
            COUNT(*) AS requests,
            SUM(CASE WHEN action='BLOCK' THEN 1 ELSE 0 END) AS blocked,
            SUM(CASE WHEN action='ALLOW' THEN 1 ELSE 0 END) AS allowed
        FROM attack_logs
        WHERE DATE(timestamp) >= DATE('now', '-6 days')
        GROUP BY DATE(timestamp)
        ORDER BY DATE(timestamp)
    """)

    rows = cursor.fetchall()

    conn.close()

    # ----------------------------------------
    # Convert SQL result to dictionary
    # ----------------------------------------

    db_data = {}

    for row in rows:

        db_data[row[0]] = {

            "requests": row[1],

            "blocked": row[2] or 0,

            "allowed": row[3] or 0

        }

    # ----------------------------------------
    # Always return last 7 days
    # ----------------------------------------

    trends = []

    today = datetime.now().date()

    for i in range(6, -1, -1):

        day = today - timedelta(days=i)

        day_str = day.strftime("%Y-%m-%d")

        display = day.strftime("%b %d")

        values = db_data.get(

            day_str,

            {

                "requests": 0,

                "blocked": 0,

                "allowed": 0

            }

        )

        trends.append({

            "date": display,

            "requests": values["requests"],

            "blocked": values["blocked"],

            "allowed": values["allowed"]

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

def get_detection_module_stats():
    """
    Returns how many incidents were detected by each security module.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT explanation
        FROM attack_logs
        WHERE explanation IS NOT NULL
    """)

    rows = cursor.fetchall()

    conn.close()

    module_counts = {
        "DistilBERT": 0,
        "Presidio": 0,
        "Jailbreak Rule Engine": 0,
        "Role Manipulation Rule Engine": 0,
    }

    import json

    for row in rows:

        if not row[0]:
            continue

        try:

            explanation = json.loads(row[0])

            modules = explanation.get("detection_modules", [])

            for module in modules:

                if module in module_counts:
                    module_counts[module] += 1

        except Exception:
            continue

    return module_counts