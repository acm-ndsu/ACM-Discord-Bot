import asyncio
import random
from cowpy import cow
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!cowsay"

        # displayed when !help is called
        self.description = self.signal + " <message> : Makes a cow say your message."

        # displatyed when !help test is called
        self.help = self.signal + """ : !cowsay <message> : Makes a cow say you message.
        The message is a string following the command.
        """



    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):

            msg = message.content.replace(self.signal+" ", "")
            msg = cow.milk_random_cow(msg)

            msg = "```" + msg + "```"

            await client.send_message(message.channel, msg)
