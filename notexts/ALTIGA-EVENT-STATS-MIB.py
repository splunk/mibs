#
# PySNMP MIB module ALTIGA-EVENT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-EVENT-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alEventMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alEventMibModule")
alEventGroup, alStatsEvent = mibBuilder.importSymbols("ALTIGA-MIB", "alEventGroup", "alStatsEvent")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaEventStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2))
altigaEventStatsMibModule.setRevisions(('2003-01-13 00:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaEventStatsMibModule.setLastUpdated('200301130000Z')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsEventGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1))
alStatsEventNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alStatsEventNotificationId.setStatus('current')
alEventStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2), )
if mibBuilder.loadTexts: alEventStatsTable.setStatus('current')
alEventStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1), ).setIndexNames((0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"))
if mibBuilder.loadTexts: alEventStatsEntry.setStatus('current')
alEventStatsClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsClass.setStatus('current')
alEventStatsEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsEventNumber.setStatus('current')
alEventStatsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsCount.setStatus('current')
altigaEventStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1))
altigaEventStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1))
altigaEventStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 1)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibCompliance = altigaEventStatsMibCompliance.setStatus('deprecated')
altigaEventStatsMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibComplianceRev1 = altigaEventStatsMibComplianceRev1.setStatus('current')
altigaEventStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroup = altigaEventStatsGroup.setStatus('deprecated')
altigaEventStatsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 3)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"), ("ALTIGA-EVENT-STATS-MIB", "alStatsEventNotificationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroupRev1 = altigaEventStatsGroupRev1.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-EVENT-STATS-MIB", alEventStatsEntry=alEventStatsEntry, altigaEventStatsMibCompliances=altigaEventStatsMibCompliances, altigaEventStatsMibComplianceRev1=altigaEventStatsMibComplianceRev1, PYSNMP_MODULE_ID=altigaEventStatsMibModule, alEventStatsCount=alEventStatsCount, alEventStatsEventNumber=alEventStatsEventNumber, altigaEventStatsMibModule=altigaEventStatsMibModule, altigaEventStatsMibConformance=altigaEventStatsMibConformance, alEventStatsTable=alEventStatsTable, alEventStatsClass=alEventStatsClass, altigaEventStatsMibCompliance=altigaEventStatsMibCompliance, altigaEventStatsGroupRev1=altigaEventStatsGroupRev1, alStatsEventNotificationId=alStatsEventNotificationId, altigaEventStatsGroup=altigaEventStatsGroup, alStatsEventGlobal=alStatsEventGlobal)
