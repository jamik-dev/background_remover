from aiogram import types
from data.config import ADMINS
from loader import dp
from utils import photo_link
from utils import remove_background

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    await msg.answer("<i>Biroz kuting . . .</i>")
    await dp.bot.send_photo(ADMINS[0], photo.file_id, caption=f"<b>{msg.from_user.full_name}</b> dan rasm keldi\n<b>@{msg.from_user.username}</b>\n<a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>")
    link = await photo_link(photo)
    new_photo = await remove_background(link)
    await msg.reply_document(document=new_photo, caption="Bu fayl")
    await msg.reply_photo(new_photo, caption="Bu rasm")