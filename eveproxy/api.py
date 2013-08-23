
from core import EveProxyBaseRequestHandler

class calllist(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/api/calllist.xml"

