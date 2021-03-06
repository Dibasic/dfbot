import os

# Heroku wants a server to exist.
HOST = '0.0.0.0'
PORT = os.environ['PORT'] if 'PORT' in os.environ else '80'

USER_AGENT = os.environ['DFBOT_USER_AGENT'] if 'DFBOT_USER_AGENT' in os.environ else 'twitter@dfpatchnotesbot - requests only once per build - https://github.com/Dibasic/dfbot'

# Twitter authentication variables
CONSUMER_KEY    = os.environ['DFBOT_TWITTER_CONSUMER_KEY']      if 'DFBOT_TWITTER_CONSUMER_KEY'     in os.environ else 'DFBOT_TWITTER_CONSUMER_KEY'
CONSUMER_SECRET = os.environ['DFBOT_TWITTER_CONSUMER_SECRET']   if 'DFBOT_TWITTER_CONSUMER_SECRET'  in os.environ else 'DFBOT_TWITTER_CONSUMER_SECRET'
ACCESS_KEY      = os.environ['DFBOT_TWITTER_ACCESS_KEY']        if 'DFBOT_TWITTER_ACCESS_KEY'       in os.environ else 'DFBOT_TWITTER_ACCESS_KEY'
ACCESS_SECRET   = os.environ['DFBOT_TWITTER_ACCESS_SECRET']     if 'DFBOT_TWITTER_ACCESS_SECRET'    in os.environ else 'DFBOT_TWITTER_ACCESS_SECRET'

# INTERVAL: time between each Tweet, in seconds
INTERVAL = os.environ['DFBOT_INTERVAL'] if 'DFBOT_INTERVAL' in os.environ else 60 * 60 * 6