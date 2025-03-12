import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден в .env файле!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Бот запущен. 🎉")

@dp.message()
async def echo_message(message: Message):
    await message.answer(message.text)

async def main():
    logging.info("Бот запущен и работает отлично! 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
pip freeze > requirements.txt