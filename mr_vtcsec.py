#!/usr/bin/env python

from TwitterFollowBot import TwitterBot
import time,sys

bot = TwitterBot(sys.argv[1])

while True:
    print 'retweeting..'
    try:
        bot.auto_rt_user_popular('_conorpp',count=3)
        bot.sync_follows()
    except Exception as e:
        print(e)
    # only run once per 3 minutes to avoid rate limit
    time.sleep(180)
