from aiogram import Bot, Dispatcher, types
from aiogram import filters

from .config import Config


bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(filters.Command("start"))
async def start_command_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Open Web App", web_app=types.WebAppInfo(url=Config.FRONTEND))
            ]
        ]
    )
    await message.answer(text=f"Hello {message.from_user.full_name}!", reply_markup=kb)


@dp.message
async def message_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Open Web App", web_app=types.WebAppInfo(url=Config.FRONTEND))
            ]
        ]
    )
    await message.answer(text=f"Hello {message.from_user.full_name}!", reply_markup=kb)
