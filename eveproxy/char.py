
from core import EveProxyBaseRequestHandler

class AccountBalance(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/AccountBalance.xml"


class AssetList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/AssetList.xml"


class CalendarEventAttendees(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'eventIDs']
    urlPart = "/char/CalendarEventAttendees.xml"


class CharacterSheet(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/CharacterSheet.xml"


class ContactList(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/ContactList.xml"


class ContactNotifications(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/ContactNotifications.xml"


class Contracts(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    optionalParamaters = ['contractID']
    urlPart = "/char/Contracts.xml"


class ContractItems(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'contractID']
    urlPart = "/char/ContractItems.xml"


class ContractBids(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/ContractBids.xml"


class FacWarStats(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/FacWarStats.xml"


class IndustryJobs(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/IndustryJobs.xml"


class Killlog(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    optionalParamaters = ['beforeKillID']
    urlPart = "/char/Killlog.xml"


class Locations(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'IDs']
    urlPart = "/char/Locations.xml"


class MailBodies(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'ids']
    urlPart = "/char/MailBodies.xml"


class MailingLists(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/MailingLists.xml"


class MailMessages(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/MailMessages.xml"


class MarketOrders(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    optionalParamaters = ['orderID']
    urlPart = "/char/MarketOrders.xml"


class Medals(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/Medals.xml"


class Notifications(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/Notifications.xml"


class NotificationTexts(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'IDs']
    urlPart = "/char/NotificationTexts.xml"


class Research(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/Research.xml"


class SkillInTraining(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/SkillInTraining.xml"


class SkillQueue(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/SkillQueue.xml"


class Standings(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/Standings.xml"


class UpcomingCalendarEvents(EveProxyBaseRequestHandler):
    requiredParamaters = ['keyID', 'vCode', 'characterID']
    urlPart = "/char/UpcomingCalendarEvents.xml"


class WalletJournal(EveProxyBaseRequestHandler):
    paramaterDefaults = {'accountKey': 1000}
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'accountKey']
    optionalParamaters = ['fromID', 'rowCount']
    urlPart = "/char/WalletJournal.xml"


class WalletTransactions(EveProxyBaseRequestHandler):
    paramaterDefaults = {'accountKey': 1000}
    requiredParamaters = ['keyID', 'vCode', 'characterID', 'accountKey']
    optionalParamaters = ['fromID', 'rowCount']
    urlPart = "/char/WalletTransactions.xml"

