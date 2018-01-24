import asyncio
import random
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!roll"

        # displayed when !help is called
        self.description = self.signal + " <X>d<Y> : Rolls a Y-sided die X times."""

        # displatyed when !help test is called
        self.help = self.signal + """ <X>d<Y> : Rolls a Y-sided die X times."""
        super().__init__()


    async def handle_message(self, client, message):
        args = message.content.split(" ", 1)
        if args[0] == self.signal:
            sides = 6
            count = 1
            if len(args) > 1:
                try:
                    parts = args[1].split('d')
                    count = int(parts[0])
                    sides = int(parts[1])
                except (IndexError, ValueError):
                    client.send_message(message.channel, "Not in XdY format; assuming 1d6")
            rolls = ""
            total = 0
            for x in range(count):
                r = random.randint(1, sides)
                rolls += str(r) + ", "
                total += r

            await client.send_message("Rolling {0:d}d{1:d}...\n{2:s}\nTotal: {3:d}".format(count, sides, rolls, total))
