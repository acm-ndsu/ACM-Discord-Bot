import asyncio
import random
import pickle
import re
from handlers.message_handler import HandlerModule, MessageHandler

### Helper Methods

def get_user_karma(state, uuid):
    amt = state["karma"].get(uuid, 0)
    msg = "<@" + uuid + ">: karma is at " + str(amt)
    return msg

def add_user_karma(state, uuid, amount):
    if "karma" not in state: state["karma"] = {}

    if uuid not in state["karma"]:
        state["karma"][uuid] = 0
    state["karma"][uuid] += amount

    msg = "<@" + uuid + ">: karma is now " + str(state["karma"][uuid])
    return msg


## Module Definition

class Module(HandlerModule):
    def __init__(self):
        super().__init__("karma", persist_state=True)

    def init_handlers(self):

        self.handlers.append( GiveTakeKarmaHandler() )
        self.handlers.append( CheckSelfKarmaHandler() )
        self.handlers.append( CheckKarmaHandler() )


class GiveTakeKarmaHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.buzzkill_limit = 5
        self.signal = "!karma"

        self.params = "<User-Mention><Amount>"

        # displayed when !help is called
        self.short_description = "Bestow the given amount of ++/-- from person."

        # displatyed when !help test is called
        self.long_description  = "Bestow the given amount of ++/-- from person."


    async def handle_message(self, client, message, state):
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
                    msg = add_user_karma(state, user, amount)

        if msg is not None:
            await client.send_message(message.channel, msg)


class CheckSelfKarmaHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!karma"

        # displayed when !help is called
        self.short_description = "Check how much karma you have."

        # displatyed when !help test is called
        self.long_description = "Check how much karma you have."


    async def handle_message(self, client, message, state):
        msg = None

        m = re.search(r'<@!?(\d+)>\s*(\+\++|--+)$', message.content, re.DOTALL)
        if m is None:

            args = message.content.split(" ", 1)
            if args[0] == self.signal:

                if len(args) < 2:
                    msg = get_user_karma(state, message.author.id)

        if msg is not None:
            await client.send_message(message.channel, msg)


class CheckKarmaHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!karma"

        # displayed when !help is called
        self.short_description = "<User-Mention> : Show how much karma the given user has."

        self.long_description = "<User-Mention> : Show how much karma the given user has."


    async def handle_message(self, client, message, state):
        msg = None

        m = re.search(r'<@!?(\d+)>\s*(\+\++|--+)$', message.content, re.DOTALL)
        if m is None:

            args = message.content.split(" ", 1)
            if args[0] == self.signal:

                if len(args) > 1:
                    m = re.search(r'<@!?(\d+)>', args[1], re.DOTALL)
                    if m is not None:
                        msg = get_user_karma(state, m.group(1))
        if msg is not None:
            await client.send_message(message.channel, msg)


