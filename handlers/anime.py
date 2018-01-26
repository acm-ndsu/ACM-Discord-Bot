
import asyncio
import random
import requests
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("anime")

    def init_handlers(self):

        self.handlers.append( AnimeHandler() )


class AnimeHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!anime"

        self.params = "<top> | <bottom>"

        # displayed when !help is called
        self.short_description = "Generates a random anime meme. """

        # displatyed when !help test is called
        self.long_description = "Generates a random anime  meme using imgflip api."

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
            48835181,
            67457456,
            77104422,
            53114009,
            71438489,
            49205105,
            67580477,
            76331267,
            80975850,
            31666916,
            51969741,
            44660853,
            4013622,
            43950101,
            49199381,
            27750606,
            41945860,
            68116873,
            113134097,
            71218628,
            101305547,
            49619379,
            64986519,
            50597830,
            89123027,
            28388155,
            52963738,
            106117641,
            34303382,
            53112845,
            25658529,
            115677867,
            59872333,
            114463489,
            22028330,
            100708736,
            86378411,
            95265591,
            50135595,
            83874167,
            108974740,
            121784562,
            103202143
        ]

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
