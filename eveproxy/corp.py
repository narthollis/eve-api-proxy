
from core import EveProxyBaseRequestHandler

class AccountBalance(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/AccountBalance.xml"


class AssetList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/AssetList.xml"


class ContactList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/ContactList.xml"


class ContainerLog(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/ContainerLog.xml"


class Contracts(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Contracts.xml"


class ContractItems(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/ContractItems.xml"


class ContractBids(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/ContractBids.xml"


class CorporationSheet(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/CorporationSheet.xml"


class FacWarStats(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/FacWarStats.xml"


class IndustryJobs(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/IndustryJobs.xml"


class Killlog(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Killlog.xml"


class Locations(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Locations.xml"


class MarketOrders(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/MarketOrders.xml"


class Medals(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Medals.xml"


class MemberMedals(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/MemberMedals.xml"


class MemberSecurity(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/MemberSecurity.xml"


class MemberSecurityLog(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/MemberSecurityLog.xml"


class MemberTracking(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/MemberTracking.xml"


class OutpostList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/OutpostList.xml"


class OutpostServiceDetail(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/OutpostServiceDetail.xml"


class Shareholders(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Shareholders.xml"


class Standings(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Standings.xml"


class StarbaseDetail(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/StarbaseDetail.xml"


class StarbaseList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/StarbaseList.xml"


class Titles(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/Titles.xml"


class WalletJournal(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/WalletJournal.xml"


class WalletTransactions(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode']
    urlPart = "/corp/WalletTransactions.xml"

