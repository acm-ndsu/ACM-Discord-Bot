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
                await message.channel.send("Excuse me but there's nothing there.")
            elif len(comparison) < 3:
                await message.channel.send("Compare that and what?")
            elif "anime" in message.content.lower():
                if "trash" in message.content.lower():
                    await message.channel.send("There is no difference.")
                else:
                    await message.channel.send("Easy, one of these things is trash, and the other thing probably is too.")
            elif "robbot" in message.content.lower() and "human" in message.content.lower():
                await message.channel.send("There is no difference.")
            else:
                good = False
                while (not good):
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Ok, so")
                    else:
                        await message.channel.send("Well")
                    
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Um")
                    else:
                        await message.channel.send("Uh")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("The first thing")
                    else:
                        await message.channel.send("The first is")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Ah")
                    else:
                        await message.channel.send("Hm")
                        
                    await asyncio.sleep(random.random() * 2)
                        
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Well its an object idea thing")
                    else:
                        await message.channel.send("Its an idea or object, thing")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("That")
                    else:
                        await message.channel.send("That uh")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Exists")
                    else:
                        await message.channel.send("Does things")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    await message.channel.send("Maybe")
                    
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Where as the second")
                    else:
                        await message.channel.send("But the second")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Eh")
                    else:
                        await message.channel.send("Er")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("May or may not do that too")
                    else:
                        await message.channel.send("Doesn't, or, does")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Or something like that")
                    else:
                        await message.channel.send("Or the complete opposite")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    await message.channel.send("Maybe")
                        
                    await asyncio.sleep(random.random() * 2)
                    
                    #Checks for a repeat
                    if (bool(random.getrandbits(1))):
                        await message.channel.send("Wait")
                        await asyncio.sleep(random.random() * 2)
                        if (bool(random.getrandbits(1))):
                            await message.channel.send("Yeah I got that completely wrong, let me try again")
                        else:
                            good = True
                            await message.channel.send("No")
                            await asyncio.sleep(random.random() * 2)
                            await message.channel.send("Yeah, that's right")
                    else:
                        await message.channel.send("Yeah")
                        good = True
                
                await asyncio.sleep(random.random() * 2)
                await message.channel.send("Hope that helped.")
                