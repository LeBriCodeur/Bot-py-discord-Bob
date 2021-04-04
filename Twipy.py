import os
from twitchio.ext import commands
from twitchio.client import Client
from dotenv import load_dotenv
bot_name = "Twipy"
load_dotenv()
bot = commands.Bot(
    irc_token=os.getenv("TOKEN_TWITCH"),
    client_id=os.getenv("CLIENT_ID"),
    nick='Aroun31',
    initial_channels=['Aroun31'],
    prefix='!',
)


client = Client(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
)


@bot.event
async def event_ready():
    print(f"{bot_name} au rapport prêt à bosser !")


@bot.event
async def event_message(ctx):
    print(ctx.author)
    print(ctx.content)
    await bot.handle_commands(ctx)




@bot.command(name='sub')
async def issub(ctx):
    p = bot.get_followers('aroun_31', True)
    for i in p:
      print(i)
    # await ctx.send("pong")


@bot.command(name='ping')
async def pyng(ctx):
    await ctx.send("pong")


@bot.command(name='who')
async def get_chatters(ctx):
    chatters = await client.get_chatters('aroun_31')
    all_chatters = ' '.join(chatters.all)
    await ctx.send(f"Présent dans le chat : {all_chatters}")


if __name__ == '__main__':
    bot.run()
    print("Je commençais à m'endormir !")

