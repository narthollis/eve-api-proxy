
import webapp2

import eveproxy.account
import eveproxy.char
import eveproxy.corp
import eveproxy.eve
import eveproxy.map
import eveproxy.server
import eveproxy.api


app = webapp2.WSGIApplication([
            (r'/account/AccountStatus.xml', eveproxy.account.AccountStatus),
            (r'/account/APIKeyInfo.xml', eveproxy.account.APIKeyInfo),
            (r'/account/Characters.xml', eveproxy.account.Characters),

            (r'/char/AccountBalance.xml', eveproxy.char.AccountBalance),
            (r'/char/AssetList.xml', eveproxy.char.AssetList),
            (r'/char/CalendarEventAttendees.xml', eveproxy.char.CalendarEventAttendees),
            (r'/char/CharacterSheet.xml', eveproxy.char.CharacterSheet),
            (r'/char/ContactList.xml', eveproxy.char.ContactList),
            (r'/char/ContactNotifications.xml', eveproxy.char.ContactNotifications),
            (r'/char/Contracts.xml', eveproxy.char.Contracts),
            (r'/char/ContractItems.xml', eveproxy.char.ContractItems),
            (r'/char/ContractBids.xml', eveproxy.char.ContractBids),
            (r'/char/FacWarStats.xml', eveproxy.char.FacWarStats),
            (r'/char/IndustryJobs.xml', eveproxy.char.IndustryJobs),
            (r'/char/Killlog.xml', eveproxy.char.Killlog),
            (r'/char/Locations.xml', eveproxy.char.Locations),
            (r'/char/MailBodies.xml', eveproxy.char.MailBodies),
            (r'/char/MailingLists.xml', eveproxy.char.MailingLists),
            (r'/char/MailMessages.xml', eveproxy.char.MailMessages),
            (r'/char/MarketOrders.xml', eveproxy.char.MarketOrders),
            (r'/char/Medals.xml', eveproxy.char.Medals),
            (r'/char/Notifications.xml', eveproxy.char.Notifications),
            (r'/char/NotificationTexts.xml', eveproxy.char.NotificationTexts),
            (r'/char/Research.xml', eveproxy.char.Research),
            (r'/char/SkillInTraining.xml', eveproxy.char.SkillInTraining),
            (r'/char/SkillQueue.xml', eveproxy.char.SkillQueue),
            (r'/char/Standings.xml', eveproxy.char.Standings),
            (r'/char/UpcomingCalendarEvents.xml', eveproxy.char.UpcomingCalendarEvents),
            (r'/char/WalletJournal.xml', eveproxy.char.WalletJournal),
            (r'/char/WalletTransactions.xml', eveproxy.char.WalletTransactions),

            (r'/corp/AccountBalance.xml', eveproxy.corp.AccountBalance),
            (r'/corp/AssetList.xml', eveproxy.corp.AssetList),
            (r'/corp/ContactList.xml', eveproxy.corp.ContactList),
            (r'/corp/ContainerLog.xml', eveproxy.corp.ContainerLog),
            (r'/corp/Contracts.xml', eveproxy.corp.Contracts),
            (r'/corp/ContractItems.xml', eveproxy.corp.ContractItems),
            (r'/corp/ContractBids.xml', eveproxy.corp.ContractBids),
            (r'/corp/CorporationSheet.xml', eveproxy.corp.CorporationSheet),
            (r'/corp/FacWarStats.xml', eveproxy.corp.FacWarStats),
            (r'/corp/IndustryJobs.xml', eveproxy.corp.IndustryJobs),
            (r'/corp/Killlog.xml', eveproxy.corp.Killlog),
            (r'/corp/Locations.xml', eveproxy.corp.Locations),
            (r'/corp/MarketOrders.xml', eveproxy.corp.MarketOrders),
            (r'/corp/Medals.xml', eveproxy.corp.Medals),
            (r'/corp/MemberMedals.xml', eveproxy.corp.MemberMedals),
            (r'/corp/MemberSecurity.xml', eveproxy.corp.MemberSecurity),
            (r'/corp/MemberSecurityLog.xml', eveproxy.corp.MemberSecurityLog),
            (r'/corp/MemberTracking.xml', eveproxy.corp.MemberTracking),
            (r'/corp/OutpostList.xml', eveproxy.corp.OutpostList),
            (r'/corp/OutpostServiceDetail.xml', eveproxy.corp.OutpostServiceDetail),
            (r'/corp/Shareholders.xml', eveproxy.corp.Shareholders),
            (r'/corp/Standings.xml', eveproxy.corp.Standings),
            (r'/corp/StarbaseDetail.xml', eveproxy.corp.StarbaseDetail),
            (r'/corp/StarbaseList.xml', eveproxy.corp.StarbaseList),
            (r'/corp/Titles.xml', eveproxy.corp.Titles),
            (r'/corp/WalletJournal.xml', eveproxy.corp.WalletJournal),
            (r'/corp/WalletTransactions.xml', eveproxy.corp.WalletTransactions),

            (r'/eve/AllianceList.xml', eveproxy.eve.AllianceList),
            (r'/eve/CertificateTree.xml', eveproxy.eve.CertificateTree),
            (r'/eve/CharacterID.xml', eveproxy.eve.CharacterID),
            (r'/eve/CharacterInfo.xml', eveproxy.eve.CharacterInfo),
            (r'/eve/CharacterName.xml', eveproxy.eve.CharacterName),
            (r'/eve/ConquerableStationList.xml', eveproxy.eve.ConquerableStationList),
            (r'/eve/ErrorList.xml', eveproxy.eve.ErrorList),
            (r'/eve/FacWarStats.xml', eveproxy.eve.FacWarStats),
            (r'/eve/FacWarTopStats.xml', eveproxy.eve.FacWarTopStats),
            (r'/eve/RefTypes.xml', eveproxy.eve.RefTypes),
            (r'/eve/SkillTree.xml', eveproxy.eve.SkillTree),
            (r'/eve/TypeName.xml', eveproxy.eve.TypeName),

            (r'/map/FacWarSystems.xml', eveproxy.map.FacWarSystems),
            (r'/map/Jumps.xml', eveproxy.map.Jumps),
            (r'/map/Kills.xml', eveproxy.map.Kills),
            (r'/map/Sovereignty.xml', eveproxy.map.Sovereignty),
            (r'/map/SovereigntyStatus.xml', eveproxy.map.SovereigntyStatus),

            (r'/server/ServerStatus.xml', eveproxy.server.ServerStatus),

            (r'/api/calllist.xml', eveproxy.api.calllist),
        ],
        debug=True)
