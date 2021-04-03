# Bot-py-discord-Bob
 Bob est un bot prévu pour discord on verra plus ce qu'il fera

# lib : discord.py
# # Linux/macOS
# >> python3 -m pip install -U discord.py
# # Windows
# >> py -3 -m pip install -U discord.py
# https://pypi.org/project/discord.py/

#C:\Users\mcfam\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\twitch

- [x] mettre le token en variable d'environnement (look : dotenv )
- [x] encapculer dans une class (N'est pas bon pour la récupération des commands : message.content.startswith('!bob'))
- [ ] créer un pakage
- [x] faire un fichier bat par bot pour les réveiller 
- [x] faire un fichier bat pour réveiller tout les bots
- [ ] relier twitch et discord
- [ ] créer un faux client 


# """
# class MyBot(commands.Bot):
#     def __init__(self):
#         super().__init__(command_prefix=prefix)

#     async def on_ready(self):
#         print("Le bot est prêt.")


# bot = DocBot()
# bot.run("TOKEN")
# """