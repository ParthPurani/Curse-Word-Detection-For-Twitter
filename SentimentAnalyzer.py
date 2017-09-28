import tweepy
from textblob import TextBlob

# Authentication
consumer_key= 'aoQUYl98DiYd89rDQFbaiytuI'
consumer_secret= 'CWrmm7hhar9zPh0LZ2rwF33f4A5wSGjxtD4gLXEzoWXTmei7hj'

access_token='1378641992-iCSZJiWLyqta33vgcDbz9SWVYm5LieNuuP8xBgj'
access_token_secret='ELWSe42Ahiz7mdW095hneYpoBwZ0hQlmbwzMGrpJ2oxA4'

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