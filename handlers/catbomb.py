
import asyncio
import random
import requests
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!catbomb"

        # displayed when !help is called
        self.description = self.signal + " : prints random cat."""

        # displatyed when !help test is called
        self.help = self.signal + """  : prints random cat."""


    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):

            response = requests.post("http://thecatapi.com/api/images/get", params={
                "api_key": "MjIyNDAx",
                "format": "html"
            })

            msg = response.text.split('"')[5]

            await client.send_message(message.channel, msg)
