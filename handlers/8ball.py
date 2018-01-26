import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("8ball")

    def init_handlers(self):

        self.handlers.append( EightBallHandler() )

class EightBallHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!8ball"

        self.params = "<message>"

        # displayed when !help is called
        self.short_description = "Life advice, several keystrokes away!"

        # displayed when !help test is called
        self.long_description = "Life advice, several keystrokes away!"
        self.long_description += "\nThe message is the question you ask."


    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            if len(message.content.split(" ")) < 2:
                await client.send_message(message.channel, "What?")
            else:
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

                if "ajay" in message.content.lower():
                    choice = random.randint(0,10)
                else:
                    choice = random.randint(0,19)

                await client.send_message(message.channel, responses[choice])
