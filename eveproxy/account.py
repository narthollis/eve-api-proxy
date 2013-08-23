
from core import EveProxyBaseRequestHandler

class AccountStatus(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/account/AccountStatus.xml"


class APIKeyInfo(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/account/APIKeyInfo.xml"


class Characters(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/account/Characters.xml"

