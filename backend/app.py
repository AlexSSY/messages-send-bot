import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import uvicorn


load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Bot and Dispatcher
TOKEN = os.getenv("BOT_TOKEN")  # Replace with your bot token
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = os.getenv("BACKEND") + WEBHOOK_PATH  # Replace with your public URL
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
