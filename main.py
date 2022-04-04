import importlib
import json
import asyncio

import discord

client = discord.Client()

modules = []

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    # Handle help command
    if message.content.startswith("!help"):

        content = message.content.replace("!help", "").strip()

        if len(content) == 0:
            output = "```\n"
            for module in modules:
                output += module.handle_help()
            output += "```"

            await message.channel.send(output)

        else:
            content = content.split()
            signal = content[0]

            output = ""

            for module in modules:
                output += module.handle_help(command_name=signal)

            await message.channel.send(output)
    else:

        for module in modules:
            await module.handle_message(client, message)


        if message.content.startswith('!sleep'):
            await asyncio.sleep(5)
            await message.channel.send("Done sleeping")


if __name__ == "__main__":

    with open("config.json", "r") as f:
        config = json.load(f)

    print("Loading Modules...")
    for module_name in config["handlers"]:
        try:
            module = importlib.import_module("handlers." + module_name)
            modules.append(module.Module())
        except:
            print("Failed to load module: " + module_name)
    print("Modules loaded.")

    print("Initializing Modules...")
    for module in modules:
        try:
            module.init_handlers()
        except:
            print("Failed to initialize module: " + str(module))
    print("Modules initialized.")


    with open("token.txt", "r") as f:
        token = f.read().replace("\n", "")

    client.run(token)
