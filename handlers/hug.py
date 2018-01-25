import asyncio
import random
import pickle
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("hug", persist_state=True)

    def init_handlers(self):

        self.handlers.append( HugHandler() )
        self.handlers.append( CountHandler() )


class HugHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!hug"

        self.params = "<target>"

        # displayed when !help is called
        self.short_description = "Hugs target."

        # displayed when !help test is called
        self.long_description = "Hugs target and counts how many times they have been hugged."


    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal) and "count" not in message.content:

            # this should allow for !hug @entity message
            split = message.content.split(" ")
            if not len(split) > 1:
                return # bad input
            target = split[1]


            if "counts" not in state:
                state["counts"] = {}

            if target not in state["counts"]:
                state["counts"][target] = 0

            state["counts"][target] += 1

            phrase = random.choice([
                "{} hugs {}.",
                "{} hugs {}. *There there...*",
                "{} hugs {}. *It will all be better soon...*",
                "{} hugs {}. *You'll float too....*",
            ])

            await client.send_message(message.channel, phrase.format(message.author.mention, target))


class CountHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!hug"

        self.params = "count"

        # displayed when !help is called
        self.short_description = "Responds with the number of times you have been hugged."

        # displayed when !help test is called
        self.long_description = "Responds with the number of times you have been hugged."


    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal) and "count" in message.content:

            has_counts = ( "counts" in state and message.author.mention in state["counts"] )
            if has_counts:

                msg = "{} has been hugged {} times".format(message.author.mention, state["counts"][message.author.mention])
                await client.send_message(message.channel, msg)
            else:
                await client.send_message(message.channel, "No hugs for you. So far...")

