from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time
from datetime import datetime

#API_Keys and Access Tokens defination
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

auth = OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
    
db_tweets = pd.DataFrame(columns = ['created_at','Name', 'Text', 'Twitter_Handle', 'Location'])
    
start_time = time.time()

#Input search keyword inside quotes
search_word = ''

#Input inital date to extract tweets
date_since = ''

#Maximum number of Tweets is 1000. You can define any number inside items.
tweets = tweepy.Cursor(api.search, q = search_word, language = 'en', since = date_since).items(1000)
tweet_list = [tweet for tweet in tweets]
no_of_tweets = 0
for tweet in tweet_list:
    Created_at = tweet.created_at
    Name = tweet.user.name
    Text = tweet.text
    Twitter_Handle = tweet.user.screen_name
    Location = tweet.user.location
    ith_tweet = [Created_at, Name, Text, Twitter_Handle, Location]
    db_tweets.loc[len(db_tweets)] = ith_tweet
    no_of_tweets += 1
to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
path = os.getcwd()
filename = path + '/data/' + to_csv_timestamp + 'tweets.csv'
db_tweets.to_csv(filename, encoding = 'utf-8', index = False)
end_time = time.time()
print('Time taken to scrape tweets is %s' %(end_time - start_time))
time.sleep(900)
