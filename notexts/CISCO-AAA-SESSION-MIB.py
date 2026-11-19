#
# PySNMP MIB module CISCO-AAA-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-SESSION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-AAA-SESSION-MIB", casnMIBObjects=casnMIBObjects, casnMIBGroups=casnMIBGroups, casnMIBCompliances=casnMIBCompliances, casnActive=casnActive, casnMIBConformance=casnMIBConformance, PYSNMP_MODULE_ID=ciscoAAASessionMIB, casnNasPort=casnNasPort, casnActiveTable=casnActiveTable, casnIdleTime=casnIdleTime, casnActiveTableHighWaterMark=casnActiveTableHighWaterMark, casnVaiIfIndex=casnVaiIfIndex, casnMIBComplianceRev1=casnMIBComplianceRev1, casnIpAddr=casnIpAddr, casnMIBCompliance=casnMIBCompliance, casnUserId=casnUserId, CctCallId=CctCallId, casnActiveEntry=casnActiveEntry, casnTotalSessions=casnTotalSessions, casnActiveGroup=casnActiveGroup, casnGeneralGroup=casnGeneralGroup, casnSessionId=casnSessionId, casnGeneral=casnGeneral, ciscoAAASessionMIB=ciscoAAASessionMIB, casnDisconnect=casnDisconnect, casnCallTrackerId=casnCallTrackerId, casnMIBNotificationPrefix=casnMIBNotificationPrefix, CasnSessionId=CasnSessionId, casnActiveTableEntries=casnActiveTableEntries, casnActiveGroupSup1=casnActiveGroupSup1, casnMIBNotifications=casnMIBNotifications, casnDisconnectedSessions=casnDisconnectedSessions)
