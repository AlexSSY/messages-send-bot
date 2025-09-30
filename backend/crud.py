import aiosqlite
from pathlib import Path

from .db import DB_NAME


CURRENT_DIR = Path(__file__).parent


async def add_session(telegram_user_id: int, auth_token: str):
    async with aiosqlite.connect(CURRENT_DIR / DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO telethon_sessions (telegram_user_id, auth_token) VALUES (?, ?)",
            (telegram_user_id, auth_token)
        )
        await db.commit()

async def get_sessions_by_user(telegram_user_id: int):
    async with aiosqlite.connect(CURRENT_DIR / DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, telegram_user_id, auth_token FROM telethon_sessions WHERE telegram_user_id = ?",
            (telegram_user_id,)
        )
        rows = await cursor.fetchall()
        return rows

async def get_all_sessions():
    async with aiosqlite.connect(CURRENT_DIR / DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, telegram_user_id, auth_token FROM telethon_sessions"
        )
        rows = await cursor.fetchall()
        return rows

async def delete_session(session_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "DELETE FROM telethon_sessions WHERE id = ?",
            (session_id,)
        )
        await db.commit()
