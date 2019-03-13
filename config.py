import os

# Twitter authentication variables, hardcode if you wish
CONSUMER_KEY    = os.environ['DFBOT_CONSUMER_KEY']      if 'DFBOT_CONSUMER_KEY'     in os.environ else 'DFBOT_DEFAULT_KEY'
CONSUMER_SECRET = os.environ['DFBOT_CONSUMER_SECRET']   if 'DFBOT_CONSUMER_SECRET'  in os.environ else 'DFBOT_DEFAULT_SECRET'
ACCESS_KEY      = os.environ['DFBOT_ACCESS_KEY']        if 'DFBOT_ACCESS_KEY'       in os.environ else 'DFBOT_DEFAULT_KEY'
ACCESS_SECRET   = os.environ['DFBOT_ACCESS_SECRET']     if 'DFBOT_ACCESS_SECRET'    in os.environ else 'DFBOT_DEFAULT_SECRET'

# INTERVAL: time between each Tweet, in seconds
INTERVAL = 60 * 60 * 6