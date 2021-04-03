import os
import discord
import twitch as twh
from dotenv import load_dotenv
from discord.ext import commands
from discord import Embed


load_dotenv() # dotenv_path=".env"
token = os.getenv("TOKEN")


class Bob(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=prefix)
    # Ready
    async def on_ready(self):
        print("Waaahh ça fait du bien de dormir.\nBob au rapport !")
        print("préfix utilisé : ", prefix)
    #Error event evite de crache le bot ^^
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Comment dire... Il manque des info pour que ça fonctionne... qu'il est con celui là :rolling_eyes:.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Quelque chose me dit que tu n'es pas autorisé à utiliser cette commande :angry:")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!bob'):
            await message.channel.send('Hello Bob!')

bot = Bob()
bot.run(token)