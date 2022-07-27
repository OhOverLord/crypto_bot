import asyncio
import logging
import os

from cogwatch import watch
from discord.ext import commands
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)



class Runner(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.')

    @watch(path='menus', debug=False, preload=True)
    async def on_ready(self):
        logging.info('Bot ready.')

    async def on_message(self, message):
        if message.author.bot:
            return

        await self.process_commands(message)


async def main():
    client = Runner()
    await client.start('OTkxNzEzODA2NjIxMzU2MDcy.GTC-I1.fanB6K02SIplI5fl7PcdBFbF1jMbm6nKftzilY')

if __name__ == '__main__':
    asyncio.run(main())
