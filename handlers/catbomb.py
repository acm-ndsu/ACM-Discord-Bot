
import asyncio
import random
import requests
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("catbomb")

    def init_handlers(self):

        self.handlers.append( CatBombHandler() )


class CatBombHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!catbomb"

        # displayed when !help is called
        self.short_description = "Prints a random cat image."

        # displatyed when !help test is called
        self.long_description = "Prints a random cat image from thecatapi.com."


    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            response = requests.post("http://thecatapi.com/api/images/get", params={
                "api_key": "MjIyNDAx",
                "format": "html"
            })

            msg = response.text.split('"')[5]

            await client.send_message(message.channel, msg)
