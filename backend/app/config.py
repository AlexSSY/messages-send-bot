import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
    WEBHOOK_URL = os.getenv("BACKEND") + WEBHOOK_PATH
    FRONTEND = os.getenv("FRONTEND")
    MY_PHONE = os.getenv("MY_PHONE")
