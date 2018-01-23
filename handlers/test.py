import asyncio
from handlers.message_handler import MessageHandler

class Handler(MessageHandler):
    """
    Calculates and returns how many times the user has sent the "!test" command to the bot.
    """


    async def handle_message(self, client, message):

        if message.content.startswith('!test'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            await client.send_message(message.channel, 'Done sleeping')

            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))
