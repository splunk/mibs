#
# PySNMP MIB module DLINKSW-DDP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-DDP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, NotificationType, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("DLINKSW-DDP-CLIENT-MIB", dDdpClientEntry=dDdpClientEntry, dDdpClientGroups=dDdpClientGroups, dDdpClientCompliances=dDdpClientCompliances, dDdpClientCompliance=dDdpClientCompliance, dDdpClientTable=dDdpClientTable, dDdpClientControlGroup=dDdpClientControlGroup, dDdpClientCtrl=dDdpClientCtrl, dDdpClientNotifications=dDdpClientNotifications, dDdpClientGlobalState=dDdpClientGlobalState, dDdpClientConformance=dDdpClientConformance, dDdpClientPortState=dDdpClientPortState, dDdpClientObjects=dDdpClientObjects, PYSNMP_MODULE_ID=dlinkSwDdpClientMIB, dlinkSwDdpClientMIB=dlinkSwDdpClientMIB, dDdpClientReportTimer=dDdpClientReportTimer)
