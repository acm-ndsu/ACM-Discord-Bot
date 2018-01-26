import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("roll", persist_state=True)

    def init_handlers(self):

        self.handlers.append( RollHandler() )

class RollHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!roll"

        self.params = "<X>d<Y>"

        # displayed when !help is called
        self.short_description = "Rolls a Y-sided die X times."

        # displatyed when !help test is called
        self.long_description = "Rolls a Y-sided die X times."


    async def handle_message(self, client, message, state):
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
            if sides > 100:
                msg = "Sides > 100 not supported."
            elif sides < 2:
                msg = "There is no such thing as a one-sided die."
            elif count > 100:
                msg = "More than 100 dice per roll not supported. Are you running Shadowrun or something?"
            elif count < 1:
                msg = "Okay, I will roll " + str(count) + " dice. That is less than 1. You fail the roll. Rocks fall,"
                msg += " everyone dies. The end."
            else:
                rolls = ""
                total = 0
                for x in range(count):
                    r = random.randint(1, sides)
                    rolls += str(r) + ", "
                    total += r
                msg = message.author.mention + " rolled {0:d}d{1:d}..."
                msg += "\n{2:s}\nTotal: {3:d}"
                msg = msg.format(count, sides, rolls, total)
            await client.send_message(message.channel, msg)
