import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler
import json
import requests
from requests_cache import CachedSession
import requests_cache

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
        self.params = "<category>"

        # displayed when !help is called
        self.short_description = " Returns an interesting Wiki article to distract you. "

        # displatyed when !help caltrops is called
        self.long_description = " Inspired by XKCD 2467. Uses wiki api to generate articles https://en.wikipedia.org/api/rest_v1/ "

        # define session for caching requests, set expire time to be 24 hours (86400 seconds)
        self.session = CachedSession(expire_after=86400, cache_name="caltrops_cache")

    def grab_article(self, title, response):

    async def format_and_send_async(self, message, link, desc):
        try: 
            send = "{0} | {1} ".format(desc, link)
        except Exception as ex:
            send = "Error encountered. {0}".format(ex)
        await message.channel.send(send)

    def handle_message(self, client, message, state):
        if message.content.lower().startswith(self.signal):
            split = message.content.split(" ", 1)
            link, desc = ('','')
            if not len(split) > 1:
                choice = random.choice([self.unusual, self.problem, self.computers])
                link, desc = random.choice(list(choice.items()))
            else:
                target = split[1]
                response = self.session.get("https://en.wikipedia.org/api/rest_v1/page/related/{}".format(target))  
                article_json = random.choice(response.json()["pages"])
                link = article_json["content_urls"]["desktop"]["page"]
                desc = article_json["extract"]
            self.format_and_send_async(message, link, desc)
        elif message.content.lower().startswith(self.catsignal):
            link, desc = random.choice(list(self.cat.items()))
            self.format_and_send_async(message, link, desc)
