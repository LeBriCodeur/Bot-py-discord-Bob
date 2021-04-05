import os
from twitchio.ext import commands

class Bot(commands.Bot):
  
    def __init__(self):
        super().__init__(irc_token=os.environ['TOKEN_TWITCH'], client_id=os.environ["CLIENT_ID"], nick='aroun_31', prefix='!',
                         initial_channels=['aroun_31'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Bien le bonjour maitre {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()
