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
        self.params = "<type | either none, computers, problem or unusual>"

        # displayed when !help is called
        self.short_description = " Returns an interesting Wiki article to distract you. "

        # displatyed when !help caltrops is called
        self.long_description = " Inspired by XKCD 2467. Essentially just a scrape of https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles "

        with open("../content/unusual.json") as fl:
            self.unusual = json.load(fl)
            
        with open("../content/problem.json") as fl:
            self.problem = json.load(fl)
        
        with open("../content/computers.json") as fl:
            self.computers = json.load(fl)


    async def handle_message(self, client, message, state):
        
        if message.content.lower().startswith(self.signal):
            split = message.content.split(" ", 1)
            link, desc = ('','')
            if not len(split) > 1:
                choice = random.choice([self.unusual, self.problem, self.computers])
                link, desc = random.choice(list(choice.items()))
            else:
                target = split[1]
                if target == 'problem':
                    link, desc = random.choice(list(self.problem.items()))
                elif target == 'computer':
                    link, desc = random.choice(list(self.computers.items()))
                else:
                    link, desc = random.choice(list(self.unusual.items()))
                    
            try: 
                send = "{0} | {1} ".format(desc, link)
            except KeyError:
                send = "Error encountered."
            await message.channel.send(send)
