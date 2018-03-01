import pickle
import re
import copy

class HandlerModule:

    def __init__(self, module_name, persist_state=False):
        self.handlers = []
        self.module_name = module_name
        self.persist_state = persist_state

        if self.persist_state:
            clean_module_name = re.sub(r'\W+', '', self.module_name)
            self.pickle_file = clean_module_name + ".pkl"
            try:
                with open(self.pickle_file, 'rb') as f:
                    self.shared_state = pickle.load(f)
            except FileNotFoundError:
                self.shared_state = {}
        else:
            self.shared_state = {}

        self.shared_state_cache = copy.deepcopy(self.shared_state)


    async def handle_message(self, client, message):
        for handler in self.handlers:
            await handler.handle_message(client, message, self.shared_state)

        # if shared stared changed and persist_state is true,
        # then persist the changes and update the comparison cache
        if self.persist_state and self.shared_state != self.shared_state_cache:
            self.shared_state_cache = copy.deepcopy(self.shared_state)
            self.save()

    def save(self):
        with open(self.pickle_file, 'wb') as f:
            pickle.dump(self.shared_state, f)

    def handle_help(self, command_name=None):
        output = ""
        for handler in self.handlers:
            output += handler.handle_help(command_name)
        return output

    def init_handlers(self):
        raise Exception("HandlerModule.init_handlers not overwritten")


class MessageHandler:

    def __init__(self):
        self.signal = ""
        self.params = ""
        self.short_description = ""
        self.long_description = ""


    async def handle_message(self, client, message, state):
        raise Exception("MessageHandler.handle_message not overwritten")

    def handle_help(self, command_name=None):

        if command_name is None or command_name.strip() == "":
            output = ""
            output += "{} {}: {}".format(
                    self.signal,
                    self.params,
                    self.short_description)
            return output

        elif command_name == self.signal or command_name == self.signal[1:]:
            output = ""
            output += "{} {}: {}".format(
                    self.signal,
                    self.params,
                    self.long_description)
            return output
        else:
            return ""



