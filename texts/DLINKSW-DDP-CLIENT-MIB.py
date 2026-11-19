#
# PySNMP MIB module DLINKSW-DDP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-DDP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwDdpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 161))
dlinkSwDdpClientMIB.setRevisions(('2013-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setRevisionsDescriptions((' This is the first version of the MIB file.\n            ',))
if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setLastUpdated('201308050000Z')
if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwDdpClientMIB.setDescription('This MIB module defines objects for D-Link Discovery Protocol client.')
dDdpClientNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 0))
dDdpClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 1))
dDdpClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 2))
dDdpClientCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1))
dDdpClientGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDdpClientGlobalState.setStatus('current')
if mibBuilder.loadTexts: dDdpClientGlobalState.setDescription("This object represents the DDP client's global state\n\t\t        true - Indicates the DDP client is enabled\n\t\t        false - Indicates the DDP client is disabled")
dDdpClientReportTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), )).clone(30)).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDdpClientReportTimer.setStatus('current')
if mibBuilder.loadTexts: dDdpClientReportTimer.setDescription('This object specifies the interval at which DDP report messages are sent\n\t\t\tby the device.\n            Setting the object to 0 prohibits the device from sending DDP report message.')
dDdpClientTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3), )
if mibBuilder.loadTexts: dDdpClientTable.setStatus('current')
if mibBuilder.loadTexts: dDdpClientTable.setDescription('The table contains a list of port-specific information for DDP client.')
dDdpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dDdpClientEntry.setStatus('current')
if mibBuilder.loadTexts: dDdpClientEntry.setDescription('Each entry represents the DDP Client state on a port.')
dDdpClientPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDdpClientPortState.setStatus('current')
if mibBuilder.loadTexts: dDdpClientPortState.setDescription('This object represents the DDP Client state on a port\n\t\t        true - Indicates DDP client is enabled on the port\n\t\t        false - Indicates DDP client is disabled on the port\n\t\t\t\t')
dDdpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 1))
dDdpClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 2))
dDdpClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 1, 1)).setObjects(("DLINKSW-DDP-CLIENT-MIB", "dDdpClientControlGroup"), ("DLINKSW-DDP-CLIENT-MIB", "dDdpClientControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDdpClientCompliance = dDdpClientCompliance.setStatus('current')
if mibBuilder.loadTexts: dDdpClientCompliance.setDescription('The compliance statement for entities which implement the\n            DLINKSW-DDP-CLIENT-MIB.')
dDdpClientControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 2, 1)).setObjects(("DLINKSW-DDP-CLIENT-MIB", "dDdpClientGlobalState"), ("DLINKSW-DDP-CLIENT-MIB", "dDdpClientPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDdpClientControlGroup = dDdpClientControlGroup.setStatus('current')
if mibBuilder.loadTexts: dDdpClientControlGroup.setDescription('A collection of objects providing accessing to global status and report time or the status of a port.')
mibBuilder.exportSymbols("DLINKSW-DDP-CLIENT-MIB", PYSNMP_MODULE_ID=dlinkSwDdpClientMIB, dDdpClientNotifications=dDdpClientNotifications, dDdpClientReportTimer=dDdpClientReportTimer, dDdpClientGlobalState=dDdpClientGlobalState, dDdpClientConformance=dDdpClientConformance, dDdpClientTable=dDdpClientTable, dDdpClientEntry=dDdpClientEntry, dDdpClientGroups=dDdpClientGroups, dDdpClientCtrl=dDdpClientCtrl, dlinkSwDdpClientMIB=dlinkSwDdpClientMIB, dDdpClientObjects=dDdpClientObjects, dDdpClientCompliance=dDdpClientCompliance, dDdpClientControlGroup=dDdpClientControlGroup, dDdpClientCompliances=dDdpClientCompliances, dDdpClientPortState=dDdpClientPortState)
