import asyncio
import logging

from maxapi import Bot, Dispatcher

from bot import MAXBot
from config import TOKEN

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    bot = Bot(TOKEN)
    dp = Dispatcher()

    MaxBot = MAXBot(bot, dp)
    MaxBot.load_cogs()

    asyncio.run(dp.start_polling(bot))
