import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("aoe")


    def init_handlers(self):

        self.handlers.append( aoeHandler() )


class aoeHandler(MessageHandler):
    def __init__(self):
        self.signal = "!aoe"

        # params to dispay in help meesages
        self.params = "[AoEVersion] <TauntNumber>"

        # displayed when !help is called
        self.short_description = " Age of Empires taunter"

        # displatyed when !help aoe is called
        self.long_description = " Uses optional AoE version (1-3 + M, default: 2) and taunt number to generate taunts"


    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):
            # Had to move this here because scoping problems and I'm tired of being proper
            AoE1 = {
            1: "Yes.",
            2: "No.",
            3: "I need food.",
            4: "Somebody pass the wood.",
            5: "Gold please.",
            6: "Gimme some stone.",
            7: "*Whimper*",
            8: "Your attempts are futile.",
            9: "*Group cheer*",
            10: "Hey, I'm in your town.",
            11: "*Group groan*",
            12: "Join me!",
            13: "I don't think so.",
            14: "Start the game already!",
            15: "Who's the man?",
            16: "Attack them now!",
            17: "*Low laugh*",
            18: "I am weak, please don't kill me!",
            19: "*High pitched laugh*",
            20: "I just got some... satisfaction!",
            21: "Hey, nice town!",
            22: "We will NOT tolerate this behavior.",
            23: "Get out!",
            24: "Dad gum!",
            25: "Aw, yeah!"
            }
            
            AoE2 = {
            1: "Yes.",
            2: "No.",
            3: "Food please.",
            4: "Wood please.",
            5: "Gold please.",
            6: "Stone please.",
            7: "Ahh!",
            8: "All hail, king of the losers!",
            9: "Ooh!",
            10: "I'll beat you back to Age of Empires.",
            11: "(Herb laugh)",
            12: "Ah! Being rushed.",
            13: "Sure, blame it on your ISP.",
            14: "Start the game already!",
            15: "Don't point that thing at me!",
            16: "Enemy sighted",
            17: "It is good to be the king.",
            18: "Monk! I need a monk!",
            19: "Long time, no siege.",
            20: "My granny could scrap better than that.",
            21: "Nice town, I'll take it.",
            22: "Quit touching me!",
            23: "Raiding party!",
            24: "Dadgum.",
            25: "Eh, smite me.",
            26: "The wonder, the wonder, the... no!",
            27: "You played two hours to die like this?",
            28: "Yeah, well, you should see the other guy.",
            29: "Roggan.",
            30: "Wololo.",
            31: "Attack an enemy now.",
            32: "Cease creating extra villagers.",
            33: "Create extra villagers.",
            34: "Build a navy.",
            35: "Stop building a navy.",
            36: "Wait for my signal to attack.",
            37: "Build a wonder.",
            38: "Give me your extra resources.",
            39: "(Ally sound)",
            40: "(Enemy sound)",
            41: "(Neutral sound)",
            42: "What age are you in?"
            }
            
            AoM = {
            1: "Yes.",
            2: "No.",
            3: "Food please.",
            4: "Wood please.",
            5: "Gold please.",
            6: "Do you have extra resources?",
            7: "Aww",
            8: "Meet here",
            9: "Oooh",
            10: "Are you ready?",
            11: "(Laugh)",
            12: "I need help",
            13: "Sure, blame it on your firewall.",
            14: "Start the game already",
            15: "Attack now",
            16: "Build a wonder",
            17: "I have extra wood",
            18: "I have extra food",
            19: "I have extra gold",
            20: "You're my hero",
            21: "I'm scouting",
            22: "Whatever",
            23: "Oh, you let a girl beat you",
            24: "Are we there yet?",
            25: "Voted off",
            26: "Ouch, that had to hurt",
            27: "What happened to the stone?",
            28: "Throw things at me",
            29: "(Scream)",
            30: "Wololo.",
            31: "You're very brave",
            32: "Turn back now",
            33: "I feel less fighting",
            34: "Give up now",
            35: "Coward",
            36: "Did I mention that I am a god now?",
            37: "Not a wise decision but a decision nonetheless",
            38: "What do I gotta do to get some food around here",
            39: "I need some back-up",
            40: "Fire in the hole",
            41: "What a baby",
            42: "I wish he would stop doing that",
            43: "Ahh what a foolish decision",
            44: "Ahh you are such a fool"
            }
            
            AoE3 = {
            1: "Yes.",
            2: "No.",
            3: "I need food.",
            4: "I need wood.",
            5: "I need coin.",
            6: "Do you have extra resources.",
            7: "I have extra food.",
            8: "I have extra wood.",
            9: "I have extra coin.",
            10: "Meet here.",
            11: "Are you ready.",
            12: "I need help.",
            13: "Attack now.",
            14: "Upgrade your trade route.",
            15: "Wololo.",
            16: "I'm in your base, killing your dudes.",
            17: "Check in your wallet. That's me on the dollar bill.",
            18: "I believe that makes me your daddy.",
            19: "El-Oh-El, I am R-Oh-Tee-Eff-El. (Laugh out Loud, I am Rolling on the Floor Laughing.)",
            20: "Aren't you becoming quite the little problem.",
            21: "(Laughter)",
            22: "This will give me cred, street cred.",
            23: "Hey, shut your pie hole.",
            24: "I'll take that trade.",
            25: "You sit on the computer all day playing. You know nothing of hard life.",
            26: "Really. Such a noob.",
            27: "Ask not for whom the timer ticks. It ticks for thee.",
            28: "(Alternate laughter)",
            29: "Check in your pocket. The quarter is me, too.",
            30: "Where is my mother.",
            31: "(Charge bugle call)",
            32: "Believe it, little boy.",
            33: "Zing."
            }
            
            versions = {0: AoM, 1: AoE1, 2: AoE2, 3: AoE3}
            
            send = None
            parts = message.content.split(" ")
            
            for part in parts:
                part.strip()
            
            if len(parts) > 2: # There SHOULD exist at least "!AoE ver num"
                try:
                    vers = int(parts[1])
                    num = int(parts[2])
                except ValueError:
                    if parts[1].lower() == "m":
                        vers = 0
                        try: num = int(parts[2])
                        except ValueError: num = random.randint(1, 44)
                    else:
                        try:
                            num = int(parts[1])
                            vers = 2
                        except ValueError: 
                            vers = random.randint(0, 3)
                            if vers == 0: num = random.randint(1, 44)
                            elif vers == 1: num = random.randint(1, 25)
                            elif vers == 2: num = random.randint(1, 42)
                            else: num = random.randint(1, 33)
            elif len(parts) > 1: # There SHOULD exist "!AoE num"
                try:
                    vers = 2
                    num = int(parts[1])
                except ValueError:
                    vers = random.randint(0, 3)
                    if vers == 0: num = random.randint(1, 44)
                    elif vers == 1: num = random.randint(1, 25)
                    elif vers == 2: num = random.randint(1, 42)
                    else: num = random.randint(1, 33)
            else:
                vers = random.randint(0, 3)
                if vers == 0: num = random.randint(1, 44)
                elif vers == 1: num = random.randint(1, 25)
                elif vers == 2: num = random.randint(1, 42)
                else: num = random.randint(1, 33)
            
            
            try: 
                send = versions[vers][num]
            except KeyError:
                '''vers = random.randint(0, 3)
                if vers == 0: num = random.randint(1, 44)
                elif vers == 1: num = random.randint(1, 25)
                elif vers == 2: num = random.randint(1, 42)
                else: num = random.randint(1, 33)
                send = versions[vers][num]'''
                send = "I am sorry, that does not exist."
            await client.send_message(message.channel, send)