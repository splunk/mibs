#
# PySNMP MIB module CISCO-LINK-ERROR-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LINK-ERROR-MONITOR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoLinkErrorMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 426))
ciscoLinkErrorMonitorMIB.setRevisions(('2004-11-19 00:00',))
if mibBuilder.loadTexts: ciscoLinkErrorMonitorMIB.setLastUpdated('200411190000Z')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorMIB.setOrganization('Cisco Systems, Inc.')
ciscoLinkErrMonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 0))
ciscoLinkErrMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 1))
ciscoLinkErrMonMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 2))
clemGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1))
clemInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2))
class ClemCounterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rxcrc", 1), ("txcrc", 2), ("inerrors", 3))

clemEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemEnabled.setStatus('current')
clemSamplingInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemSamplingInterval.setStatus('current')
clemSamplingTimes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemSamplingTimes.setStatus('current')
clemAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("errdisable", 1), ("failover", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemAction.setStatus('current')
clemThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5), )
if mibBuilder.loadTexts: clemThresholdTable.setStatus('current')
clemThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdCounterType"))
if mibBuilder.loadTexts: clemThresholdEntry.setStatus('current')
clemThresholdCounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1, 1), ClemCounterType())
if mibBuilder.loadTexts: clemThresholdCounterType.setStatus('current')
clemThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemThresholdLow.setStatus('current')
clemThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemThresholdHigh.setStatus('current')
clemNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 6), Bits().clone(namedValues=NamedValues(("lowThresholdExceeded", 0), ("highThresholdExceeded", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemNotifEnable.setStatus('current')
clemIfCounterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1), )
if mibBuilder.loadTexts: clemIfCounterTable.setStatus('current')
clemIfCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-LINK-ERROR-MONITOR-MIB", "clemIfCounterType"))
if mibBuilder.loadTexts: clemIfCounterEntry.setStatus('current')
clemIfCounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1, 1, 1), ClemCounterType())
if mibBuilder.loadTexts: clemIfCounterType.setStatus('current')
clemIfCounterEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clemIfCounterEnable.setStatus('current')
clemLowThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 426, 0, 1)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdLow"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clemLowThresholdExceeded.setStatus('current')
clemHighThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 426, 0, 2)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdHigh"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clemHighThresholdExceeded.setStatus('current')
ciscoLinkErrMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 1))
ciscoLinkErrMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2))
ciscoLinkErrMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 1, 1)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemGlobalGroup"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdGroup"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemIfCounterGroup"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemNotificationGroup"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemNotificationControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLinkErrMonMIBCompliance = ciscoLinkErrMonMIBCompliance.setStatus('current')
clemGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 1)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemEnabled"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemSamplingInterval"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemSamplingTimes"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemGlobalGroup = clemGlobalGroup.setStatus('current')
clemThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 2)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdLow"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemThresholdGroup = clemThresholdGroup.setStatus('current')
clemIfCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 3)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemIfCounterEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemIfCounterGroup = clemIfCounterGroup.setStatus('current')
clemNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 4)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemLowThresholdExceeded"), ("CISCO-LINK-ERROR-MONITOR-MIB", "clemHighThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemNotificationGroup = clemNotificationGroup.setStatus('current')
clemNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 5)).setObjects(("CISCO-LINK-ERROR-MONITOR-MIB", "clemNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemNotificationControlGroup = clemNotificationControlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LINK-ERROR-MONITOR-MIB", clemIfCounterEntry=clemIfCounterEntry, clemEnabled=clemEnabled, clemIfCounterGroup=clemIfCounterGroup, clemSamplingInterval=clemSamplingInterval, clemNotifEnable=clemNotifEnable, clemIfCounterType=clemIfCounterType, clemIfCounterEnable=clemIfCounterEnable, ciscoLinkErrMonMIBCompliances=ciscoLinkErrMonMIBCompliances, ciscoLinkErrMonMIBCompliance=ciscoLinkErrMonMIBCompliance, clemNotificationGroup=clemNotificationGroup, clemInterfaceObjects=clemInterfaceObjects, PYSNMP_MODULE_ID=ciscoLinkErrorMonitorMIB, clemThresholdCounterType=clemThresholdCounterType, ciscoLinkErrMonMIBGroups=ciscoLinkErrMonMIBGroups, ciscoLinkErrMonMIBConform=ciscoLinkErrMonMIBConform, clemLowThresholdExceeded=clemLowThresholdExceeded, clemIfCounterTable=clemIfCounterTable, clemThresholdTable=clemThresholdTable, ciscoLinkErrMonMIBObjects=ciscoLinkErrMonMIBObjects, ciscoLinkErrorMonitorMIB=ciscoLinkErrorMonitorMIB, clemThresholdHigh=clemThresholdHigh, ciscoLinkErrMonMIBNotifs=ciscoLinkErrMonMIBNotifs, clemThresholdEntry=clemThresholdEntry, clemGlobalObjects=clemGlobalObjects, ClemCounterType=ClemCounterType, clemAction=clemAction, clemSamplingTimes=clemSamplingTimes, clemThresholdGroup=clemThresholdGroup, clemThresholdLow=clemThresholdLow, clemGlobalGroup=clemGlobalGroup, clemNotificationControlGroup=clemNotificationControlGroup, clemHighThresholdExceeded=clemHighThresholdExceeded)
