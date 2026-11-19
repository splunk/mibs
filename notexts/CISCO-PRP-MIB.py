#
# PySNMP MIB module CISCO-PRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PRP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 866))
ciscoPrpMIB.setRevisions(('2019-09-11 00:00',))
if mibBuilder.loadTexts: ciscoPrpMIB.setLastUpdated('201909110000Z')
if mibBuilder.loadTexts: ciscoPrpMIB.setOrganization('Cisco Systems, Inc.')
class PrpStatus(TextualConvention, Integer32):
    reference = 'Prp channel or LAN status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("stateUp", 1), ("stateDown", 2))

ciscoPrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 0))
ciscoPrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 1))
ciscoPrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2))
ciscoPrpChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1), )
if mibBuilder.loadTexts: ciscoPrpChannelTable.setStatus('current')
ciscoPrpChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1), ).setIndexNames((0, "CISCO-PRP-MIB", "ciscoPrpChannelIndex"))
if mibBuilder.loadTexts: ciscoPrpChannelEntry.setStatus('current')
ciscoPrpChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciscoPrpChannelIndex.setStatus('current')
ciscoPrpChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelId.setStatus('current')
ciscoPrpChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelName.setStatus('current')
ciscoPrpChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 4), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelStatus.setStatus('current')
ciscoPrpChannelLanAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 5), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanAStatus.setStatus('current')
ciscoPrpChannelLanBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 6), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanBStatus.setStatus('current')
ciscoPrpChannelStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"))
if mibBuilder.loadTexts: ciscoPrpChannelStateChange.setStatus('current')
ciscoPrpLanAStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"))
if mibBuilder.loadTexts: ciscoPrpLanAStateChange.setStatus('current')
ciscoPrpLanBStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 3)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"))
if mibBuilder.loadTexts: ciscoPrpLanBStateChange.setStatus('current')
ciscoPrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1))
ciscoPrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2))
ciscoPrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpMIBMainObjectGroup"), ("CISCO-PRP-MIB", "ciscoPrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBCompliance = ciscoPrpMIBCompliance.setStatus('current')
ciscoPrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBMainObjectGroup = ciscoPrpMIBMainObjectGroup.setStatus('current')
ciscoPrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanAStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanBStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBNotificationGroup = ciscoPrpMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRP-MIB", ciscoPrpChannelStateChange=ciscoPrpChannelStateChange, ciscoPrpMIBNotificationGroup=ciscoPrpMIBNotificationGroup, ciscoPrpMIBObjects=ciscoPrpMIBObjects, ciscoPrpChannelEntry=ciscoPrpChannelEntry, ciscoPrpChannelIndex=ciscoPrpChannelIndex, ciscoPrpMIBConform=ciscoPrpMIBConform, ciscoPrpMIB=ciscoPrpMIB, ciscoPrpMIBMainObjectGroup=ciscoPrpMIBMainObjectGroup, ciscoPrpChannelLanBStatus=ciscoPrpChannelLanBStatus, ciscoPrpMIBGroups=ciscoPrpMIBGroups, PrpStatus=PrpStatus, ciscoPrpChannelName=ciscoPrpChannelName, PYSNMP_MODULE_ID=ciscoPrpMIB, ciscoPrpMIBCompliance=ciscoPrpMIBCompliance, ciscoPrpChannelStatus=ciscoPrpChannelStatus, ciscoPrpChannelId=ciscoPrpChannelId, ciscoPrpMIBCompliances=ciscoPrpMIBCompliances, ciscoPrpLanBStateChange=ciscoPrpLanBStateChange, ciscoPrpMIBNotifs=ciscoPrpMIBNotifs, ciscoPrpChannelTable=ciscoPrpChannelTable, ciscoPrpChannelLanAStatus=ciscoPrpChannelLanAStatus, ciscoPrpLanAStateChange=ciscoPrpLanAStateChange)
