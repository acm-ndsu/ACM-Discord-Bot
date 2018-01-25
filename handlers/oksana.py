import asyncio
import random
import pickle
from handlers.message_handler import MessageHandler


class Handler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!oksana"

        # displayed when !help is called
        self.description = self.signal + " : quotes Oksana"

        # displayed when !help test is called
        self.help = self.signal + """ : quotes Oksana."""


    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):
            phrase = random.choice([
                "You all have decision to make, drop class and be happy or stay in class and suffer. Your choice.",
                "You are lucky people. No pen, no book, no knowledge, and you are happy.",
                "Everyone with the code",
                "It is not a problem with the server it is a problem with the Monday",
                "Now I will show you the face of the person who is responsible for all this trouble, atleast you will have the enemy in front of you.",
                "I will wait for you to log in and then we will do the blah blah blah",
                "If you make decision to be in my class, be strong, drink milk, take the vitamins",
                "International students, if you are traveling home, do your best not to fail the class",
                "Welcome to the new trouble in your life"
            ])

            await client.send_message(message.channel, phrase)

