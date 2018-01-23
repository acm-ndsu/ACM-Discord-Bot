
class MessageHandler:

    def __init__(self):
        self.signal = ""
        self.description = ""
        self.help = ""


    def handle_message(self, client, message):
        raise Exception("handle_message not overwritten")


