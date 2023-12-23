# Airport-information-system-FastAPI
## Используемая СУБД: SQLite
## Инструкции к запуску:
- В командной строке наберите команду cd {путь к файлу main.py}
- Введите uvicorn main:app --reload, чтобы запустить сервер
- Запустите файл main.py
- Перейдите по ссылке http://127.0.0.1:8000/docs
- Созданные эндпоинты для взаимодействия с базой данных позволяют обновлять, удалять и создавать записи в БД (однако не все таблицы имеют такие возможности (например, нельзя удалять клиентов или обновлять данные билета)). Все изменения будут отображаться в БД (можно использовать https://sqliteviewer.app/ для отслеживания).
