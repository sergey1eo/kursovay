from aiogram import Bot
from aiogram.dispatcher import Dispatcher # отвечает за доставку сообщений

from config import TOKEN


bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
