#Script to authorise twitter access on behalf of us

import tweepy
from tweepy import OAuthHandler
import simplejson as json

consumer_key = '6ihQfJrlrbvBZpNLmGVGPwSSd'
consumer_secret = 'fCQmDjzBF3uNz7yQ1LxtrL27buxrs2DdTaNUtZOPpzaT7BSR6C'
access_token = '766090286804135936-wuQ1Du64kt0uvY2mCPkfU45iRvBVr7G'
access_secret = 'WdGNRwPKGEHVbs7zv1sUv1ULwR02KpxW7KxdUwYHvdoSr'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#Api variable is the entry point to access most tweets
api = tweepy.API(auth)

def process_or_store(tweet):
    with open('data.txt', 'w') as outfile:
        json.dump(tweet, outfile)
    with open('data.txt') as infile:
        datastore = json.load(infile)

print(datastore['created_at'])

#Tweepy cursor interface helps us iterate through objects
for status in tweepy.Cursor(api.home_timeline).items(10):
	#Process a single item
	process_or_store(status._json)
