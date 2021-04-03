import os
from dotenv import load_dotenv
# Twitch API
import twitch

load_dotenv() # dotenv_path=".env"

# info twitch
account_name = "aroun31"
channel_name = "aroun31"
token_twitch = os.getenv("TOKEN_TWITCH") # oauth:
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = 91452241
user_id_str = "91452241"

# helix = twitch.Helix(client_id, client_secret, False, None, False, token_twitch)
helix = twitch.Helix(client_id, client_secret)
print("joe : ", helix)


for user in helix.users([user_id]):
    print(user.display_name)


# for video in helix.videos([user_id]):
#     print(video.title)


# for comment in helix.video(user_id).comments:
#     print(comment.commenter.display_name)


twitch.Chat(channel=channel_name, nickname=channel_name, oauth='oauth:'+token_twitch).subscribe(
        lambda message: print(message.channel, message.user.display_name, message.text))