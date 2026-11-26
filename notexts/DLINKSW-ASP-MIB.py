#
# PySNMP MIB module DLINKSW-ASP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-ASP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, MacAddress, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus", "TruthValue")
dlinkSwArpSpoofingPreventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 76))
dlinkSwArpSpoofingPreventMIB.setRevisions(('2016-07-05 00:00', '2013-07-18 00:00',))
if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setLastUpdated('201607050000Z')
if mibBuilder.loadTexts: dlinkSwArpSpoofingPreventMIB.setOrganization('D-Link Corp.')
dAspMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 0))
dAspMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 1))
dAspMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 2))
dAspGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1), )
if mibBuilder.loadTexts: dAspGatewayTable.setStatus('current')
dAspGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1), ).setIndexNames((0, "DLINKSW-ASP-MIB", "dAspGatewayIP"), (0, "DLINKSW-ASP-MIB", "dAspGatewayMAC"))
if mibBuilder.loadTexts: dAspGatewayEntry.setStatus('current')
dAspGatewayIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: dAspGatewayIP.setStatus('current')
dAspGatewayMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: dAspGatewayMAC.setStatus('current')
dAspActivePortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dAspActivePortList.setStatus('current')
dAspGatewayRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dAspGatewayRowStatus.setStatus('current')
dAspLoggingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dAspLoggingEnabled.setStatus('current')
dAspMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1))
dAspCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1, 1)).setObjects(("DLINKSW-ASP-MIB", "dAspMgtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspCompliance = dAspCompliance.setStatus('deprecated')
dAspCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1, 2)).setObjects(("DLINKSW-ASP-MIB", "dAspMgtGroup"), ("DLINKSW-ASP-MIB", "dAspLoggingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspCompliance2 = dAspCompliance2.setStatus('current')
dAspMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2))
dAspMgtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2, 1)).setObjects(("DLINKSW-ASP-MIB", "dAspActivePortList"), ("DLINKSW-ASP-MIB", "dAspGatewayRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspMgtGroup = dAspMgtGroup.setStatus('current')
dAspLoggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2, 2)).setObjects(("DLINKSW-ASP-MIB", "dAspLoggingEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAspLoggingGroup = dAspLoggingGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-ASP-MIB", dAspActivePortList=dAspActivePortList, dAspMIBGroups=dAspMIBGroups, dAspMIBConformance=dAspMIBConformance, dAspGatewayRowStatus=dAspGatewayRowStatus, dAspLoggingGroup=dAspLoggingGroup, dAspGatewayEntry=dAspGatewayEntry, dAspMIBCompliances=dAspMIBCompliances, dAspGatewayIP=dAspGatewayIP, dAspMIBObjects=dAspMIBObjects, PYSNMP_MODULE_ID=dlinkSwArpSpoofingPreventMIB, dAspCompliance2=dAspCompliance2, dAspCompliance=dAspCompliance, dAspGatewayMAC=dAspGatewayMAC, dAspLoggingEnabled=dAspLoggingEnabled, dlinkSwArpSpoofingPreventMIB=dlinkSwArpSpoofingPreventMIB, dAspGatewayTable=dAspGatewayTable, dAspMIBNotifications=dAspMIBNotifications, dAspMgtGroup=dAspMgtGroup)
