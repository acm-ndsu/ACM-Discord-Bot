import random
from handlers.message_handler import HandlerModule, MessageHandler


class Module(HandlerModule):
    def __init__(self):
        super().__init__("opinion", persist_state=False)

    def init_handlers(self):

        self.handlers.append(OpinionHandler())


class OpinionHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!opinion"

        self.params = "<language>"

        # displayed when !help is called
        self.short_description = "programming language opinions."

        # displayed when !help test is called
        self.long_description = "Randomly generates an opinion about a programming language."

    async def handle_message(self, client, message, state):

        if message.content.lower().startswith(self.signal):

            adjective = random.choice([
                "",
                "",
                "",
                "bold ",
                "brutally honest ",
                "controversial ",
                "honest ",
                "humble ",
                "insightful ",
                "off-color ",
                "off-the-record ",
                "perceptive ",
                "true ",
                "undebatable "
            ])

            opening_remarks = random.choice([
                "",
                "I believe ",
                "I think ",
                "I would say "

            ])

            language_options = [
                "Ada",
                "ALGOL 68",
                "Basic",
                "C",
                "C#",
                "C++",
                "COBOL",
                "CSS",
                "F#",
                "Fortran",
                "Go",
                "Haskell",
                "HTML",
                "Java",
                "Javascript",
                "Kotlin",
                "LambdaMOO",
                "Lisp",
                "Matlab",
                "Objective-C",
                "Pascal",
                "Perl",
                "PHP",
                "Prolog",
                "Python",
                "R",
                "Ruby",
                "Rust",
                "Scratch",
                "Shakespeare",
                "Shell",
                "SQL",
                "Swift",
                "Typescript",
                "Visual Basic"
            ]

            split = message.content.split(" ")

            if len(split) > 1 and split[1].strip().lower() in [lang.lower() for lang in language_options]:
                language = split[1].strip()
            else:
                language = random.choice(language_options)

            opinion = random.choice([
                "could use some more work.",
                "is a gift to mankind!",
                "is a good language.",
                "is a great language.",
                "is actually pretty good.",
                "is decent.",
                "is my favorite programming language.",
                "is the worst language created.",
                "is wonderful!",
                "has more cons than pros.",
                "has more pros than cons.",
                "needs improvements.",
                "should be banned from GitHub.",
                "shouldn't be considered a language."
            ])

            closing_remarks = random.choice([
                "",
                "",
                "",
                "Any arguments?",
                "But hey, that's just my opinion. A robbot opinion.",
                "But that's what everybody says.",
                "Do you agree?",
                "I hope you would say the same!",
                "I know it's not that popular of an opinion.",
                "I know others tend to agree.",
                "I think.",
                "Maybe I'm wrong.",
                "Thoughts?",
                "What do you think?"
            ])

            my_opinion = "In my " + adjective + "opinion, " + \
                         opening_remarks + language + " " + opinion + " " + closing_remarks

            await message.channel.send(my_opinion)
