import sqlite3

# Создание таблицы (один раз при запуске)
def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            original TEXT,
            translated TEXT
        )
    """)
    conn.commit()
    conn.close()

# Запись нового сообщения
def log_message_to_db(user_id, username, original, translated):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO messages (user_id, username, original, translated)
        VALUES (?, ?, ?, ?)
    """, (user_id, username, original, translated))
    conn.commit()
    conn.close()
