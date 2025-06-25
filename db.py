import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get("DATABASE_URL")

def insert_message(user_id, username, original, translated, country):
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO messages (user_id, username, original, translated, country)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, username, original, translated, country))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[DB Error] Failed to insert message: {e}")