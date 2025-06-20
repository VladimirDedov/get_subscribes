import sqlite3
from contextlib import contextmanager

from bd_create import create_table


@contextmanager
def get_db_connection(db_name: str = "users.db"):
    """Подключение к БД"""
    conn = sqlite3.connect(db_name)
    try:
        cur = conn.cursor()
        create_table(cur)  # Если таблиц нет, то создать
        yield cur
        conn.commit()
    except Exception as err:
        print(f"Не удалось подключиться или создать БД\n {err}")
        conn.rollback()
    finally:
        conn.close()


def write_user_to_bd(list_of_data: tuple):
    with get_db_connection("users.db") as cur:

        for tp in list_of_data:
            cur.execute("INSERT OR IGNORE INTO users(user_id, user_name, user_phone, user_last_name) "
                        "VALUES(?,?,?,?)",
                        tp)
            print('Пользователи записаны')


if __name__ == '__main__':
    def get_text(st):
        return tuple([s.strip() for s in st.split('|')])


    with open("users.txt", 'r', encoding="utf-8") as f:
        usernames = [line.strip() for line in f if line]
        tuple_users = tuple(map(get_text, usernames))

    print(tuple_users)

    write_user_to_bd(tuple_users)