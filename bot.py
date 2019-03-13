from config import *
import random, sys, time, tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter = tweepy.API(auth)

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