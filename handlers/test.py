import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("test")


    def init_handlers(self):

        self.handlers.append( TestHandler() )


class TestHandler(MessageHandler):
    def __init__(self):
        self.signal = "!test"

        # params to dispay in help meesages
        self.params = ""

        # displayed when !help is called
        self.short_description = " Calculates and returns random number"

        # displatyed when !help test is called
        self.long_description = " Generates a random number between 0 and 10000"




    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            await client.edit_message(message.channel, 'Your number {}.'.format(random.randint(0, 10000)))
