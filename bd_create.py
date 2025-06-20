def create_table(cur):
    """Создание таблиц при первом подключении"""
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE,
                    user_name TEXT DEFAULT NULL,
                    user_phone TEXT DEFAULT NULL,
                    user_last_name TEXT DEFAULT NULL,
                    is_send_message BOOLEAN DEFAULT FALSE
                )
            """)