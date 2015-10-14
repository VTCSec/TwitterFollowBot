#!/usr/bin/env python

from TwitterFollowBot import TwitterBot
import facebook_bot
import time,sys,re

if len(sys.argv) != 3:
    print('usage: ./mr_vtcsec <twitter-config> <fb-access-token-file>')
    sys.exit(1)

tbot = TwitterBot(sys.argv[1])
fbot = facebook_bot.FacebookBot(sys.argv[2],'203269536364770')  # public id of vtcsec fb page

def build_link(t,author):
    return 'https://twitter.com/'+author+'/status/'+str(t['id'])

def build_fb_post(t):
    text = t['retweeted_status']['text']
    print text

    author = re.search(r'@(.+?):',t['text']).groups()[0]
    src = build_link(t,author)
    if 'entities' in t:
        if len(t['entities']['urls']):
            src = t['entities']['urls'][0]['expanded_url']
    print author
    return """
        %s (@%s, %s)
    """ % (text,author,src)
    

while True:
    print 'retweeting..'
    try:
        tweets = tbot.auto_rt_user_popular('_conorpp',count=4)
        tbot.sync_follows()
        #tweets = [{'text':'RT @_conorpp: rab fdewfhewo http://example.com'}]
        for i in tweets:
            text = i['retweeted_status']['text']
            if '@' in text:
                continue
            post = build_fb_post(i)
            print('posted to facebook: ', post)
            fbot.api.put_wall_post(post)
    except Exception as e:
        print(e)
    # only run once per 3 minutes to avoid rate limit
    time.sleep(180)
