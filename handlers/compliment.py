import asyncio
import random
import pickle
from handlers.message_handler import MessageHandler


class Handler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!compliment"

        #displayed when !help is called
        self.description = self.signal + " : Offers a random compliment."

        #displayed when !help test is called
        self.help = self.signal + """ : Offers a random compliment."""


    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):
            noun = random.choice([
                "heart",
                "face",
                "breath",
                "aura",
                "hand",
                "cookie",
                "voice",
                "eye",
                "ear",
                "hair",
                "cooking",
                "clothing",
                "foot",
                "shoe"
            ])
            verb = random.choice([
                "smells",
                "looks",
                "feels",
                "tastes",
                "sounds",
            ])
            adj = random.choice([
                "like happiness",
                "like joy",
                "like heaven",
                "amazing",
                "like cookies",
                "like a spring breeze"
                "like a haiku",
                "good",
                "unique"
                "adventurous",
                "amiable",
                "exuberant",
                "creative",
                "dynamic",
                "exquisite",
                "tasty",
                "wonderful",
                "sweet",
                "like it exists",
                "satisfactory"
            ])

            phrase = "Your " + noun + " " + verb + " " + adj + "."

            await client.send_message(message.channel, phrase)
