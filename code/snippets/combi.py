import tweepy
from config import tokens, spotifytokens
import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read user-modify-playback-state'

username = 'APPs'

token = util.prompt_for_user_token(
    username,
    scope,
    client_id=spotifytokens['client_id'],
    client_secret=spotifytokens['client_secret'],
    redirect_uri='https://www.example.com'
)
sp = spotipy.Spotify(auth=token)

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


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        wordlist = status.text.split()
        if wordlist[1] == 'redeem':
            query = ' '.join(wordlist[2:])
            print(f'redeeming {query}')
            if token:
                sp.start_playback(uris=[sp.search(query)['tracks']['items'][0]['uri']])


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=[f'@{api.me().screen_name}'])

if __name__ == '__main__':
    pass
