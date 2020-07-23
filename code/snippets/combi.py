import tweepy
from config import tokens, spotifytokens
import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read user-modify-playback-state'

username='APPs'

token = util.prompt_for_user_token(
    username,
    scope,
    client_id=spotifytokens['client_id'],
    client_secret=spotifytokens['client_secret'],
    redirect_uri='https://www.example.com'
)

auth = tweepy.OAuthHandler(tokens["consumer_key"], tokens["consumer_secret"])

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print("Error! Failed to get request token.")

# Example w/o callback (desktop)
verifier = input("Verifier: ")

# Get access token
auth.get_access_token(verifier)

key = auth.access_token
secret = auth.access_token_secret
auth = tweepy.OAuthHandler(tokens["consumer_key"], tokens["consumer_secret"])
auth.set_access_token(key, secret)
api = tweepy.API(auth)
for i in api.mentions_timeline():
    text = i.text[len(api.me().screen_name) + 2:]
    if text.startswith('redeem'):
        pass


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        wordlist = status.text.split()
        if wordlist[1] == 'redeem':
            print('redeeming')
            if token:
                sp = spotipy.Spotify(auth=token)
                sp.start_playback(uris=['spotify:track:5rqQTEIVK2PTuXU9GI2wT0'])


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=[f'@{api.me().screen_name}'])

if __name__ == '__main__':
    pass