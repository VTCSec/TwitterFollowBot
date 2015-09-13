#!/usr/bin/env python

from TwitterFollowBot import TwitterBot
import time

bot = TwitterBot('config.txt')

while True:
    print 'retweeting..'
    bot.auto_rt_user_popular('_conorpp',count=3)
    time.sleep(5)
