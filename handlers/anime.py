
import asyncio
import random
import requests
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!anime"

        # displayed when !help is called
        self.description = self.signal + " <top> | <bottom> : Generates a random anime meme. """

        # displatyed when !help test is called
        self.help = self.signal + """ <top> | <bottom> : Generates a random anime  meme using imgflip api."""

        # precache ids
        self.ids = [
            25807110,
            94397920,
            18174314,
            22220076,
            34416107,
            12474821,
            12993192,
            4597749,
            7339663,
            35535326,
            19104818,
            57423992,
            26921405,
            17626160,
            44571077,
            43405372,
            38950445,
            19622581,
            31239668,
            117332355,
            42888394,
            36733847,
            38271852,
            42673583,
            71304973,
            50135478,
            50638399,
            58286928,
            47153328,
            39726670,
            122956951,
            35276598,
            114668963,
            48835181
        ]

    async def handle_message(self, client, message):

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
