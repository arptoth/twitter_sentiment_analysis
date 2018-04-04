import tweepy
from textblob import TextBlob

consumer_key = "HmnAWGD4vnfpjL7DJxbvRGMuQ"
consumer_secret = "3qTYrGw0kVdTqtJZ5yIKkzO6PirMxTDK8anVOqVk0EGuzNPnOm"

access_token = "285566103-icKJD0n7KChDS4WmqdXj3eMbwJtl6quw4SorLPDX"

access_secret = "GLynBr5XweOqt28bBcrFCVwTXzVf2McYQBpVEGoxVT2ZI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
