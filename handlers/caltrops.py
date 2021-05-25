import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler
import json

class Module(HandlerModule):
    def __init__(self):
        super().__init__("caltrops")


    def init_handlers(self):
        self.handlers.append( caltropHandler() )


class caltropHandler(MessageHandler):
    def __init__(self):
        self.signal = "!caltrop"

        # params to dispay in help meesages
        self.params = ""

        # displayed when !help is called
        self.short_description = " Returns an interesting Wiki article to distract you. "

        # displatyed when !help caltrops is called
        self.long_description = " Inspired by XKCD 2467. Essentially just a scrape of https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles "

        with open("../content/caltrops.json") as fl:
            self.caltrops = json.load(fl)


    async def handle_message(self, client, message, state):
        if message.content.lower().startswith(self.signal):
            link, desc = random.choice(list(self.caltrops.items()))
            try: 
                send = "{0} | {1} ".format(desc, link)
            except KeyError:
                send = "Error encountered."
            await message.channel.send(send)
