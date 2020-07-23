import tweepy
from config import tokens

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


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=[f'@{api.me().screen_name}'])
