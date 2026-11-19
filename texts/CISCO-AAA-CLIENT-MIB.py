#
# PySNMP MIB module CISCO-AAA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoAAAClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 158))
ciscoAAAClientMIB.setRevisions(('2001-11-19 00:00', '2001-05-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAAAClientMIB.setRevisionsDescriptions(('Deprecate object cacLockoutPeriod and add a new object \n         cacLockoutPeriodExt.\n        ', 'Initial version\n        ',))
if mibBuilder.loadTexts: ciscoAAAClientMIB.setLastUpdated('200111190000Z')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n \n                Tel: +1 800 553-NETS\n \n                E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setDescription('This MIB module provides data for authentication method \n                 priority based on Authentication, Authorization, \n                 Accounting (AAA) protocols.\n\n\n                 References:\n                     The TACACS+ Protocol Version 1.78, Internet Draft\n                     RFC 1411 Telnet Authentication: Kerberos Version 4.\n                     RFC 1964 The Kerberos Version 5 GSS-API Mechanism.\n                ')
class SessionType(TextualConvention, Integer32):
    description = 'Represents a session type.\n\n      telnet(1) indicates telnet session.\n\n      console(2) indicates console session.\n\n      http(3) indicates http session.\n\n      '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("http", 3))

class AuthenMethod(TextualConvention, Integer32):
    description = 'Represents authentication method.\n\n     tacacs(1) indicates that TACACS method is used for\n     authentication.\n\n     radius(2) indicates that RADIUS method is used for\n     authentication.\n\n     kerberos(3) indicates that KERBEROS method is used\n     for authentication.\n\n     local(4) indicates that local password is used\n     for authentication. Which password is used depend\n     on what login mode users specified. \n     '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tacacs", 1), ("radius", 2), ("kerberos", 3), ("local", 4))

class LoginMode(TextualConvention, Integer32):
    description = 'Represents login mode.\n\n     login(1) indicates the normal mode.\n\n     enable(2) indicates the privileged mode.\n     '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("login", 1), ("enable", 2))

cacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1))
cacPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1))
cacLoginConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2))
cacPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1), )
if mibBuilder.loadTexts: cacPriorityTable.setStatus('current')
if mibBuilder.loadTexts: cacPriorityTable.setDescription('This table contains entries for AAA authentication \n           methods configured in the system. At startup, agent \n           set up all the entries of the table. All authentication\n           methods will be disabled except local authentication will \n           be enabled for each session type and login mode. Users \n           later can enable/disable a specific authentication method \n           through cacEnable object. \n \n           The following table describes the startup state of each\n           authentication method and session type in normal login\n           mode and enable login mode.\n \n           AuthenMethod Console Session   Telnet Session    Http Session\n           ------------ ----------------  ----------------  ------------\n           tacacs       disabled          disabled          disabled\n           radius       disabled          disabled          disabled\n           kerberos     disabled          disabled          disabled\n           local        enabled(*)        enabled(*)        enabled(*)\n \n           (*) denotes primary method.\n           ')
cacPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacSession"), (0, "CISCO-AAA-CLIENT-MIB", "cacAuthen"), (0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"))
if mibBuilder.loadTexts: cacPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: cacPriorityEntry.setDescription('An entry containing the priority number of an authentication\n            method used in a session. \n            ')
cacSession = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 1), SessionType())
if mibBuilder.loadTexts: cacSession.setStatus('current')
if mibBuilder.loadTexts: cacSession.setDescription('This is the session type used to connect to the network\n           device.\n           ')
cacAuthen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 2), AuthenMethod())
if mibBuilder.loadTexts: cacAuthen.setStatus('current')
if mibBuilder.loadTexts: cacAuthen.setDescription('This is the authentication method used to authenticate \n           users. \n           ')
cacLoginMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 3), LoginMode())
if mibBuilder.loadTexts: cacLoginMode.setStatus('current')
if mibBuilder.loadTexts: cacLoginMode.setDescription('This is the login mode user used to login to the network\n           device.\n           ')
cacEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacEnable.setStatus('current')
if mibBuilder.loadTexts: cacEnable.setDescription('It indicates whether the authentication method denoted by\n          cacAuthen is enabled or not.\n\n          When this object is true(1), the authentication method denoted\n          by cacAuthen is enabled.\n\n          When this object is false(2), the authentication method denoted\n          by cacAuthen is disabled.\n\n          If the value of cacAuthen is local, the value of this\n          object cannot be set to false(2). \n          ')
cacPriorityNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacPriorityNumber.setStatus('current')
if mibBuilder.loadTexts: cacPriorityNumber.setDescription('This is the priority number of an authentication method to \n          be used in user authentication for a session. This value is \n          automatically assigned and reflects the relative priority \n          of the authentication method denoted by cacAuthen with \n          respected to already configured authentication methods. \n          It is assigned in the order in which the authentication\n          method is enabled by the user through cacEnable.  \n          The higher value has the higher priority. This object\n          is used to determine the fallback order in case the\n          primary authentication method indicated by cacPrimaryMethod\n          failed.  \n\n          If the authentication method denoted by cacAuthen is disabled \n          for the type of session denoted by cacSession, the value\n          of this object is equal to 0.\n          ')
cacPrimaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacPrimaryMethod.setStatus('current')
if mibBuilder.loadTexts: cacPrimaryMethod.setDescription('It indicates whether the authentication method denoted by\n          cacAuthen is the primary (first one to be tried) method \n          when there are multiple authentication method configured.\n\n          Setting this object to true(1) will make the authentication \n          method denoted by cacAuthen to be the primary authentication\n          method for the session denoted by cacSession. The previously\n          configured primary method will be changed to false(2).\n          \n          Setting this object to false(2) is not allowed.\t\n          ')
cacLoginConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1), )
if mibBuilder.loadTexts: cacLoginConfigTable.setStatus('current')
if mibBuilder.loadTexts: cacLoginConfigTable.setDescription('A table that contains login configuration \n         which is associated with this system.\n        ')
cacLoginConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"), (0, "CISCO-AAA-CLIENT-MIB", "cacSession"))
if mibBuilder.loadTexts: cacLoginConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cacLoginConfigEntry.setDescription('An entry containing the configuration of the login.\n        ')
cacMaxLoginAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacMaxLoginAttempt.setStatus('current')
if mibBuilder.loadTexts: cacMaxLoginAttempt.setDescription('Indicates the maximum number of login attempts allowed.\n             Setting this variable to 0 will disable the attempt\n             limit checking.\n\n             If the login session type does not support this attempt \n             limit checking, the value of this object can only be set \n             to 0.\n            ')
cacLockoutPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 600), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriod.setStatus('deprecated')
if mibBuilder.loadTexts: cacLockoutPeriod.setDescription('Indicates the lockout period after the maximum number\n             of login attempt is met. For console, the console input\n             will be frozen during this period. For remote logins, the\n             connection will be closed and any subsequent access\n             from that station will be closed during the lockout time.\n\n             Setting this variable to 0 will disable the lockout.\n             If the login session type does not support this lockout \n             period, the value of this object can only be set to 0.\n         \n            If the lockout period is greater than the maximum value\n            reportable by this object then this object should report \n            its maximum value (600) and cacLockoutPeriodExt must be\n            used to report the lockout period.\n            ')
cacLockoutPeriodExt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 43200), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriodExt.setStatus('current')
if mibBuilder.loadTexts: cacLockoutPeriodExt.setDescription('Specifies the lockout period after the maximum number\n             of login attempt is met. For console, the console input\n             will be frozen during this period. For remote logins, the\n             connection will be closed and any subsequent access\n             from that station will be closed during the lockout time.\n\n             Setting this variable to 0 will disable the lockout.\n             If the login session type does not support this lockout\n             period, the value of this object can only be set to 0.\n            ')
cacMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 2))
cacMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3))
cacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1))
cacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2))
cacMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance = cacMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cacMIBCompliance.setDescription('The compliance statement for entities which\n             implement the CISCO AAA Client MIB')
cacMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance2 = cacMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: cacMIBCompliance2.setDescription('The compliance statement for entities which\n             implement the CISCO AAA Client MIB')
cacPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacEnable"), ("CISCO-AAA-CLIENT-MIB", "cacPriorityNumber"), ("CISCO-AAA-CLIENT-MIB", "cacPrimaryMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacPriorityGroup = cacPriorityGroup.setStatus('current')
if mibBuilder.loadTexts: cacPriorityGroup.setDescription('A collection of objects providing the\n             AAA client priority information.\n            ')
cacLoginConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroup = cacLoginConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cacLoginConfigGroup.setDescription('A collection of objects providing the\n             AAA client login configuration.\n            ')
cacLoginConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 3)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriodExt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroupRev1 = cacLoginConfigGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cacLoginConfigGroupRev1.setDescription('A collection of objects providing the\n             AAA client login configuration. \n            ')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-MIB", cacMIBCompliance2=cacMIBCompliance2, cacSession=cacSession, cacLoginConfig=cacLoginConfig, cacAuthen=cacAuthen, cacPriorityNumber=cacPriorityNumber, cacPriority=cacPriority, cacPrimaryMethod=cacPrimaryMethod, cacLoginMode=cacLoginMode, cacLoginConfigGroupRev1=cacLoginConfigGroupRev1, cacLoginConfigTable=cacLoginConfigTable, AuthenMethod=AuthenMethod, LoginMode=LoginMode, cacEnable=cacEnable, cacMIBCompliances=cacMIBCompliances, cacPriorityGroup=cacPriorityGroup, cacMIBGroups=cacMIBGroups, PYSNMP_MODULE_ID=ciscoAAAClientMIB, cacMIBConformance=cacMIBConformance, SessionType=SessionType, cacMaxLoginAttempt=cacMaxLoginAttempt, cacMIBNotifications=cacMIBNotifications, cacLockoutPeriodExt=cacLockoutPeriodExt, ciscoAAAClientMIB=ciscoAAAClientMIB, cacPriorityTable=cacPriorityTable, cacLoginConfigEntry=cacLoginConfigEntry, cacPriorityEntry=cacPriorityEntry, cacLoginConfigGroup=cacLoginConfigGroup, cacMIBCompliance=cacMIBCompliance, cacMIBObjects=cacMIBObjects, cacLockoutPeriod=cacLockoutPeriod)
