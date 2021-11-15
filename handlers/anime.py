
import asyncio
import random
from discord.embeds import Embed
import requests
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("anime")

    def init_handlers(self):

        self.handlers.append(AnimeHandler())


class AnimeHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!anime"

        self.params = "<top> | <bottom>"

        # displayed when !help is called
        self.short_description = "Generates a random anime meme. """

        # displatyed when !help test is called
        self.long_description = "Generates a random anime meme using imgflip api."

        # precache ids
        self.ids = [
            436751,
            188789496,
            72525473,
            139917843,
            157043617,
            145808514,
            137353308,
            60777140,
            131745903,
            298218630,
            108625481,
            113072153,
            31800622,
            11327935,
            7048535,
            1515139,
            32816085,
            106768881,
            57017508,
            661485,
            89690890,
            142411902,
            128810305,
            58183501,
            79424238,
            59550998,
            55696258,
            71855330,
            130860546,
            109171346,
            193080025,
            312960591,
            193877577,
            273023139,
            269124211,
            292107102,
            312253034,
            285480613,
            102723630,
            196656673,
            93010299,
            134305394,
            170630501,
            84106237,
            161386028,
            20026271,
            6714067,
            3834295,
            50060691,
            81402125,
            137001780,
            182760548,
            100521582,
            65559824,
            43219716,
            23275115,
            69456833,
            143647722,
            43725618,
            132884121,
            77177887,
            49076528,
            132136644,
            75561365,
            76948493,
            160575291,
            116313825,
            169131954,
            135505881,
            21719478,
            170419332,
            9296893,
            24474770,
            41333315,
            33433653,
            103190542,
            30416740,
            200117692,
            28326024,
            214508575,
            119965793,
            78495263,
            111437452,
            306957476,
            172996502,
            64176117,
            213436080,
            35149956,
            210403104,
            101275548,
            186617257,
            219806944,
            292020718,
            202507801,
            26678083,
            37706117,
            151361668,
            20313056,
            209873012,
            11684057,
            26433458,
            183525229,
            17120867,
            111574244,
            137379602,
            23296481,
            246768659,
            305787733,
            287340280,
            225053018,
            20858173,
            10248627,
            91614032,
            183124918,
            200170911,
            152862915,
            165269312,
            19707065,
            256088914,
            261434247,
            112665846,
            260734629,
            242837340,
            190521008,
            32860710,
            307420772,
            164007200,
            289411296,
            314380060,
            7987885,
            10705195,
            9417708,
            21832128,
            17119739,
            20301465,
            155702631,
            23669379,
            78913792,
            82824323,
            111436639,
            139005826,
            109200698,
            111657029,
            52161378,
            174464127,
            260167178,
            104537926

        ]

    async def handle_message(self, client, message, state):

        if message.content.lower().startswith(self.signal):

            msg = message.content.replace(self.signal, "")

            if "|" in msg:
                top, bottom = msg.split("|")
            else:
                top = " "
                bottom = msg if msg else " "

            meme_id = random.choice(self.ids)

            response = requests.post("https://api.imgflip.com/caption_image", data={
                "template_id": meme_id,
                "username": "waakis",
                "password": "123abc",
                "text0": top,
                "text1": bottom
            })

            embed = Embed(title= "{0} Meme".format(message.author.mention),color= 10489424)
            embed.set_image(url=response.json()["data"]["url"])

            await message.channel.send(embed = embed)
