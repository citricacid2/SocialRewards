from flask import Flask, request
import tweepy
from config import tokens

app = Flask(__name__)

cookie_values = {

}

@app.route('/')
def main():


@app.route('/oauth/twitter')
def oauth_twitter():

    return request.args.get('oauth_verifier')


@app.route('/oauth/spotify')
def oauth_spotify():
    return request.args.get('oauth_verifier')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
