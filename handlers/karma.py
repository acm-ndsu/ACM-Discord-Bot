import asyncio
import random
import pickle
import re
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("karma")

    def init_handlers(self):

        self.handlers.append( GiveKarmaHandler() )


class GiveKarmaHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.buzzkill_limit = 5
        self.signal = "!karma"
        self.karma = {}

        # displayed when !help is called
        self.short_description = "Karma system."

        # displatyed when !help test is called
        self.help = self.signal + " : Check how much karma you have."
        self.help += self.signal + " <User-Mention><Amount> : Bestow the given amount of ++/-- from person."
        self.help += "\n" + self.signal + " <User-Mention> : Show how much karma the given user has."


    async def handle_message(self, client, message):
        msg = None
        m = re.search(r'<@!?(\d+)>\s*(\+\++|--+)$', message.content, re.DOTALL)
        if m is not None:
            user = m.group(1)
            amount_str = m.group(2)
            amount = len(amount_str) - 1
            if amount_str.startswith('-'):
                amount *= -1
            if amount is not None:
                if user == message.author.id:
                    msg = "You cannot set karma on yourself!"
                elif abs(amount) > self.buzzkill_limit > 0:
                    msg = "Buzzkill mode enabled;"
                    msg += " karma change greater than " + str(self.buzzkill_limit) + " not allowed"
                else:
                    msg = self.add_user_karma(user, amount)
        else:
            args = message.content.split(" ", 1)
            if args[0] == self.signal:
                if len(args) < 2:
                    msg = self.get_user_karma(message.author.id)
                else:
                    m = re.search(r'<@!?(\d+)>', args[1], re.DOTALL)
                    if m is not None:
                        msg = self.get_user_karma(m.group(1))
        if msg is not None:
            await client.send_message(message.channel, msg)

    def get_user_karma(self, uuid):
        amt = self.karma.get(uuid, 0)
        msg = "<@" + uuid + ">: karma is at " + str(amt)
        return msg

    def add_user_karma(self, uuid, amount):
        if uuid not in self.karma:
            self.karma[uuid] = 0
        self.karma[uuid] += amount
        msg = "<@" + uuid + ">: karma is now " + str(self.karma[uuid])
        try:
            self.save()
        except:
            msg += "\n(WARN): could not save karma file. Admin should investigate"
        return msg

