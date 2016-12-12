#!/usr/bin/env python

import tweepy, time, os, sys, yaml

#enter the corresponding information from your Twitter application:

# Load twitter credentials for this bot from config file
BOTCRED_FILE = '%s/.twurlrc' % os.path.expanduser('~') 
with open(BOTCRED_FILE, 'r') as credfile:
	full_config = yaml.load(credfile)
	api_key = api_key = full_config['profiles']['mirrorbar'].keys()[0]
	bot_creds = full_config['profiles']['mirrorbar'][api_key]

CONSUMER_KEY = bot_creds['consumer_key']
CONSUMER_SECRET = bot_creds['consumer_secret']
ACCESS_KEY = bot_creds['token']
ACCESS_SECRET = bot_creds['secret']

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
