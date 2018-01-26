
import asyncio
import random
import requests
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("meme", persist_state=False)

    def init_handlers(self):

        self.handlers.append( MemeHandler() )

class MemeHandler(MessageHandler):
    def __init__(self):
        self.signal = "!meme"

        self.params = "<top text> | <bottom text>"

        # displayed when !help is called
        self.short_description = "Generates a random meme. "

        # displatyed when !help test is called
        self.long_description = "Generates a random meme using imgflip api."

        # precache ids
        response = requests.get("https://api.imgflip.com/get_memes")
        self.ids = []
        for meme in response.json()["data"]["memes"]:
            self.ids.append(meme["id"])

    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            msg = message.content.replace(self.signal+" ", "")
            top, bottom = msg.split("|")
            meme_id = random.choice(self.ids)

            response = requests.post("https://api.imgflip.com/caption_image", data={
                "template_id": meme_id,
                "username": "waakis",
                "password": "123abc",
                "text0": top,
                "text1": bottom
            })

            msg = response.json()["data"]["url"]


            await client.send_message(message.channel, msg)
