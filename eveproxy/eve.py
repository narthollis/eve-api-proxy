
from core import EveProxyBaseRequestHandler

class AllianceList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/AllianceList.xml"


class CertificateTree(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/CertificateTree.xml"


class CharacterID(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/CharacterID.xml"


class CharacterInfo(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/CharacterInfo.xml"


class CharacterName(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/CharacterName.xml"


class ConquerableStationList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/ConquerableStationList.xml"


class ErrorList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/ErrorList.xml"


class FacWarStats(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/FacWarStats.xml"


class FacWarTopStats(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/FacWarTopStats.xml"


class RefTypes(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/RefTypes.xml"


class SkillTree(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/SkillTree.xml"


class TypeName(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/eve/TypeName.xml"

