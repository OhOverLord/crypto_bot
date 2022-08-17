import asyncio
import logging

from cogwatch import watch
from discord.ext import commands
from settings import SECRET_KEY
from webserver import keep_alive

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
    keep_alive()
    client = Runner()
    await client.start(SECRET_KEY)

if __name__ == '__main__':
    asyncio.run(main())
