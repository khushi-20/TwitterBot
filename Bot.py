import tweepy
import time


auth = tweepy.OAuthHandler('','')
auth.set_access_token('','')
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(FILE_NAME,last_seen_id):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    tweets = api.mentions_timeline(retrieve_last_seen_id(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(tweets):
       if '#HelloWorld123' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status('@' + tweet.user.screen_name +'#HelloWorld back to you!', tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen_id(FILE_NAME,tweet.id)
   

while True:
    reply_to_tweets()
    time.sleep(15)

