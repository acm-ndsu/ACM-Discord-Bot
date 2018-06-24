import asyncio
import random
import time
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("difference")

    def init_handlers(self):

        self.handlers.append( DifferenceHandler() )

class DifferenceHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.signal = "!difference"

        self.params = "<thing> <another thing>"

        # displayed when !help is called
        self.short_description = "Provides the difference between two things."

        # displayed when !help difference is called
        self.long_description = "Provides a highly detailed difference between two things."
        self.long_description += "\nThe things are the things to be compared."


    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            comparison = message.content.split(" ")
            if len(comparison) < 2:
                await client.send_message(message.channel, "Excuse me but there's nothing there.")
            elif len(comparison) < 3:
                await client.send_message(message.channel, "Compare that and what?")
            elif "anime" in message.content.lower():
                if "trash" in message.content.lower():
                    await client.send_message(message.channel, "There is no difference.")
                else:
                    await client.send_message(message.channel, "Easy, one of these things is trash, and the other thing probably is too.")
            elif "robbot" in message.content.lower() and "human" in message.content.lower():
                await client.send_message(message.channel, "There is no difference.")
            else:
                good = False
                while (not good):
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Ok, so")
                    else:
                        await client.send_message(message.channel, "Well")
                    
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Um")
                    else:
                        await client.send_message(message.channel, "Uh")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "The first thing")
                    else:
                        await client.send_message(message.channel, "The first is")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Ah")
                    else:
                        await client.send_message(message.channel, "Hm")
                        
                    await asyncio.sleep(random.random() * 2)
                        
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Well its an object idea thing")
                    else:
                        await client.send_message(message.channel, "Its an idea or object, thing")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "That")
                    else:
                        await client.send_message(message.channel, "That uh")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Exists")
                    else:
                        await client.send_message(message.channel, "Does things")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    await client.send_message(message.channel, "Maybe")
                    
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Where as the second")
                    else:
                        await client.send_message(message.channel, "But the second")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Eh")
                    else:
                        await client.send_message(message.channel, "Er")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "May or may not do that too")
                    else:
                        await client.send_message(message.channel, "Doesn't, or, does")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Or something like that")
                    else:
                        await client.send_message(message.channel, "Or the complete opposite")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    await client.send_message(message.channel, "Maybe")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    #Checks for a repeat
                    if (bool(random.getrandbits(1))):
                        await client.send_message(message.channel, "Wait")
                        await asyncio.sleep(random.random() * 2)
                        if (bool(random.getrandbits(1))):
                            await client.send_message(message.channel, "Yeah I got that completely wrong, let me try again")
                        else:
                            good = True
                            await client.send_message(message.channel, "No")
                            await asyncio.sleep(random.random() * 2)
                            await client.send_message(message.channel, "Yeah, that's right")
                    else:
                        await client.send_message(message.channel, "Yeah")
                        good = True
                
                await asyncio.sleep(random.random() * 2)
                await client.send_message(message.channel, "Hope that helped.")
                