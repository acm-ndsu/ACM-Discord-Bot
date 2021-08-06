from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("mock")


    def init_handlers(self):
        self.handlers.append( MockHandler() )


class MockHandler(MessageHandler):
    def __init__(self):
        self.signal = "!mock"

        # params to dispay in help meesages
        self.params = "<text>"

        # displayed when !help is called
        self.short_description = " Returns the sentence in mock-case "

        # displatyed when !help caltrops is called
        self.long_description = " Inspired by SpongeBob mock text, which turns sentence into alternating upper and lower case letters "

    async def handle_message(self, client, message, state):
        if message.content.lower().startswith(self.signal):
            
            msg = message.content.replace(self.signal, "")

            increment = 0
            for i in len(msg):
                if increment % 2 == 0:
                    msg[i] = msg[i].lower()
                else:
                    msg[i] = msg[i].upper()
                increment += 1

            await message.channel.send(msg)

