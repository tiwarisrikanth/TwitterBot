import tweepy
import time

auth = tweepy.OAuthHandler('API key', 'API secret key')

auth.set_access_token('Access token', 'Access secret token')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user)

search = '#ChineseAppBanned'

nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print("ReTweeted")
        tweet.retweet()
        time.sleep(1)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

