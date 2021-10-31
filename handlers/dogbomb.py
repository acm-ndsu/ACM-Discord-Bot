
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
            response = await requests.get("https://dog.ceo/api/breeds/image/random")

            await message.channel.send(response["message"])
