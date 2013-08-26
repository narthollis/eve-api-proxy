
from core import EveProxyBaseRequestHandler

class AllianceList(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/AllianceList.xml"


class CertificateTree(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/CertificateTree.xml"


class CharacterID(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/CharacterID.xml"


class CharacterInfo(EveProxyBaseRequestHandler):
    requiredParamaters = []
    optionalParamaters = ['keyID', 'vCode']
    urlPart = "/eve/CharacterInfo.xml"


class CharacterName(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/CharacterName.xml"


class ConquerableStationList(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/ConquerableStationList.xml"


class ErrorList(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/ErrorList.xml"


class FacWarStats(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/FacWarStats.xml"


class FacWarTopStats(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/FacWarTopStats.xml"


class RefTypes(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/RefTypes.xml"


class SkillTree(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/SkillTree.xml"


class TypeName(EveProxyBaseRequestHandler):
    requiredParamaters = []
    urlPart = "/eve/TypeName.xml"

