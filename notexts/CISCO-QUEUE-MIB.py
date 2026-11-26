#
# PySNMP MIB module CISCO-QUEUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-QUEUE-MIB
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
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQueueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 37))
ciscoQueueMIB.setRevisions(('1995-08-21 00:00',))
if mibBuilder.loadTexts: ciscoQueueMIB.setLastUpdated('9505310000Z')
if mibBuilder.loadTexts: ciscoQueueMIB.setOrganization('Cisco Systems, Inc.')
ciscoQueueObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 1))
ciscoQueueTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 2))
ciscoQueueConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3))
class CQAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fifo", 1), ("priority", 2), ("custom", 3), ("weightedFair", 4))

cQIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1), )
if mibBuilder.loadTexts: cQIfTable.setStatus('current')
cQIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cQIfEntry.setStatus('current')
cQIfQType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 1), CQAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfQType.setStatus('current')
cQIfTxLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfTxLimit.setStatus('current')
cQIfSubqueues = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfSubqueues.setStatus('current')
cQStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2), )
if mibBuilder.loadTexts: cQStatsTable.setStatus('current')
cQStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"))
if mibBuilder.loadTexts: cQStatsEntry.setStatus('current')
cQStatsQNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cQStatsQNumber.setStatus('current')
cQStatsDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsDepth.setStatus('current')
cQStatsMaxDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsMaxDepth.setStatus('current')
cQStatsDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsDiscards.setStatus('current')
cQRotationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3), )
if mibBuilder.loadTexts: cQRotationTable.setStatus('current')
cQRotationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"))
if mibBuilder.loadTexts: cQRotationEntry.setStatus('current')
cQRotationOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQRotationOctets.setStatus('current')
cQCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1))
cQGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2))
cQCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1, 1)).setObjects(("CISCO-QUEUE-MIB", "cQIfGroup"), ("CISCO-QUEUE-MIB", "cQStatsGroup"), ("CISCO-QUEUE-MIB", "cQRotationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQCompliance = cQCompliance.setStatus('current')
cQIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 1)).setObjects(("CISCO-QUEUE-MIB", "cQIfQType"), ("CISCO-QUEUE-MIB", "cQIfTxLimit"), ("CISCO-QUEUE-MIB", "cQIfSubqueues"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQIfGroup = cQIfGroup.setStatus('current')
cQStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 2)).setObjects(("CISCO-QUEUE-MIB", "cQStatsDepth"), ("CISCO-QUEUE-MIB", "cQStatsMaxDepth"), ("CISCO-QUEUE-MIB", "cQStatsDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQStatsGroup = cQStatsGroup.setStatus('current')
cQRotationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 3)).setObjects(("CISCO-QUEUE-MIB", "cQRotationOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQRotationGroup = cQRotationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QUEUE-MIB", ciscoQueueMIB=ciscoQueueMIB, cQGroups=cQGroups, cQIfSubqueues=cQIfSubqueues, cQRotationOctets=cQRotationOctets, ciscoQueueConformance=ciscoQueueConformance, ciscoQueueTraps=ciscoQueueTraps, cQCompliances=cQCompliances, cQRotationGroup=cQRotationGroup, cQIfTxLimit=cQIfTxLimit, cQStatsEntry=cQStatsEntry, cQRotationTable=cQRotationTable, cQStatsMaxDepth=cQStatsMaxDepth, cQCompliance=cQCompliance, cQIfTable=cQIfTable, cQIfEntry=cQIfEntry, cQStatsGroup=cQStatsGroup, CQAlgorithm=CQAlgorithm, cQIfQType=cQIfQType, PYSNMP_MODULE_ID=ciscoQueueMIB, cQStatsTable=cQStatsTable, cQRotationEntry=cQRotationEntry, cQIfGroup=cQIfGroup, cQStatsDiscards=cQStatsDiscards, ciscoQueueObjects=ciscoQueueObjects, cQStatsDepth=cQStatsDepth, cQStatsQNumber=cQStatsQNumber)
