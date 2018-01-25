import asyncio
import random
import pickle
from handlers.message_handler import MessageHandler

count_filename = "hug_counts.pkl"

class Handler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!hug"

        # displayed when !help is called
        self.description = self.signal + " <target> : hugs target.\n"
        self.description += self.signal + " count : Responds with the number of times you have been hugped."

        # displayed when !help test is called
        self.help = self.signal + """ <target> : hugs target."""
        self.help += self.signal + """ count : Responds with the number of times you have been hugped."""

        self.counts = {}

        try:
            with open(count_filename, 'rb') as f:
                self.counts = pickle.load(f)
        except FileNotFoundError:
            pass  # that's okay; swallow


    async def handle_message(self, client, message):

        if message.content.startswith(self.signal):
            signal, target = message.content.split(" ")

            if target == "count" or target is None or target == "":
                msg = "{} has been hugped {} times".format(message.author.mention, self.counts[message.author.mention])
                await client.send_message(message.channel, msg)

            else:
                if target not in self.counts:
                    self.counts[target] = 0
                self.counts[target] += 1

                self.save()

                phrase = random.choice([
                    "{} hugs {}.",
                    "{} hugs {}. *There there...*",
                    "{} hugs {}. *It will all be better soon...*",
                    "{} hugs {}. *You'll float too....*",
                ])

                await client.send_message(message.channel, phrase.format(message.author.mention, target))


    def save(self):
        with open(count_filename, 'wb') as f:
            pickle.dump(self.counts, f)

