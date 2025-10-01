from fastapi import Header
from fastapi.exceptions import HTTPException
from aiogram.utils.web_app import safe_parse_webapp_init_data
import aiosqlite

from .bot import bot
from .config import Config


async def get_telegram_user_id(init_data: str = Header(..., alias="X-Telegram-Init-Data")) -> int:
    """
    Dependency для FastAPI.
    Принимает initData (строка от Telegram WebApp), валидирует и возвращает user_id.
    """
    try:
        parsed = safe_parse_webapp_init_data(bot.token, init_data)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid initData")

    if not parsed.user:
        raise HTTPException(status_code=401, detail="No user in initData")

    return parsed.user.id


async def get_db():
    db = await aiosqlite.connect(Config.DB_PATH)
    db.row_factory = aiosqlite.Row
    try:
        yield db
    finally:
        await db.close()
