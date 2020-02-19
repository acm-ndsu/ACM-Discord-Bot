import asyncio
import random
import pickle
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("slap", persist_state=True)

    def init_handlers(self):

        self.handlers.append( SlapHandler() )
        self.handlers.append( SlapCountHandler() )

class SlapHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!slap"

        self.params = "<target>"

        # displayed when !help is called
        self.short_description = "Slaps target."

        # displayed when !help test is called
        self.long_description = "Slaps target."

    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):
            split = message.content.split(" ", 1)
            if not len(split) > 1:
                return # bad input
            target = split[1]

            if target in ["count", "slap count"]:
                return

            if "counts" not in state:
                state["counts"] = {}

            if target not in state["counts"]:
                state["counts"][target] = 0
            state["counts"][target] += 1

            phrase = random.choice([
                "{} slaps {} with a trout.",
                "{} beats {} with a wet noodle.",
                "{} slaps {} around a bit with a large trout.",
                "{} slaps {} around a bit with a diet trout small.",
                "{} slaps {} around a bit with a trout small.",
                "{} slaps {} around a bit with a minnow"
            ])

            await message.channel.send(phrase.format(message.author.mention, target))


class SlapCountHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!slap"

        self.params = "count"

        # displayed when !help is called
        self.short_description = "Responds with the number of times you have been slapped."

        # displayed when !help test is called
        self.long_description = "Responds with the number of times you have been slapped."

    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            split = message.content.split(" ", 1)
            if len(split) > 1:
                target = split[1]

            if "counts" not in state:
                state["counts"] = {}

            if len(split) == 1 or target in ["count", "slap count"]:

                if message.author.mention in state["counts"]:
                    msg = "{} has been slapped {} times".format(message.author.mention, state["counts"][message.author.mention])
                    await message.channel.send(msg)
                else:
                    await message.channel.send("People must like you, you haven't been slapped. Yet.")



