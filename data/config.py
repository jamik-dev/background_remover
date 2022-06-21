# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
# bla bla
import os
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = []
a = (os.environ.get("ADMINS"))
ADMINS.append(a)
IP = str(os.environ.get("ip"))