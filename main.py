import discord
from discord.ext import commands
from discord import Embed


#Pour whitelist une commande par rôle : @commands.has_any_role("🔐 PATRON")
# pour ajouter des rôles : ("🔐 PATRON", "pdg", "branleur")
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description="coucou")
token = "TOKEN-DU-BOT"

#Ready
@bot.event
async def on_ready():
    print("Je prends vie !!!!")


#Error event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Comment dire... Il manque des info pour que ça fonctionne... qu'il est con celui là :rolling_eyes:.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Quelque chose me dit que tu n'es pas autorisé à utiliser cette commande :angry:")


# commande qui dis de la merde et redirige le membre vers la commande help
@bot.command()
async def bob(a_ctx):
    message = f"Salut je suis Bob le bot.\nJe suis fait pour le serveur de :\nMartin62#4778 et AlexLiveFrr#0050\ndédié à ETS2 !\nMon créateur est une âme généreuse et on le nomme :\
    \n'Le BriCodeur'.\nC'est grâce à lui que je peux dire plein de conneries et ça me ravi chaque jour qui passe.\nSinon {a_ctx.author.name} tu peux utiliser {prefix}cmd pour les commandes"
    await a_ctx.send(message)


# liste des commandes
@bot.command()
async def cmd(a_ctx):
    await a_ctx.send(f"Les différentes commandes sont : \n{prefix}bob\n")

# retourne les infos du serveur si envie (c'est à finir faut composer le message)
@bot.command()
async def serverInfo(a_ctx):
    server = a_ctx.guild
    serverName = server.server_name # Nom du serveur
    serverDesc = server.description # Description du serveur : /!\ Normal si c'est None ou Null /!\
    nrbTxtChan = len(server.text_channels) # Nombre de canal texte du serveur 
    nrbVocChan = len(server.voice_channels) # Nombre de canal vocaux du serveur 
    nrbMembers = server.member_count # Nombre de membres du serveur 
    await a_ctx.send(f"bla bla bla toutes les infos du serveur : {serverName} {serverDesc} {nrbTxtChan} {nrbVocChan} {nrbMembers} ")


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


bot.run(token)


