from config import *
import random, sys, time, tweepy

twitter_auth = tweepy.OAuthHandler(DFBOT_TWITTER_CONSUMER_KEY, DFBOT_TWITTER_CONSUMER_SECRET)
twitter_auth.set_access_token(DFBOT_TWITTER_ACCESS_KEY, DFBOT_TWITTER_ACCESS_SECRET)
twitter = tweepy.API(twitter_auth)

def main():
    while True:
        print('Running...')
        content = get_content()
        twitter.update_status(content)
        time.sleep(INTERVAL)

def get_content():
    file = open('notes.txt', 'r')
    lines = []
    for line in file.readlines():
        lines.append(line)
    file.close()
    return random.choice(lines)

main()