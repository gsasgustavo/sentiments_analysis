import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

a = open('twitter_credentials.json','r')
b = json.load(a)

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(b['consumer_key'], b['consumer_secret'])
    auth.set_access_token(b['access_token'], b['access_token_secret'])
    stream = Stream(auth, l)

    stream.filter(track=['python', 'javascript', 'ruby'])