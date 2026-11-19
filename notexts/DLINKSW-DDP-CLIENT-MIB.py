#
# PySNMP MIB module DLINKSW-DDP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-DDP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, ModuleIdentity, Unsigned32, Gauge32, iso, Bits, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Unsigned32", "Gauge32", "iso", "Bits", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
dlinkSwDdpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 161))
dlinkSwDdpClientMIB.setRevisions(('2013-08-05 00:00',))
if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setLastUpdated('201308050000Z')
if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setOrganization('D-Link Corp.')
dDdpClientNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 0))
dDdpClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 1))
dDdpClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 2))
dDdpClientCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1))
dDdpClientGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDdpClientGlobalState.setStatus('current')
dDdpClientReportTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), )).clone(30)).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDdpClientReportTimer.setStatus('current')
dDdpClientTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3), )
if mibBuilder.loadTexts: dDdpClientTable.setStatus('current')
dDdpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dDdpClientEntry.setStatus('current')
dDdpClientPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDdpClientPortState.setStatus('current')
dDdpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 1))
dDdpClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 2))
dDdpClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 1, 1)).setObjects(("DLINKSW-DDP-CLIENT-MIB", "dDdpClientControlGroup"), ("DLINKSW-DDP-CLIENT-MIB", "dDdpClientControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDdpClientCompliance = dDdpClientCompliance.setStatus('current')
dDdpClientControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 2, 1)).setObjects(("DLINKSW-DDP-CLIENT-MIB", "dDdpClientGlobalState"), ("DLINKSW-DDP-CLIENT-MIB", "dDdpClientPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDdpClientControlGroup = dDdpClientControlGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-DDP-CLIENT-MIB", dDdpClientCompliances=dDdpClientCompliances, dlinkSwDdpClientMIB=dlinkSwDdpClientMIB, PYSNMP_MODULE_ID=dlinkSwDdpClientMIB, dDdpClientCompliance=dDdpClientCompliance, dDdpClientControlGroup=dDdpClientControlGroup, dDdpClientReportTimer=dDdpClientReportTimer, dDdpClientCtrl=dDdpClientCtrl, dDdpClientTable=dDdpClientTable, dDdpClientGroups=dDdpClientGroups, dDdpClientPortState=dDdpClientPortState, dDdpClientObjects=dDdpClientObjects, dDdpClientConformance=dDdpClientConformance, dDdpClientEntry=dDdpClientEntry, dDdpClientNotifications=dDdpClientNotifications, dDdpClientGlobalState=dDdpClientGlobalState)
