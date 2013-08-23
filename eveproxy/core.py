
import json, hashlib, datetime

import webapp2

from google.appengine.ext import ndb


class APICacheObject(ndb.Model):
    response = ndb.StringProperty()
    expiry = ndb.DateTimeProperty()


class EveProxyBaseRequestHandler(webapp2.RequestHandler):
    APIROOT = 'http://api.eve-online.com'

    def get(self):
        self.response.headers['Content-Type'] = 'application/xml;charset=UTF-8'
        self.response.headers['Access-Control-Allow-Origin'] = '*'

        params = {}
        for key in self.requiredParamaters:
            params[key] = self.request.get(key)
            if not params[key]:
                return self.error(400)

        path = self.request.path + '.aspx'

        h = hashlib.md5()
        h.update(path)
        h.update(json.dumps(params))
        h = h.hexdigest()

        key = ndb.Key(APICacheObject, h)
        api_cache = key.get()

        if api_cache != None:
            self.response.write("Found Cache Item\n")

            if datetime.datetime.now() > api_cache.expiry:
                key.delete()
                api_cache = None

        if api_cache == None:
            api_cache = APICacheObject(key=key)

            api_cache.response = path + '\n' + json.dumps(params)
            api_cache.expiry = datetime.datetime.now()+datetime.timedelta(seconds=60)

            api_cache.put()

            self.response.write('NOT FROM CACHE\n')


        self.response.write(api_cache.response + '\n')
        self.response.write(api_cache.expiry.isoformat() + '\n')
        self.response.write(datetime.datetime.now().isoformat() + '\n')


    def post(self):
        self.get()
