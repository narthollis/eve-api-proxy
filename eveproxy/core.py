
import json, hashlib, datetime, urllib2, re
from urllib import urlencode

import webapp2

from google.appengine.ext import ndb


class APICacheObject(ndb.Model):
    response = ndb.TextProperty()
    status = ndb.IntegerProperty()
    expiry = ndb.DateTimeProperty()


class EveProxyBaseRequestHandler(webapp2.RequestHandler):
    APIROOT = 'https://api.eveonline.com'

    expiryRe = re.compile(r'<cachedUntil>(.*)</cachedUntil>')

    paramaterDefaults = {}
    requiredParamaters = []
    optionalParamaters = []
    cacheTime = None

    def log(self, message):
        self.response.headers.add('X-API-Proxy-Log', str(message))

    def get(self):
        self.response.headers['Content-Type'] = 'application/xml;charset=UTF-8'
        self.response.headers['Access-Control-Allow-Origin'] = '*'

        params = {}
        for key in self.requiredParamaters:
            params[key] = self.request.get(key, self.paramaterDefaults.get(key, None))
            if not params[key]:
                return self.error(400)
        for key in self.optionalParamaters:
            p = self.request.get(key)
            if p:
                params[key] = p

        path = self.request.path + '.aspx'
        if not path.startswith('/'):
            path = '/' + path

        self.log(path)
        self.log(json.dumps(params))

        h = hashlib.md5()
        h.update(path)
        h.update(json.dumps(params))
        h = h.hexdigest()

        key = ndb.Key(APICacheObject, h)
        api_cache = key.get()

        currentTime = datetime.datetime.utcnow()

        self.response.headers['X-API-Proxy'] = 'From Cache'

        if api_cache != None:
            if api_cache.expiry:
                if currentTime > api_cache.expiry:
                    self.response.headers['X-API-Proxy-Removed'] = 'Cache Expirerd'
                    key.delete()
                    api_cache = None
            else:
                self.response.headers['X-API-Proxy-Removed'] = 'Cache No Expiry'
                key.delete()
                api_cache = None

        if api_cache == None:
            self.response.headers['X-API-Proxy'] = 'New Request'

            api_cache = APICacheObject(key=key)

            try:
                params = urlencode(params)

                print self.APIROOT + path + '?' + params

                up_stream = urllib2.urlopen(self.APIROOT + path, params)
                #up_stream = urllib2.urlopen(self.APIROOT + path + '?' + params)

                api_cache.response = up_stream.read()
                api_cache.status = up_stream.getcode()

                result = self.expiryRe.search(api_cache.response)
                if result:
                    api_cache.expiry = datetime.datetime.strptime(result.group(1), '%Y-%m-%d %H:%M:%S')

                if not api_cache.expiry:
                    if self.cacheTime:
                        api_cache.expiry = currentTime + self.cacheTime
                    else:
                        api_cache.expiry = currentTime + datetime.timedelta(seconds=60)

            except urllib2.HTTPError, e:
                api_cache.response = e.reason
                api_cache.status = e.code
                api_cache.expiry = currentTime + datetime.timedelta(seconds=60)

            api_cache.put()

        self.response.headers['X-API-Cache-Until'] = api_cache.expiry.isoformat()
        self.response.headers['X-API-Cache-Current-Time'] = currentTime.isoformat()

        self.response.status = api_cache.status
        self.response.write(api_cache.response + '\n')

    def post(self):
        self.get()

