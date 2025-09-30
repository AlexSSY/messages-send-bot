import os
from fastapi import FastAPI, Request, Header, Depends
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.web_app import safe_parse_webapp_init_data
from dotenv import load_dotenv
import uvicorn


load_dotenv()
app = FastAPI()


# Разрешённые источники (можно "*" на dev)
origins = [
    "*",
    "http://localhost:5173",  # Vite dev
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # откуда разрешены запросы
    allow_credentials=True,
    allow_methods=["*"],             # GET, POST, PUT, DELETE...
    allow_headers=["*"],             # все заголовки, включая X-Telegram-Init-Data
)


TOKEN = os.getenv("BOT_TOKEN")  
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = os.getenv("BACKEND") + WEBHOOK_PATH
FRONTEND = os.getenv("FRONTEND")


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Open Web App", web_app=types.WebAppInfo(url=FRONTEND))
            ]
        ]
    )
    await message.answer(text=f"Hello {message.from_user.full_name}!", reply_markup=kb)


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()


@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = types.Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


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


@app.get("/me")
async def get_me(user_id: int = Depends(get_telegram_user_id)):
    return {"telegram_user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
