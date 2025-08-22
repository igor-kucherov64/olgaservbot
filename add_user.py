import sqlite3

def add_user(olgaservbot_users, telegram_id, username):
    """
    Добавляет пользователя в базу данных SQLite.

    Args:
        db_name: Имя файла базы данных.
        username: Имя пользователя.
        password: Пароль пользователя.
    """
    try:
        # Устанавливаем соединение с базой данных
        conn = sqlite3.connect(olgaservbot_users)
        cursor = conn.cursor()

        # Создаем таблицу, если она не существует
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        # Добавляем пользователя в таблицу
        cursor.execute("INSERT INTO olgaservbot_users (telegram_id, username) VALUES (?, ?)", (telegram_id, username))

        # Фиксируем изменения
        conn.commit()
        print(f"Пользователь '{username}' успешно добавлен.")

    except sqlite3.IntegrityError:
        print(f"Ошибка: Пользователь '{username}' уже существует.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем соединение
        if conn:
            conn.close()


# Пример использования
add_user("olgaservbot.db", "123", "Igor")
