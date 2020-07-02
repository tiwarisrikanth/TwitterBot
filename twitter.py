import tweepy
import time

auth = tweepy.OAuthHandler('tquRuwtO0J1t6SBHt20WBwW95', 'cwP7Ae9B4rvubpY1pfuDjJSEIvwV1rS75EYt7gQI9r7nK8luAQ')

auth.set_access_token('802507154456506368-T3B9wA5vorNckNTylSBPWWDyBLVk94H', 'cS7yVhKlDbRm3OeLzeL9UeHYnixMr73H4Qfq70pBA8zh9')

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

