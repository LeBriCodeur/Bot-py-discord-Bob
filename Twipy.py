import os
from dotenv import load_dotenv
from twitchio.ext import commands
from twitchio.client import Client
bot_name = "Twipy"

load_dotenv()

client = Client(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
)


class Twipy(commands.Bot):
  
    def __init__(self):
        super().__init__(irc_token=os.environ['TOKEN_TWITCH'], client_id=os.environ["CLIENT_ID"], nick='Aroun31', prefix='!',
                         initial_channels=['Aroun31'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Twipy au rapport !')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='who')
    async def get_chatters(self, ctx):
        chatters = await client.get_chatters('aroun31')
        all_chatters = ' '.join(chatters.all)
        await ctx.send(f"Présent dans le chat : {all_chatters}")

    # @commands.command(name='sub')
    # async def issub(self, ctx):
    #     p = await client.get_followers(['aroun31'])
    #     print(p)

    # @commands.command(name='clip')
    # async def clipCreate(self, ctx):
    #     p = await self.create_clip(os.environ['TOKEN_TWITCH'], ["aroun31"])
    #     print(p)

    @commands.command(name='ping')
    async def pyng(self, ctx):
        await ctx.send("pong")


# bot = Twipy()
# bot.run()


# if __name__ == '__main__':
#     Twipy.run()
#     print("Je commençais à m'endormir !")

