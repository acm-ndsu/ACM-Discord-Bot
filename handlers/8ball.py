import asyncio
import random
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!test"

        # displayed when !help is called
        self.description = self.signal + " : Life advice, several keystrokes away!"

        # displayed when !help test is called
        self.help = self.signal + """ : Life advice, several keystrokes away!
        The message is the question you ask.
        """



    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):

            responses = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful",
            ]
            
            choice = 1
            
            if "Ajay" in message:
                choice = random.randint(0,10)
            else:
                choice = random.randint(0,19)
            
            await client.edit_message(message.channel, responses[choice])
