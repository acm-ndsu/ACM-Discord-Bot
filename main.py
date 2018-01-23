import importlib
import json
import asyncio

import discord

client = discord.Client()

message_handlers = []

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
            output = ""
            for handler in message_handlers:
                output += handler.description + "\n"

            await client.send_message(message.channel, output)

        else:
            content = content.split()
            signal = "!" + content[0]

            for handler in message_handlers:
                if handler.signal == signal:
                    await client.send_message(message.channel, content.help)
                    break



    for handler in message_handlers:
        await handler.handle_message(client, message)


    if message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

if __name__ == "__main__":

    with open("config.json", "r") as f:
        config = json.load(f)

    print("Loading Modules...")
    for module_name in config["handlers"]:
        module = importlib.import_module("handlers." + module_name)
        message_handlers.append(module.Handler())
    print("Modules loaded.")

    with open("token.txt", "r") as f:
        token = f.read().replace("\n", "")

    client.run(token)
