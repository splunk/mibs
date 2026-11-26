#
# PySNMP MIB module CISCO-ENTITY-PFE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-PFE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
ciscoEntityPfeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 265))
ciscoEntityPfeMib.setRevisions(('2002-11-27 16:00',))
if mibBuilder.loadTexts: ciscoEntityPfeMib.setLastUpdated('200211271600Z')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setOrganization('Cisco System, Inc.')
class CurrentUtilization(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class CurrentEfficiency(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class IntervalUtilization(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class IntervalEfficiency(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class TotalUtilization(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class TotalEfficiency(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class Percentage(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class EventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("log", 2), ("notify", 3), ("logAndNotify", 4))

class HistEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("thldUtilizationEvent", 1), ("thldEfficiencyEvent", 2), ("thld1MinUtilizationEvent", 3), ("thld1MinEfficiencyEvent", 4), ("thld5MinUtilizationEvent", 5), ("thld5MinEfficiencyEvent", 6), ("restartEvent", 7))

cePfeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 0))
cePfeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1))
cePfeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2))
cePfePerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1))
cePfeHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2))
cePfePerfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1), )
if mibBuilder.loadTexts: cePfePerfConfigTable.setStatus('current')
cePfePerfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cePfePerfConfigEntry.setStatus('current')
cePfePerfConfigTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfConfigTimeElapsed.setStatus('current')
cePfePerfConfigValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfConfigValidIntervals.setStatus('current')
cePfePerfConfigThldUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 3), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThldUtilization.setStatus('current')
cePfePerfConfigThldEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 4), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThldEfficiency.setStatus('current')
cePfePerfConfigThld1MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 5), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld1MinUtilization.setStatus('current')
cePfePerfConfigThld1MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 6), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld1MinEfficiency.setStatus('current')
cePfePerfConfigThld5MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 7), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld5MinUtilization.setStatus('current')
cePfePerfConfigThld5MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 8), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld5MinEfficiency.setStatus('current')
cePfePerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2), )
if mibBuilder.loadTexts: cePfePerfCurrentTable.setStatus('current')
cePfePerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1), )
cePfePerfConfigEntry.registerAugmentions(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEntry"))
cePfePerfCurrentEntry.setIndexNames(*cePfePerfConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cePfePerfCurrentEntry.setStatus('current')
cePfePerfCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 1), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrentUtilization.setStatus('current')
cePfePerfCurrentEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 2), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrentEfficiency.setStatus('current')
cePfePerfCurrent1MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 3), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent1MinUtilization.setStatus('current')
cePfePerfCurrent1MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 4), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent1MinEfficiency.setStatus('current')
cePfePerfCurrent5MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 5), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent5MinUtilization.setStatus('current')
cePfePerfCurrent5MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 6), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent5MinEfficiency.setStatus('current')
cePfePerfIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3), )
if mibBuilder.loadTexts: cePfePerfIntervalTable.setStatus('current')
cePfePerfIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalNumber"))
if mibBuilder.loadTexts: cePfePerfIntervalEntry.setStatus('current')
cePfePerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: cePfePerfIntervalNumber.setStatus('current')
cePfePerfIntervalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 2), IntervalUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfIntervalUtilization.setStatus('current')
cePfePerfIntervalEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 3), IntervalEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfIntervalEfficiency.setStatus('current')
cePfePerfTotalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4), )
if mibBuilder.loadTexts: cePfePerfTotalTable.setStatus('current')
cePfePerfTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cePfePerfTotalEntry.setStatus('current')
cePfePerfTotalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 1), TotalUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfTotalUtilization.setStatus('current')
cePfePerfTotalEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 2), TotalEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfTotalEfficiency.setStatus('current')
cePfeHistNotifiesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 1), EventType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfeHistNotifiesEnable.setStatus('current')
cePfeHistTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfeHistTableSize.setStatus('current')
cePfeHistTableLastIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistTableLastIndex.setStatus('current')
cePfeHistTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4), )
if mibBuilder.loadTexts: cePfeHistTable.setStatus('current')
cePfeHistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-ENTITY-PFE-MIB", "cePfeHistIndex"))
if mibBuilder.loadTexts: cePfeHistEntry.setStatus('current')
cePfeHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cePfeHistIndex.setStatus('current')
cePfeHistEntPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 2), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistEntPhysIndex.setStatus('current')
cePfeHistType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 3), HistEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistType.setStatus('current')
cePfeHistThld = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 4), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistThld.setStatus('current')
cePfeHistValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistValue.setStatus('current')
cePfeHistRestartReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistRestartReason.setStatus('current')
cePfeHistTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistTimeStamp.setStatus('current')
cePfeHistThldEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"))
if mibBuilder.loadTexts: cePfeHistThldEvent.setStatus('current')
cePfeHistRestartEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 2)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"))
if mibBuilder.loadTexts: cePfeHistRestartEvent.setStatus('current')
cePfeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1))
cePfeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2))
cePfeMIBPerformanceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeMIBPerformanceGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBCurrentGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBHistGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBHistEventGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBIntervalGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBTotalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBPerformanceCompliance = cePfeMIBPerformanceCompliance.setStatus('current')
cePfeMIBPerformanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistTableSize"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistTableLastIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistNotifiesEnable"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigTimeElapsed"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigValidIntervals"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBPerformanceGroup = cePfeMIBPerformanceGroup.setStatus('current')
cePfeMIBCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 2)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBCurrentGroup = cePfeMIBCurrentGroup.setStatus('current')
cePfeMIBIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 3)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBIntervalGroup = cePfeMIBIntervalGroup.setStatus('current')
cePfeMIBTotalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 4)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBTotalGroup = cePfeMIBTotalGroup.setStatus('current')
cePfeMIBHistGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 5)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBHistGroup = cePfeMIBHistGroup.setStatus('current')
cePfeMIBHistEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 6)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistThldEvent"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBHistEventGroup = cePfeMIBHistEventGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PFE-MIB", cePfePerfCurrent1MinEfficiency=cePfePerfCurrent1MinEfficiency, cePfePerfConfigTable=cePfePerfConfigTable, cePfeMIBCurrentGroup=cePfeMIBCurrentGroup, cePfePerfTotalTable=cePfePerfTotalTable, cePfeMIBTotalGroup=cePfeMIBTotalGroup, cePfePerfTotalUtilization=cePfePerfTotalUtilization, TotalEfficiency=TotalEfficiency, cePfePerfTotalEntry=cePfePerfTotalEntry, cePfeMIBObjects=cePfeMIBObjects, cePfePerfIntervalUtilization=cePfePerfIntervalUtilization, cePfePerfIntervalNumber=cePfePerfIntervalNumber, cePfePerfTotalEfficiency=cePfePerfTotalEfficiency, cePfeHistEntry=cePfeHistEntry, cePfePerfConfigThldEfficiency=cePfePerfConfigThldEfficiency, cePfePerfCurrentEntry=cePfePerfCurrentEntry, cePfeMIBCompliances=cePfeMIBCompliances, cePfePerfIntervalTable=cePfePerfIntervalTable, cePfePerfIntervalEfficiency=cePfePerfIntervalEfficiency, cePfeHistRestartReason=cePfeHistRestartReason, cePfePerfCurrent1MinUtilization=cePfePerfCurrent1MinUtilization, cePfeMIBHistEventGroup=cePfeMIBHistEventGroup, ciscoEntityPfeMib=ciscoEntityPfeMib, cePfePerfCurrentUtilization=cePfePerfCurrentUtilization, CurrentUtilization=CurrentUtilization, cePfeMIBIntervalGroup=cePfeMIBIntervalGroup, cePfeMIBPerformanceCompliance=cePfeMIBPerformanceCompliance, cePfeMIBHistGroup=cePfeMIBHistGroup, cePfePerfConfigTimeElapsed=cePfePerfConfigTimeElapsed, cePfePerfCurrent5MinUtilization=cePfePerfCurrent5MinUtilization, cePfeHistEntPhysIndex=cePfeHistEntPhysIndex, cePfePerfConfigThld5MinUtilization=cePfePerfConfigThld5MinUtilization, PYSNMP_MODULE_ID=ciscoEntityPfeMib, cePfePerformance=cePfePerformance, IntervalEfficiency=IntervalEfficiency, cePfePerfConfigThld1MinUtilization=cePfePerfConfigThld1MinUtilization, cePfePerfCurrentEfficiency=cePfePerfCurrentEfficiency, cePfeHistThld=cePfeHistThld, cePfeHistRestartEvent=cePfeHistRestartEvent, CurrentEfficiency=CurrentEfficiency, cePfeHistThldEvent=cePfeHistThldEvent, cePfePerfConfigThld1MinEfficiency=cePfePerfConfigThld1MinEfficiency, cePfeHistType=cePfeHistType, TotalUtilization=TotalUtilization, cePfePerfConfigThldUtilization=cePfePerfConfigThldUtilization, cePfePerfCurrent5MinEfficiency=cePfePerfCurrent5MinEfficiency, cePfeHistNotifiesEnable=cePfeHistNotifiesEnable, EventType=EventType, cePfeHistValue=cePfeHistValue, Percentage=Percentage, IntervalUtilization=IntervalUtilization, cePfeMIBNotifications=cePfeMIBNotifications, cePfePerfIntervalEntry=cePfePerfIntervalEntry, cePfeHistTableSize=cePfeHistTableSize, cePfeMIBPerformanceGroup=cePfeMIBPerformanceGroup, cePfeHistTable=cePfeHistTable, cePfeMIBConformance=cePfeMIBConformance, cePfePerfCurrentTable=cePfePerfCurrentTable, cePfeMIBGroups=cePfeMIBGroups, cePfeHistTableLastIndex=cePfeHistTableLastIndex, cePfeHistTimeStamp=cePfeHistTimeStamp, cePfeHistory=cePfeHistory, HistEventType=HistEventType, cePfeHistIndex=cePfeHistIndex, cePfePerfConfigValidIntervals=cePfePerfConfigValidIntervals, cePfePerfConfigEntry=cePfePerfConfigEntry, cePfePerfConfigThld5MinEfficiency=cePfePerfConfigThld5MinEfficiency)
