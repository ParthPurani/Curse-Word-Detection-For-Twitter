import tweepy
import json
#from textblob import TextBlob
#from gtts import gTTS
#import os, time
#import re
#from nltk.tokenize import word_tokenize

#nltk.download('punkt')
# Authentication
consumer_key= 'zRJA6MtT0TuhMQzoFpwbWPtjo'
consumer_secret= 'y3ugtakLvC1mShJCef2KZnNof7io0SXWKrTW2ZQHiLvhMilPg9'

access_token='1371632089-28V48w18t6fvOx3rRAqFasX9o3XvQ7bh4Zo4r39'
access_token_secret='XL0kgbuzzuFaZlEcXCWj5ajiM5adHmjBdObhuTrvBa70a'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


for friend in tweepy.Cursor(api.friends).items(200):
    #print(friend._json)
    json_data = friend._json
    
    dict_json = dict(json_data)
    print(dict_json['screen_name'])

#
#           
#for status in tweepy.Cursor(api.home_timeline).items(10):
#    # Process a single status
#    tweet = status.text
#    #speech = re.sub(r"http\S+", "", tweet)
#    speech = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
#    print(speech + '\n')
#
#    
#t = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
#msg = "Alert !! Motion detected at " + t
#
## Send Direct Message to official Twitter handle
##api.send_direct_message(screen_name='Patriotic_Parth', text =msg) 
#    
#   
#language = 'en-IN'
#
#myobj = gTTS(text=speech, lang=language, slow=False)
#
#myobj.save("speech.mp3") 
#os.system("mpg321 speech.mp3")   

'''
#Retrieve Tweets
public_tweets = api.search('Tesla')


for tweet in public_tweets:
    print(tweet.text)
    
#Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
print("")
'''