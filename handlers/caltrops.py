import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler
import json
import requests

class Module(HandlerModule):
    def __init__(self):
        super().__init__("caltrops")


    def init_handlers(self):
        self.handlers.append( caltropHandler() )


class caltropHandler(MessageHandler):
    def __init__(self):
        self.signal = "!caltrop"
        self.catsignal = "!cattrop"

        # params to dispay in help meesages
        self.params = "<type | either none, computer, problem, unusual, random, or cat>"

        # displayed when !help is called
        self.short_description = " Returns an interesting Wiki article to distract you. "

        # displatyed when !help caltrops is called
        self.long_description = " Inspired by XKCD 2467. Essentially just a scrape of https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles "

        with open("./content/unusual.json") as fl:
            self.unusual = json.load(fl)
            
        with open("./content/problem.json") as fl:
            self.problem = json.load(fl)
        
        with open("./content/computers.json") as fl:
            self.computers = json.load(fl)

        with open("./content/cat.json") as fl:
            self.cat = json.load(fl)

    async def format_and_send_async(self, message, link, desc):
        try: 
            send = "{0} | {1} ".format(desc, link)
        except Exception as ex:
            send = "Error encountered. {0}".format(ex)
        await message.channel.send(send)

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
                elif target == 'cat':
                    link, desc = random.choice(list(self.cat.items()))
                elif target == 'random':
                    target = split[1]
                    try:
                        response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary").json()
                        link = response["content_urls"]["desktop"]["page"]
                        # shorten the blurb if it's over 250 characters
                        desc = response["extract"] if len(response["extract"]) < 250 else response["extract"][:250] + "..."
                    except:
                        print(f'Error occurred with api request: {message}')
                else:
                    link, desc = random.choice(list(self.unusual.items()))
            await self.format_and_send_async(message, link, desc)
        elif message.content.lower().startswith(self.catsignal):
            link, desc = random.choice(list(self.cat.items()))
            await self.format_and_send_async(message, link, desc)