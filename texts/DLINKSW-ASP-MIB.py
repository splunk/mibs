#
# PySNMP MIB module DLINKSW-ASP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-ASP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TruthValue, RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
dlinkSwArpSpoofingPreventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 76))
dlinkSwArpSpoofingPreventMIB.setRevisions(('2016-07-05 00:00', '2013-07-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setRevisionsDescriptions(('added dAspLoggingEnabled, dAspLoggingGroup and dAspCompliance2.\n            deprecated dAspCompliance', 'This is the first version of the MIB file.',))
if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setLastUpdated('201607050000Z')
if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setContactInfo('        D-Link Corporation\n\n                Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                        Taipei City 114, Taiwan, R.O.C\n                Tel:     +886-2-66000123\n                E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setDescription('The MIB module configures ARP spoofing prevention feature.\n            ')
dAspMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 0))
dAspMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 1))
dAspMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 2))
dAspGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1), )
if mibBuilder.loadTexts: dAspGatewayTable.setStatus('current')
if mibBuilder.loadTexts: dAspGatewayTable.setDescription('This table consists of a list of gateways for ARP spoofing \n            prevention (ASP) to prevent ARP poisoning attacking.')
dAspGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1), ).setIndexNames((0, "DLINKSW-ASP-MIB", "dAspGatewayIP"), (0, "DLINKSW-ASP-MIB", "dAspGatewayMAC"))
if mibBuilder.loadTexts: dAspGatewayEntry.setStatus('current')
if mibBuilder.loadTexts: dAspGatewayEntry.setDescription('An entry indicates the information for a protected gateway.')
dAspGatewayIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: dAspGatewayIP.setStatus('current')
if mibBuilder.loadTexts: dAspGatewayIP.setDescription('The gateway IP address of the entry.')
dAspGatewayMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: dAspGatewayMAC.setStatus('current')
if mibBuilder.loadTexts: dAspGatewayMAC.setDescription('The gateway MAC address of the entry.')
dAspActivePortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dAspActivePortList.setStatus('current')
if mibBuilder.loadTexts: dAspActivePortList.setDescription('This object indicates the port-list on which the ARP Spoofing\n            Prevention is active.\n            ')
dAspGatewayRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dAspGatewayRowStatus.setStatus('current')
if mibBuilder.loadTexts: dAspGatewayRowStatus.setDescription('The status of this table entry.')
dAspLoggingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dAspLoggingEnabled.setStatus('current')
if mibBuilder.loadTexts: dAspLoggingEnabled.setDescription("Setting to 'true' to enable ARP spoofing prevention logging feature.\n            Setting the object to 'false' will disable logging feature.")
dAspMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1))
dAspCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1, 1)).setObjects(("DLINKSW-ASP-MIB", "dAspMgtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspCompliance = dAspCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: dAspCompliance.setDescription('The compliance statement for entities which implement the \n            DLINKSW-ASP-MIB.\n            ')
dAspCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1, 2)).setObjects(("DLINKSW-ASP-MIB", "dAspMgtGroup"), ("DLINKSW-ASP-MIB", "dAspLoggingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspCompliance2 = dAspCompliance2.setStatus('current')
if mibBuilder.loadTexts: dAspCompliance2.setDescription('The compliance statement for entities which implement the \n            DLINKSW-ASP-MIB.\n            ')
dAspMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2))
dAspMgtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2, 1)).setObjects(("DLINKSW-ASP-MIB", "dAspActivePortList"), ("DLINKSW-ASP-MIB", "dAspGatewayRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspMgtGroup = dAspMgtGroup.setStatus('current')
if mibBuilder.loadTexts: dAspMgtGroup.setDescription('A collection of objects configures protected gateways for ARP spoofing\n            prevention.\n            ')
dAspLoggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2, 2)).setObjects(("DLINKSW-ASP-MIB", "dAspLoggingEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspLoggingGroup = dAspLoggingGroup.setStatus('current')
if mibBuilder.loadTexts: dAspLoggingGroup.setDescription('A collection of objects configures logging state of ARP spoofing\n            prevention.\n            ')
mibBuilder.exportSymbols("DLINKSW-ASP-MIB", dAspMgtGroup=dAspMgtGroup, dAspGatewayMAC=dAspGatewayMAC, dAspActivePortList=dAspActivePortList, dAspCompliance2=dAspCompliance2, dlinkSwArpSpoofingPreventMIB=dlinkSwArpSpoofingPreventMIB, dAspLoggingGroup=dAspLoggingGroup, dAspGatewayRowStatus=dAspGatewayRowStatus, dAspMIBConformance=dAspMIBConformance, dAspCompliance=dAspCompliance, dAspGatewayIP=dAspGatewayIP, dAspMIBGroups=dAspMIBGroups, PYSNMP_MODULE_ID=dlinkSwArpSpoofingPreventMIB, dAspMIBObjects=dAspMIBObjects, dAspMIBNotifications=dAspMIBNotifications, dAspGatewayTable=dAspGatewayTable, dAspGatewayEntry=dAspGatewayEntry, dAspMIBCompliances=dAspMIBCompliances, dAspLoggingEnabled=dAspLoggingEnabled)
