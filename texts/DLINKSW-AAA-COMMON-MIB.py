#
# PySNMP MIB module DLINKSW-AAA-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-AAA-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwAAACommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150))
dlinkSwAAACommonMIB.setRevisions(('2013-01-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setRevisionsDescriptions(('This is the first version of the MIB file.',))
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setLastUpdated('201301170000Z')
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setContactInfo('        D-Link Corporation\n\n                Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                        Taipei City 114, Taiwan, R.O.C\n                Tel:     +886-2-66000123\n                E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setDescription('The MIB module\tfor configuring AAA common feature.\n\t\t This MIB module also provides Textual Conventions \n         and OBJECT-IDENTITY Objects to be used AAA services.\n\t\t')
class DAaaSessionType(TextualConvention, Integer32):
    description = 'Represents a session type.\n\n            telnet(1) - indicates telnet session.\n\n            console(2) - indicates console session.\n\n            ssh(3) - indicates ssh session.\n\n            http(4) - indicates http session.\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("ssh", 3), ("http", 4))

class DAaaPrivilegeLevel(TextualConvention, Integer32):
    description = 'Represents privilege level.\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

class DAaaMethodListName(TextualConvention, OctetString):
    description = 'Represents the name of a method list.\n\n            The following name are reserved and cannot be used as the name of \n            method list:\n            enable, none, local, tacacs, xtacacs, tacacs+, radius             \n            '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class DAaaMethodPriority(TextualConvention, Integer32):
    description = 'Represents the priority of a method. Lower numbers indicate\n            higher priority.\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4)

class DAaaMethodName(TextualConvention, OctetString):
    description = "Represents method name.\n\n            The following name are reserved and cannot be used as method name:\n            enable, local, tacacs, and xtacacs\n       \n            The following name are reserved method name which can be applied but cannot\n            be manually created:\n            none, tacacs+ and radius.\n            \n            none - Do not perform accounting or authentication.\n            radius - Use the servers defined at dasServerConfigTable (the value of dasServerProtocol\n                    is 'radius').\n            tacacs+ - Use the servers defined at dasServerConfigTable (the value of dasServerProtocol\n                    is 'tacacsplus').             \n            The name of dasGroupName - Uses the servers which are grouped into the specified group\n                    in dasGroupTable.\n            "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

dAaaCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 0))
dAaaMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150, 1))
if mibBuilder.loadTexts: dAaaMIBObjects.setStatus('current')
if mibBuilder.loadTexts: dAaaMIBObjects.setDescription('This object provides OBJECT-IDENTITY for other AAA MIB modules.                     \n            ')
dAaaCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2))
dAaaCommonObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1))
if mibBuilder.loadTexts: dAaaCommonObjects.setStatus('current')
if mibBuilder.loadTexts: dAaaCommonObjects.setDescription('Group of objects that are related to the common AAA feature.                          \n            ')
dAaaNewModelEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dAaaNewModelEnabled.setStatus('current')
if mibBuilder.loadTexts: dAaaNewModelEnabled.setDescription("Set this object to 'true' to enable AAA global state, then the\n\t        authentication and  accounting via the AAA method lists will \n\t        take effect.\n\t        Set this object to 'false' to globally disable AAA.\n\t        ")
dAaaCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1))
daaaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1, 1)).setObjects(("DLINKSW-AAA-COMMON-MIB", "daaaGlobalCtrlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    daaaMIBCompliance = daaaMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: daaaMIBCompliance.setDescription('The compliance statement for entities which implement the \n\t        DLINKSW-AAA-COMMON-MIB.\n\t        ')
dAaaCommonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2))
daaaGlobalCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2, 1)).setObjects(("DLINKSW-AAA-COMMON-MIB", "dAaaNewModelEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    daaaGlobalCtrlGroup = daaaGlobalCtrlGroup.setStatus('current')
if mibBuilder.loadTexts: daaaGlobalCtrlGroup.setDescription('Objects for globally configuring AAA feature.\n\t        ')
mibBuilder.exportSymbols("DLINKSW-AAA-COMMON-MIB", DAaaSessionType=DAaaSessionType, dAaaCommonMIBCompliances=dAaaCommonMIBCompliances, PYSNMP_MODULE_ID=dlinkSwAAACommonMIB, DAaaPrivilegeLevel=DAaaPrivilegeLevel, dAaaCommonMIBNotifications=dAaaCommonMIBNotifications, dAaaCommonMIBGroups=dAaaCommonMIBGroups, DAaaMethodPriority=DAaaMethodPriority, DAaaMethodListName=DAaaMethodListName, dAaaCommonObjects=dAaaCommonObjects, daaaGlobalCtrlGroup=daaaGlobalCtrlGroup, DAaaMethodName=DAaaMethodName, daaaMIBCompliance=daaaMIBCompliance, dAaaNewModelEnabled=dAaaNewModelEnabled, dAaaMIBObjects=dAaaMIBObjects, dlinkSwAAACommonMIB=dlinkSwAAACommonMIB, dAaaCommonMIBConformance=dAaaCommonMIBConformance)
