import tweepy
import requests
import pandas as pd
import json
import time
from datetime import datetime

access_key = "1774966742357327872-I9EBxxmQBY1dSZDAdLWtE27sPuhpyU"
access_secret = "6mCn9ky0mYUHgCjMVBETcsaJM8Qtorxla38xsiqNXL8TQ"
consumer_key = "AgftCDsfXIIBL9zoBwQ5WVoMb"
consumer_secret = "zqsmghsvnyqWqXkE6sRtfVPQSybJ8qxxPlvRTs24wbVHmPqQZu"

#Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#creating an api object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = "@elonmusk",
                           count = 200, #maximum 200 tweets is the allowed count
                           include_rts = False, #retweets will be excluded
                           tweet_mode = 'extended') #thiss extracts full text otherwise 140 words will be extracted

print(tweets)