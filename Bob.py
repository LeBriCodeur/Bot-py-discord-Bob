import os
import discord
import Twipy
from discord import Embed
from dotenv import load_dotenv
from discord.ext import commands


# Author : Aroun Le BriCodeur
# create 01/04/21 | 0.1

#Pour whitelist une commande par rôle : @commands.has_any_role("🔐 PATRON")
# pour ajouter des rôles : ("🔐 PATRON", "pdg", "branleur")
load_dotenv() # dotenv_path=".env"

# info twitch
account_name = "Aroun31"
channel_name = "Aroun31"
token_twitch = os.getenv("TOKEN_TWITCH")
client_id = os.getenv("CLIENT_ID")

# info discord
token_discord = os.getenv("TOKEN_DISCORD")
# préfixe utilisé par le bot
prefix = "!" 
bot = commands.Bot(command_prefix=prefix, description="Description !")


# Ready
@bot.event
async def on_ready():
    print("Waaahh ça fait du bien de dormir.\nBob au rapport !")
    print("préfix utilisé : ", prefix)


# /!\ intercepte les messages mais coup rend les commands inutilisable :/ . /!\
# @bot.event
# async def on_message(message):
#     # print(message)
#     print(f"\nNouveau message sur \"{message.guild.name}\" dans \"{message.channel.name}\" de \"{message.author.name}\"\nMessage : {message.content}")


#Error event evite de crache le bot ^^
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Comment dire...\nIl manque des info pour que ça fonctionne...\nQu'il est con celui là\n :rolling_eyes:.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Quelque chose me dit que...\nTu n'es pas autorisé à utiliser cette commande :angry:")

# commande qui dis de la merde et redirige le membre vers la commande cmd
@bot.command(name="bob")
async def bob(a_ctx):
    message = f"Salut je suis Bob le bot.\n"\
    +"Mon créateur est une âme généreuse et on le nomme :"\
    +"\nLe BriCodeur.\n"\
    +"C'est grâce à lui que je peux dire plein de conneries et ça me ravi chaque jour qui passe.\n"\
    +f"Sinon {a_ctx.author.name} tu peux utiliser :\n"\
    +f"{prefix}cmd pour connaître les commandes"
    await a_ctx.send(message)

# liste des commandes
@bot.command()
async def cmd(a_ctx):
    print(f"\n{a_ctx.author.name} à fait appel à !cmd sur {a_ctx.guild.name}")
    cmd_all = ["bob", "infoserv", "soutien"]
    cmd_admin = ["ban", "kick", "del_msg value (default : 1)", "cchan \"help\""]
    message = "Les différentes commandes sont :\n"
    for i in cmd_all:
        message += f"{prefix}{i}\n"
    message += "ADMIN Commande : \n"
    for i in cmd_admin:
        message += f"{prefix}{i}\n"
    await a_ctx.send(message)

# retourne les infos du serveur si envie (c'est à finir faut composer le message)
@bot.command(name="infoserv")
async def servInfo(a_ctx):
    server = a_ctx.guild
    serverName = server.name # Nom du serveur
    serverDesc = server.description # Description du serveur : /!\ Normal si c'est None ou Null /!\
    nrbTxtChan = len(server.text_channels) # Nombre de canal texte du serveur 
    nrbVocChan = len(server.voice_channels) # Nombre de canal vocaux du serveur 
    nrbMembers = server.member_count # Nombre de membres du serveur
    if serverDesc is None: serverDesc = "Pas de description"
    await a_ctx.send(f"Infos du serveur : \nnom du serveur : {serverName},\ndescription : {serverDesc},\nNrb chan texte : {nrbTxtChan},\n"\
    +f"Nrb chan vocaux : {nrbVocChan},\nNrb membres : {nrbMembers}")

#soutenir le projet
@bot.command(name="soutien")
async def soutien(a_ctx):
    url_paypal = "https://www.paypal.com/paypalme/arounMcf"
    await a_ctx.send(f"Tu peux soutenir le bot ici :\n{url_paypal}\nCela permet de montrer de l'intéret en vers le bot et de faire manger le dev ( moi :) )")


        # # # # # # # # # # # # # # #
# # # # # Commands whitelist admins # # # # #
        # # # # # # # # # # # # # # #

# Création de catégories & canaux
@bot.command(name="cchan")
@commands.has_permissions(administrator=True)
async def newchan(a_ctx, a_type, *a_nameChan):
    server = a_ctx.guild
    print(f"\n{a_ctx.guild.name} | {a_ctx.message.author} :: {a_type} :: {a_nameChan}")
    for i in a_nameChan:
        print(i)
    if a_type == "chan":
        for i in a_nameChan:
            await server.create_text_channel(i)
            print(f"Channel text create : '{i}'  by : {a_ctx.message.author} in {a_ctx.guild.name}")
    elif a_type == "cat":
        for i in a_nameChan:
            await server.create_category(i)
            print(f"Category create : '{i}'  by : {a_ctx.message.author} in {a_ctx.guild.name}")
    elif a_type == "help":
        print("help calling")
        await a_ctx.channel.send("Créer une catégorie :\n```!cchan \"cat\" \"name category 1\" \"name category 2\" etc...```\n"\
        +"Créer un channel (text) :\n```!cchan \"chan\" \"name-channel-1\" \"name-channel-2\" etc...```")


# Delete message
@bot.command(name="del_msg")
@commands.has_permissions(administrator=True)
async def delete_msg(a_ctx, number: int = 1):
    messages = await a_ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()
    print(f"{a_ctx.guild.name} | {a_ctx.message.author} :: Nettoyage de {number} message(s) ")

# Ban
@bot.command()
# Permet le whitelist de la commande pour les admins
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.User=None, reason=None):
    admin_name = ctx.message.author
    # message dans le canal
    msg_chan = f"{member} a été ban par {admin_name} pour la raison suivante : {reason}"
    # message envoyé en mp à la personne mentionné donc le banni
    msg_mp = f"Tu as été ban de : {ctx.guild.name} pour la raison suivante : {reason}. par {admin_name}"
    print(f"\n{msg_chan} sur ctx.guild.name")
    # Vérification pour pas se ban soit même ou si personne est mentionné
    if member is None or member == ctx.message.author:
        if member == ctx.message.author:
            await ctx.channel.send("Tu veux vraiment te ban toi même ?? :face_with_monocle: ")
        else:
            await ctx.channel.send("Quand on veut ban une personne c'est pas mieux de le nommer ?? :laughing: ")
        return
    if reason is None:
        reason = "Inconnu"
    # message envoyé en mp à l'utilisateur
    await member.send(msg_mp)
    # message envoyé dans le canal ou il a été ban
    await ctx.channel.send(msg_chan)
    # écrit le même message en console
    print(msg_chan)
    # et enfin ban du membre
    await member.ban(reason=reason)

# Kick
@bot.command()
# Permet le whitelist de la commande pour les admins
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.User=None, reason=None):
    admin_name = ctx.message.author
    # message dans le canal
    msg_chan = f"{member} a été kick par {admin_name} pour la raison suivante : {reason}"
    # message envoyé en mp à la personne mentionné donc le kické
    msg_mp = f"Tu as été kick de : {ctx.guild.name} pour la raison suivante : {reason}. par {admin_name}"
    print(f"\n{msg_chan} sur ctx.guild.name")
    # Vérification pour pas se kick soit même ou si personne est mentionné
    if member is None or member == ctx.message.author:
        if member == ctx.message.author:
            await ctx.channel.send("Tu veux vraiment te Kick toi même ?? :face_with_monocle: ")
        else:
            await ctx.channel.send("Quand on veut kick une personne c'est pas mieux de le nommer ?? :laughing: ")
        return
    if reason is None:
        reason = "Inconnu"
    # message envoyé en mp à l'utilisateur
    await member.send(msg_mp)
    # message envoyé dans le canal ou il a été kick
    await ctx.channel.send(msg_chan)
    # écrit le même message en console
    print(msg_chan)
    # et enfin kick du membre
    await member.kick(reason=reason)



bot.run(token_discord)
# tw = Twipy.Twipy()
# tw.run()

