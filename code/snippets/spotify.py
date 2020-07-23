# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from config import spotifytokens
#
# scope = "user-modify-playback-state"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=spotifytokens['client_id'],
#     client_secret=spotifytokens['client_secret'],
#     redirect_uri='localhost',
#     scope=scope
# ))
#
# sp.start_playback(context_uri='spotify:track:5rqQTEIVK2PTuXU9GI2wT0')
#
import sys
import spotipy
import spotipy.util as util
from config import spotifytokens

scope = 'user-library-read user-modify-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(
    username,
    scope,
    client_id=spotifytokens['client_id'],
    client_secret=spotifytokens['client_secret'],
    redirect_uri='https://www.example.com'
)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.start_playback(uris=['spotify:track:5rqQTEIVK2PTuXU9GI2wT0'])
else:
    print("Can't get token for", username)
