import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("hug", persist_state=False)

    def init_handlers(self):

        self.handlers.append( TotoroHandler() )

class TotoroHandler(MessageHandler):
    def __init__(self):
        super().__init__()

        self.signal = "!totoro"

        # displayed when !help is called
        self.short_description = "Draws a totoro."

        # displatyed when !help test is called
        self.long_description = "Draws a totoro."



    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            msg = """ ```
  _____
 /     \\
 vvvvvvv  /|__/|
    I   /O,O   |
    I /_____   |      /|/|
   J|/^ ^ ^ \  |    /00  |    _//|
    |^ ^ ^ ^ |W|   |/^^\ |   /oo |
     \m___m__|_|    \m_m_|   \mm_|

            ```
            """

            await client.send_message(message.channel, msg)
