from flask import Flask, request, render_template, redirect, make_response, url_for
import requests
import tweepy
from config import tokens
import string, random

auth = tweepy.OAuthHandler(tokens["consumer_key"], tokens["consumer_secret"])

app = Flask(__name__)

cookie_values = {

}

def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# "(ass[\s\S]*?)"
# "{{ url_for\('static', filename='$1') }}"

# \((ass[\s\S]*?)\);
# \({{ url_for\('static', filename='$1') }}

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<name>/codegen')
def codegen(name):
    randomwords = ' '.join(requests.get('https://random-word-api.herokuapp.com/word?number=3').json())
    return render_template('page1.html', code=randomwords)


@app.route('/oauth/twitter')
def oauth_twitter():
    resp = make_response(redirect(url_for('twitterdetails')))
    id = get_random_string(10)
    resp.set_cookie('twitter_id', id)
    auth.request_token
    auth.get_access_token(request.args.get('oauth_verifier'))
    cookie_values[id] = tweepy.API(tweepy.OAuthHandler(
        tokens["consumer_key"],
        tokens["consumer_secret"]
    ).set_access_token(auth.access_token, auth.access_token_secret))
    return resp


@app.route('/twitter/login')
def twitterlogin():
    redirect_url = auth.get_authorization_url()
    return redirect(redirect_url)


@app.route('/twitter/details')
def twitterdetails():
    api = cookie_values[request.cookies.get('twitter_id')]
    list = []
    for i in api.home_timeline():
        list.append(i.text)
    return '\n'.join(list)

@app.route('/oauth/spotify')
def oauth_spotify():
    return request.args.get('oauth_verifier')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
