import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("owo")


    def init_handlers(self):

        self.handlers.append( owoHandler() )


class owoHandler(MessageHandler):
    def __init__(self):
        self.signal = "owo"

        # params to dispay in help meesages
        self.params = ""

        # displayed when !help is called
        self.short_description = " What's this?"

        # displatyed when !help test is called
        self.long_description = " No really, what is this?"




    async def handle_message(self, client, message, state):

        thing = message.content.lower()
        if self.signal in thing:
            await client.send_message(message.channel, "What's this?")
            
