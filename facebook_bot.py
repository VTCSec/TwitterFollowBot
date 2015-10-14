import facebook

class FacebookBot:
    #def post_to_facebook(msg):
    #    return self.api.put_wall_post(msg)

    def __init__(self,f,pageid):

        cfg = {'access_token':open(f,'r').read(),
                   'page_id': pageid
                   }

        graph = facebook.GraphAPI(cfg['access_token'])
        # Get page token to post as the page. You can skip 
        # the following if you want to post as yourself. 
        print graph
        """
        resp = graph.get_object('me/accounts')
        page_access_token = None
        for page in resp['data']:
          if page['id'] == cfg['page_id']:
              page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
        """
        self.api = graph
