from telebot.async_telebot import AsyncTeleBot

TOKEN = '5855705515:AAGohoX-2G5TtDh7W5V4YJ2TOLl5BGpJV_I'  # poopie123bot
bot = AsyncTeleBot(TOKEN)

from handlers import *
from modules import GameManager

manager = GameManager()

if __name__ == '__main__':
    asyncio.run(bot.polling(non_stop=True))
