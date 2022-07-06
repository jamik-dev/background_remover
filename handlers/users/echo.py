from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("<i>Rasm yuboring</i>\n<b>Eslatma</b>, Rasm foto ko'rinishida bo'lishi lozim, dokument ko'rinishida emas!")
