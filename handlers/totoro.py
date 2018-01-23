import asyncio
import random
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    def __init__(self):
        self.signal = "!totoro"

        # displayed when !help is called
        self.description = self.signal + " <message> : Draws a totoro."

        # displatyed when !help test is called
        self.help = self.signal + """ <message> : Draws a totoro. """



    async def handle_message(self, client, message):

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
