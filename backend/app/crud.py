import aiosqlite
from pathlib import Path

from app.db import DB_NAME
from app.models import TelethonSession


CURRENT_DIR = Path(__file__).parent


async def add_session(db: aiosqlite.Connection, telegram_user_id: int, phone_number: str, auth_token: str):
    await db.execute(
        "INSERT OR IGNORE INTO telethon_sessions (telegram_user_id, phone_number, auth_token) VALUES (?, ?, ?)",
        (telegram_user_id, phone_number, auth_token)
    )
    await db.commit()


async def get_sessions_by_user(db: aiosqlite.Connection, telegram_user_id: int) -> list[TelethonSession]:
    cursor = await db.execute(
        "SELECT id, telegram_user_id, auth_token FROM telethon_sessions WHERE telegram_user_id = ?",
        (telegram_user_id,)
    )
    rows = await cursor.fetchall()
    return [TelethonSession(**row) for row in rows]
    

async def get_session_by_phone_number(db: aiosqlite.Connection, phone_number: str) -> TelethonSession | None:
    db.row_factory = aiosqlite.Row  # чтобы доставать по именам колонок
    cursor = await db.execute(
        "SELECT * FROM telethon_sessions WHERE phone_number = ?",
        (phone_number,)
    )
    row = await cursor.fetchone()
    await cursor.close()

    if row:
        return TelethonSession(**dict(row))
    return None


async def get_session_by_user_and_phone(db: aiosqlite.Connection, user_id: int, phone_number: str) -> TelethonSession | None:
    db.row_factory = aiosqlite.Row  # чтобы доставать по именам колонок
    cursor = await db.execute(
        "SELECT * FROM telethon_sessions WHERE phone_number = ? AND telegram_user_id = ?",
        (phone_number, user_id)
    )
    row = await cursor.fetchone()
    await cursor.close()

    if row:
        return TelethonSession(**dict(row))
    return None


async def update_session(db: aiosqlite.Connection, telegram_user_id: int, phone_number: str, auth_token: str) -> bool:
    session = await get_session_by_user_and_phone(telegram_user_id, phone_number)
    if not session:
        return False  # записи нет, ничего не обновляем

    await db.execute(
        "UPDATE telethon_sessions SET auth_token = ? WHERE telegram_user_id = ? AND phone_number = ?",
        (auth_token, telegram_user_id, phone_number)
    )
    await db.commit()
    return True


async def get_all_sessions(db: aiosqlite.Connection) -> list[TelethonSession]:
    cursor = await db.execute(
        "SELECT id, telegram_user_id, auth_token FROM telethon_sessions"
    )
    rows = await cursor.fetchall()
    return [TelethonSession(**row) for row in rows]


async def delete_session(db: aiosqlite.Connection, session_id: int):
    await db.execute(
        "DELETE FROM telethon_sessions WHERE id = ?",
        (session_id,)
    )
    await db.commit()
