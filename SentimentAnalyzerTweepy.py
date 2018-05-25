import tweepy
from textblob import TextBlob

# Authentication
consumer_key = "YOUR_APP_KEY"
consumer_secret = "YOUR_APP_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_SECRET"

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
