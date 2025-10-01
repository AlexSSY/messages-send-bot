import os
import aiosqlite
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


DB_NAME = os.getenv("DB_NAME")
SQL_DIR = Path(__file__).parent


async def _execute_sql_file(filename: str):
    path = SQL_DIR / filename
    async with aiosqlite.connect(DB_NAME) as db:
        sql = path.read_text()
        await db.executescript(sql)
        await db.commit()


async def create_db():
    """Создать таблицу и индекс"""
    await _execute_sql_file("create_db.sql")


async def drop_db():
    """Удалить индекс и таблицу"""
    await _execute_sql_file("drop_db.sql")


async def reset_db():
    """Сброс базы данных: дроп + создание"""
    await drop_db()
    await create_db()
