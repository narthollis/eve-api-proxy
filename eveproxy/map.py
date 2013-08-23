
from core import EveProxyBaseRequestHandler

class FacWarSystems(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/map/FacWarSystems.xml"


class Jumps(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/map/Jumps.xml"


class Kills(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/map/Kills.xml"


class Sovereignty(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/map/Sovereignty.xml"


class SovereigntyStatus(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/map/SovereigntyStatus.xml"

