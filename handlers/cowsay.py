import asyncio
import random
from cowpy import cow
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("cowsay")

    def init_handlers(self):

        self.handlers.append( CowsayHandler() )

class CowsayHandler(MessageHandler):
    def __init__(self):
        super().__init__()

        self.signal = "!cowsay"

        self.params = "<message>"

        # displayed when !help is called
        self.short_description = "Makes a cow say your message."

        # displatyed when !help test is called
        self.long_description = "Makes a cow say you message. The message is a string following the command."



    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            msg = message.content.replace(self.signal+" ", "")
            msg = cow.milk_random_cow(msg)

            msg = "```" + msg + "```"

            await client.send_message(message.channel, msg)
