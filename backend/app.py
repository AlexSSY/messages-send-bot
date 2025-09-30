from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = FastAPI()

class Update(BaseModel):
    update_id: int
    message: dict | None = None
    callback_query: dict | None = None

@app.post("/webhook")
async def telegram_webhook(update: Update):
    if update.message:
        chat_id = update.message["chat"]["id"]
        text = update.message.get("text", "")

        if text == "/start":
            await send_message(chat_id, "Привет! Я твой бот 🚀")
    return {"ok": True}

async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(f"{API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": text
        })