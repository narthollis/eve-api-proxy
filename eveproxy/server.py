
from core import EveProxyBaseRequestHandler

class ServerStatus(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/server/ServerStatus.xml"

