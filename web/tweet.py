#!/usr/bin/env python

import tweepy, time, sys

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '***REMOVED***'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '***REMOVED***'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '***REMOVED***'#keep the quotes, replace this with your access token
ACCESS_SECRET = '***REMOVED***'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = '/home/ianfitzpat/webapps/mirrorbar/sessions-to-tweet.txt'
with open(filename, 'r') as fin:
    data = fin.read().splitlines(True)
    tweet_text = data[0]
    
with open(filename, 'w') as fout:
    fout.writelines(data[1:])

api.update_status(status=tweet_text)
