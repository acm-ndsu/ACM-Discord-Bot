import asyncio
import random
import pickle
from handlers.message_handler import MessageHandler
import re

_karma_filename = 'karma.pkl'

class Handler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.buzzkill_limit = 5
        self.signal = "!karma"
        self.karma = {}

        try:
            with open(_karma_filename, 'rb') as karma_file:
                karma_state = pickle.load(karma_file)
                self.buzzkill_limit = karma_state['buzzkill']
                self.karma = karma_state['karma']
        except FileNotFoundError:
            pass  # that's okay; swallow

        # displayed when !help is called
        self.description = self.signal + ": Karma system."""

        # displatyed when !help test is called
        self.help = self.signal + " : Check how much karma you have."
        self.help += self.signal + " <User-Mention><Amount> : Bestow the given amount of ++/-- from person."
        self.help += "\n" + self.signal + " <User-Mention> : Show how much karma the given user has."


    async def handle_message(self, client, message):
        msg = None
        m = re.search(r'(<@\d+>)(\+\++|--+)$', message.content, re.DOTALL)
        if m is not None:
            user = m.group(1)
            amount_str = m.group(2)
            amount = len(amount_str) - 1
            if amount_str.startswith('-'):
                amount *= -1
            if amount is not None:
                if abs(amount) > self.buzzkill_limit > 0:
                    msg = "Buzzkill mode enabled;"
                    msg += " karma change greater than " + str(self.buzzkill_limit) + "not allowed"
                else:
                    msg = self.add_user_karma(user, amount)
        else:
            args = message.content.split(" ", 1)
            if args[0] == self.signal:
                msg = ""
                if len(args) < 2:
                    msg = self.get_user_karma(message.author.mention)
                else:
                    user = args[1]
                    msg = self.get_user_karma(user)
        if msg is not None:
            await client.send_message(message.channel, msg)

    def get_user_karma(self, mention_str):
        amt = self.karma.get(mention_str, 0)
        msg = mention_str + ": karma is at " + str(amt)
        return msg

    def add_user_karma(self, mention_str, amount):
        if mention_str not in self.karma:
            self.karma[mention_str] = 0
        self.karma[mention_str] += amount
        msg = mention_str + ": karma is now " + str(self.karma[mention_str])
        try:
            self.save()
        except:
            msg += "\n(WARN): could not save karma file. Admin should investigate"
        return msg

    def save(self):
        data = {'buzzkill': self.buzzkill_limit, 'karma': self.karma}
        with open(_karma_filename, 'wb') as karma_file:
            pickle.dump(data, karma_file)
