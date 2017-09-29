import tweepy
from textblob import TextBlob

# Authentication
consumer_key= '<enter your consumer key>'
# don't include "<>" for all keys
consumer_secret= '<enter your consumer secret>'
#you need a twitter account to generate keys
#you can get your consumer & access keys from link below
# https://apps.twitter.com/app/new

access_token='<enter your access token>'
access_token_secret='<enter your access token secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('Trump')


for tweet in public_tweets:
    print(tweet.text)
    
#Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
