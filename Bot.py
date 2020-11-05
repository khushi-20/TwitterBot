import tweepy
import time


auth = tweepy.OAuthHandler('fYusfCC25u3aYahYbEBok6Cli','KSZvD4Q75YIPIFpnIIApKJa6EaCdNb02gQMjgEDAIEqYd9gSbD')
auth.set_access_token('1177230960556855299-y0WyIxzpYwTwG83HpZyB69NzMPHS7r','K7VuxI5LIr96Pf2cGdwKqAgz7igISOT2KEHBjFAkM2904')
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#HelloWorldq' in mention.full_text.lower():
            print('found #helloworld!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
