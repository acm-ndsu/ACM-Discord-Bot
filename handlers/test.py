import asyncio
import random
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!test"

        # displayed when !help is called
        self.description = self.signal + " : Calculates and returns random number"

        # displatyed when !help test is called
        self.help = self.signal + """ : Generates a random number between 0 and 10000

        """



    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):

            await client.edit_message(message.channel, 'Your number {}.'.format(random.randint(0, 10000)))
