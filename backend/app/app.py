from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from aiogram import types

from .bot import bot, dp
from .depends import get_telegram_user_id
from .config import Config


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(Config.WEBHOOK_URL)
    yield
    await bot.delete_webhook()


load_dotenv()
app = FastAPI(lifespan=lifespan)
query_list = []


origins = [
    "*",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(Config.WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = types.Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


@app.get("/me")
async def get_me(user_id: int = Depends(get_telegram_user_id)):
    return { "telegram_user_id": user_id }


@app.post("/query")
async def query(user_id: int = Depends(get_telegram_user_id)):
    query_list.append(user_id)
    return {"status" : "ok"}
