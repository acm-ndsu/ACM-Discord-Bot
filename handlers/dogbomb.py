
import asyncio
import random
import requests
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("dogbomb")

    def init_handlers(self):

        self.handlers.append( DogBombHandler() )


class DogBombHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!dogbomb"

        # displayed when !help is called
        self.short_description = "Prints a random dog image."

        # displatyed when !help test is called
        self.long_description = "Prints a random dog image from thedogapi.com."


    async def handle_message(self, client, message, state):

        if message.content.lower().startswith(self.signal):

            response = requests.post("http://thedogapi.com/api/images/get", params={
                "api_key": "24ecc9b8-721d-458f-bef3-fcfbab7efd2a",
                "format": "html"
            })

            msg = response.text.split('"')[5]

            await message.channel.send(msg)
