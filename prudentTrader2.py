#Script to authorise twitter access on behalf of us

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import simplejson as json

consumer_key = '6ihQfJrlrbvBZpNLmGVGPwSSd'
consumer_secret = 'fCQmDjzBF3uNz7yQ1LxtrL27buxrs2DdTaNUtZOPpzaT7BSR6C'
access_token = '766090286804135936-wuQ1Du64kt0uvY2mCPkfU45iRvBVr7G'
access_secret = 'WdGNRwPKGEHVbs7zv1sUv1ULwR02KpxW7KxdUwYHvdoSr'

#For opening your account and checking the tweets
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#Api variable is the entry point to access most tweets
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
            return True
    def on_error(self, data):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Google'])

