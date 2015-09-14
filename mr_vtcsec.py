#!/usr/bin/env python

from TwitterFollowBot import TwitterBot
import time,sys

bot = TwitterBot(sys.argv[1])

while True:
    print 'retweeting..'
    try:
        bot.auto_rt_user_popular('_conorpp',count=3)
    except Exception as e:
        print(e)
    time.sleep(5)
