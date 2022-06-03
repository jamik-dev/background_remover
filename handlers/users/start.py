from aiogram import types
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! \nRasmingizni yuboring!")
    await dp.bot.send_message(ADMINS[0], f"<b>{message.from_user.full_name}</b> botni ishga tushirdi!\n<b>@{message.from_user.username}</b>\n<a href='tg://user?id={message.from_user.id}'>{message.from_user.id}</a>")

