#
# PySNMP MIB module CISCO-OSCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-OSCP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
ciscoOscpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 202))
ciscoOscpMIB.setRevisions(('2001-05-18 00:00',))
if mibBuilder.loadTexts: ciscoOscpMIB.setLastUpdated('200105180000Z')
if mibBuilder.loadTexts: ciscoOscpMIB.setOrganization('Cisco Systems, Inc.')
ciscoOscpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 1))
class CoscpSwitchId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CoscpPortId(TextualConvention, Unsigned32):
    status = 'current'

class CoscpBundleId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CoscpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("version1", 2))

ciscoOscpBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1))
coscpHighestVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 1), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpHighestVersion.setStatus('current')
coscpLowestVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 2), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLowestVersion.setStatus('current')
coscpSwitchId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 3), CoscpSwitchId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpSwitchId.setStatus('current')
coscpPriorityChangeMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("immediate", 1), ("delayed", 2))).clone('immediate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpPriorityChangeMode.setStatus('current')
coscpHelloHoldDown = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloHoldDown.setStatus('current')
coscpHelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(150, 30000)).clone(3000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloInterval.setStatus('current')
coscpHelloInactivityFactor = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 50)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloInactivityFactor.setStatus('current')
coscpNotifiesEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpNotifiesEnabled.setStatus('current')
coscpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2), )
if mibBuilder.loadTexts: coscpLinkTable.setStatus('current')
coscpLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1), ).setIndexNames((0, "CISCO-OSCP-MIB", "coscpLinkPortId"))
if mibBuilder.loadTexts: coscpLinkEntry.setStatus('current')
coscpLinkPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 1), CoscpPortId())
if mibBuilder.loadTexts: coscpLinkPortId.setStatus('current')
coscpLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("dedicatedWavelength", 2), ("inBand", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkType.setStatus('current')
coscpLinkVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 3), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkVersion.setStatus('current')
coscpLinkHelloState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("attempt", 2), ("oneWay", 3), ("twoWay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkHelloState.setStatus('current')
coscpLinkRemoteSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 5), CoscpSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkRemoteSwitchId.setStatus('current')
coscpLinkRemotePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 6), CoscpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkRemotePortId.setStatus('current')
coscpLinkDerivedBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 7), CoscpBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkDerivedBundleId.setStatus('current')
coscpLinkConfigBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 8), CoscpBundleId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpLinkConfigBundleId.setStatus('current')
coscpLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkIfIndex.setStatus('current')
coscpLinkSelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpLinkSelPriority.setStatus('current')
coscpLinkInHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkInHellos.setStatus('current')
coscpLinkInDiscardedHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkInDiscardedHellos.setStatus('current')
coscpLinkOutHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkOutHellos.setStatus('current')
coscpLinkTransDown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkTransDown.setStatus('current')
coscpBundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3), )
if mibBuilder.loadTexts: coscpBundleTable.setStatus('current')
coscpBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1), ).setIndexNames((0, "CISCO-OSCP-MIB", "coscpBundleRemoteSwitchId"), (0, "CISCO-OSCP-MIB", "coscpBundleId"))
if mibBuilder.loadTexts: coscpBundleEntry.setStatus('current')
coscpBundleRemoteSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 1), CoscpSwitchId())
if mibBuilder.loadTexts: coscpBundleRemoteSwitchId.setStatus('current')
coscpBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 2), CoscpBundleId())
if mibBuilder.loadTexts: coscpBundleId.setStatus('current')
coscpBundleActivePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 3), CoscpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundleActivePortId.setStatus('current')
coscpBundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundleIfIndex.setStatus('current')
coscpBundlePortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundlePortCount.setStatus('current')
coscpBundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: coscpBundleRowStatus.setStatus('current')
ciscoOscpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 2))
ciscoOscpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0))
coscpNotifyTransDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0, 1)).setObjects(("CISCO-OSCP-MIB", "coscpLinkTransDown"))
if mibBuilder.loadTexts: coscpNotifyTransDown.setStatus('current')
ciscoOscpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3))
ciscoOscpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1))
ciscoOscpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2))
ciscoOscpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1, 1)).setObjects(("CISCO-OSCP-MIB", "ciscoOscpBasicGroup"), ("CISCO-OSCP-MIB", "ciscoOscpNotificationsGroup"), ("CISCO-OSCP-MIB", "ciscoOscpBundleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpMIBCompliance = ciscoOscpMIBCompliance.setStatus('current')
ciscoOscpBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 1)).setObjects(("CISCO-OSCP-MIB", "coscpHighestVersion"), ("CISCO-OSCP-MIB", "coscpLowestVersion"), ("CISCO-OSCP-MIB", "coscpSwitchId"), ("CISCO-OSCP-MIB", "coscpHelloHoldDown"), ("CISCO-OSCP-MIB", "coscpHelloInterval"), ("CISCO-OSCP-MIB", "coscpHelloInactivityFactor"), ("CISCO-OSCP-MIB", "coscpNotifiesEnabled"), ("CISCO-OSCP-MIB", "coscpLinkType"), ("CISCO-OSCP-MIB", "coscpLinkVersion"), ("CISCO-OSCP-MIB", "coscpLinkHelloState"), ("CISCO-OSCP-MIB", "coscpLinkRemoteSwitchId"), ("CISCO-OSCP-MIB", "coscpLinkRemotePortId"), ("CISCO-OSCP-MIB", "coscpLinkIfIndex"), ("CISCO-OSCP-MIB", "coscpLinkInHellos"), ("CISCO-OSCP-MIB", "coscpLinkInDiscardedHellos"), ("CISCO-OSCP-MIB", "coscpLinkOutHellos"), ("CISCO-OSCP-MIB", "coscpLinkTransDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpBasicGroup = ciscoOscpBasicGroup.setStatus('current')
ciscoOscpBundleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 2)).setObjects(("CISCO-OSCP-MIB", "coscpPriorityChangeMode"), ("CISCO-OSCP-MIB", "coscpLinkDerivedBundleId"), ("CISCO-OSCP-MIB", "coscpLinkConfigBundleId"), ("CISCO-OSCP-MIB", "coscpLinkSelPriority"), ("CISCO-OSCP-MIB", "coscpBundleActivePortId"), ("CISCO-OSCP-MIB", "coscpBundleIfIndex"), ("CISCO-OSCP-MIB", "coscpBundlePortCount"), ("CISCO-OSCP-MIB", "coscpBundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpBundleGroup = ciscoOscpBundleGroup.setStatus('current')
ciscoOscpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 3)).setObjects(("CISCO-OSCP-MIB", "coscpNotifyTransDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpNotificationsGroup = ciscoOscpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OSCP-MIB", coscpLinkHelloState=coscpLinkHelloState, coscpBundleRowStatus=coscpBundleRowStatus, ciscoOscpMIBNotifications=ciscoOscpMIBNotifications, ciscoOscpMIBConformance=ciscoOscpMIBConformance, coscpLinkConfigBundleId=coscpLinkConfigBundleId, coscpBundleRemoteSwitchId=coscpBundleRemoteSwitchId, ciscoOscpNotificationsGroup=ciscoOscpNotificationsGroup, ciscoOscpMIBObjects=ciscoOscpMIBObjects, coscpHighestVersion=coscpHighestVersion, coscpLinkOutHellos=coscpLinkOutHellos, coscpLinkTransDown=coscpLinkTransDown, coscpBundleTable=coscpBundleTable, ciscoOscpNotificationsPrefix=ciscoOscpNotificationsPrefix, coscpNotifyTransDown=coscpNotifyTransDown, ciscoOscpMIBGroups=ciscoOscpMIBGroups, ciscoOscpBundleGroup=ciscoOscpBundleGroup, coscpLowestVersion=coscpLowestVersion, ciscoOscpMIBCompliance=ciscoOscpMIBCompliance, coscpHelloInterval=coscpHelloInterval, coscpBundleEntry=coscpBundleEntry, coscpHelloInactivityFactor=coscpHelloInactivityFactor, coscpNotifiesEnabled=coscpNotifiesEnabled, coscpBundleId=coscpBundleId, PYSNMP_MODULE_ID=ciscoOscpMIB, coscpBundlePortCount=coscpBundlePortCount, ciscoOscpMIBCompliances=ciscoOscpMIBCompliances, coscpPriorityChangeMode=coscpPriorityChangeMode, coscpLinkPortId=coscpLinkPortId, coscpLinkRemotePortId=coscpLinkRemotePortId, coscpBundleActivePortId=coscpBundleActivePortId, coscpLinkType=coscpLinkType, coscpLinkIfIndex=coscpLinkIfIndex, ciscoOscpBasicGroup=ciscoOscpBasicGroup, coscpLinkSelPriority=coscpLinkSelPriority, coscpLinkTable=coscpLinkTable, coscpLinkVersion=coscpLinkVersion, CoscpSwitchId=CoscpSwitchId, ciscoOscpMIB=ciscoOscpMIB, coscpLinkInDiscardedHellos=coscpLinkInDiscardedHellos, coscpLinkRemoteSwitchId=coscpLinkRemoteSwitchId, coscpBundleIfIndex=coscpBundleIfIndex, CoscpPortId=CoscpPortId, ciscoOscpBaseGroup=ciscoOscpBaseGroup, coscpLinkEntry=coscpLinkEntry, coscpLinkDerivedBundleId=coscpLinkDerivedBundleId, coscpLinkInHellos=coscpLinkInHellos, coscpSwitchId=coscpSwitchId, coscpHelloHoldDown=coscpHelloHoldDown, CoscpVersion=CoscpVersion, CoscpBundleId=CoscpBundleId)
