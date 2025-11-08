from maxapi.types import MessageCreated
from maxapi import F

class MAXBot:
    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp

    def load_cogs(self):
        dp = self.dp

        @dp.message_created(F.message.body.text)
        async def echo(event: MessageCreated):
            await event.message.answer(f"{event.message.body.text}")
