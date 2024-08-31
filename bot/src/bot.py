import logging, asyncio, sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import Message, WebAppInfo

from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
# from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, KeyboardBuilder


from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

load_dotenv("../.env")
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
web_app = WebAppInfo(url="https://webapp.tungulov.space")


def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
    kb = [
        [KeyboardButton(text="Web App", web_app=web_app)],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    return keyboard

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=webAppKeyboard())

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id, reply_markup=webAppKeyboard())
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!", reply_markup=webAppKeyboard())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

def start():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())