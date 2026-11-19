#
# PySNMP MIB module CISCO-AAA-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-SESSION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TruthValue, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowPointer")
ciscoAAASessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 150))
ciscoAAASessionMIB.setRevisions(('2006-03-21 00:00', '2002-04-11 00:00', '1999-11-16 00:00',))
if mibBuilder.loadTexts: ciscoAAASessionMIB.setLastUpdated('200603210000Z')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setOrganization('Cisco Systems, Inc.')
class CctCallId(TextualConvention, Unsigned32):
    status = 'current'

class CasnSessionId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

casnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1))
casnActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1))
casnGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2))
casnActiveTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableEntries.setStatus('current')
casnActiveTableHighWaterMark = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableHighWaterMark.setStatus('current')
casnActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3), )
if mibBuilder.loadTexts: casnActiveTable.setStatus('current')
casnActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-AAA-SESSION-MIB", "casnSessionId"))
if mibBuilder.loadTexts: casnActiveEntry.setStatus('current')
casnSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 1), CasnSessionId())
if mibBuilder.loadTexts: casnSessionId.setStatus('current')
casnUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnUserId.setStatus('current')
casnIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIpAddr.setStatus('current')
casnIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 4), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIdleTime.setStatus('current')
casnDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: casnDisconnect.setStatus('current')
casnCallTrackerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 6), CctCallId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnCallTrackerId.setStatus('current')
casnNasPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnNasPort.setStatus('current')
casnVaiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnVaiIfIndex.setStatus('current')
casnTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnTotalSessions.setStatus('current')
casnDisconnectedSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnDisconnectedSessions.setStatus('current')
casnMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2))
casnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2, 1))
casnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3))
casnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1))
casnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2))
casnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBCompliance = casnMIBCompliance.setStatus('deprecated')
casnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"), ("CISCO-AAA-SESSION-MIB", "casnActiveGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBComplianceRev1 = casnMIBComplianceRev1.setStatus('current')
casnActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveTableEntries"), ("CISCO-AAA-SESSION-MIB", "casnActiveTableHighWaterMark"), ("CISCO-AAA-SESSION-MIB", "casnUserId"), ("CISCO-AAA-SESSION-MIB", "casnIpAddr"), ("CISCO-AAA-SESSION-MIB", "casnIdleTime"), ("CISCO-AAA-SESSION-MIB", "casnDisconnect"), ("CISCO-AAA-SESSION-MIB", "casnCallTrackerId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroup = casnActiveGroup.setStatus('current')
casnGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnTotalSessions"), ("CISCO-AAA-SESSION-MIB", "casnDisconnectedSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnGeneralGroup = casnGeneralGroup.setStatus('current')
casnActiveGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 3)).setObjects(("CISCO-AAA-SESSION-MIB", "casnNasPort"), ("CISCO-AAA-SESSION-MIB", "casnVaiIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroupSup1 = casnActiveGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SESSION-MIB", ciscoAAASessionMIB=ciscoAAASessionMIB, casnGeneral=casnGeneral, casnActiveTableHighWaterMark=casnActiveTableHighWaterMark, casnSessionId=casnSessionId, casnVaiIfIndex=casnVaiIfIndex, casnDisconnectedSessions=casnDisconnectedSessions, casnMIBNotifications=casnMIBNotifications, casnMIBCompliance=casnMIBCompliance, casnDisconnect=casnDisconnect, casnMIBGroups=casnMIBGroups, casnActiveEntry=casnActiveEntry, casnActiveTableEntries=casnActiveTableEntries, CasnSessionId=CasnSessionId, casnMIBObjects=casnMIBObjects, casnTotalSessions=casnTotalSessions, CctCallId=CctCallId, casnActive=casnActive, casnMIBConformance=casnMIBConformance, casnMIBNotificationPrefix=casnMIBNotificationPrefix, casnMIBCompliances=casnMIBCompliances, casnUserId=casnUserId, casnCallTrackerId=casnCallTrackerId, casnActiveGroup=casnActiveGroup, casnMIBComplianceRev1=casnMIBComplianceRev1, casnActiveGroupSup1=casnActiveGroupSup1, casnActiveTable=casnActiveTable, casnGeneralGroup=casnGeneralGroup, casnIpAddr=casnIpAddr, casnIdleTime=casnIdleTime, casnNasPort=casnNasPort, PYSNMP_MODULE_ID=ciscoAAASessionMIB)
