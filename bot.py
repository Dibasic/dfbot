from config import *
import patreon, sys, time, tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter = tweepy.API(auth)

while True:
    print('Running...')
    content = get_content()
    twitter.update_status(content)
    time.sleep(INTERVAL)