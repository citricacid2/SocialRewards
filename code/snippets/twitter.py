import twitter
from config import tokens

print(tokens['consumer_key'])
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

if __name__ == '__main__':
    pass