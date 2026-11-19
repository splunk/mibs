#
# PySNMP MIB module ALTIGA-EVENT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-EVENT-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alEventMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alEventMibModule")
alEventGroup, alStatsEvent = mibBuilder.importSymbols("ALTIGA-MIB", "alEventGroup", "alStatsEvent")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaEventStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2))
altigaEventStatsMibModule.setRevisions(('2003-01-13 00:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaEventStatsMibModule.setRevisionsDescriptions(('Added alStatsEventNotificationId object', 'Updated with new header',))
if mibBuilder.loadTexts: altigaEventStatsMibModule.setLastUpdated('200301130000Z')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setDescription('The Altiga Event Statistics MIB models counters and objects that are\n          of management interest for events.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            MIB:        Management Information Base\n\n         ')
alStatsEventGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1))
alStatsEventNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alStatsEventNotificationId.setStatus('current')
if mibBuilder.loadTexts: alStatsEventNotificationId.setDescription('The event class and event ID string in class/id format.\n       The string applies as the product is configured to\n       send log events whenever SNMP generates notifications.')
alEventStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2), )
if mibBuilder.loadTexts: alEventStatsTable.setStatus('current')
if mibBuilder.loadTexts: alEventStatsTable.setDescription('The Event Stats Per Class/Event Number.')
alEventStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1), ).setIndexNames((0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"))
if mibBuilder.loadTexts: alEventStatsEntry.setStatus('current')
if mibBuilder.loadTexts: alEventStatsEntry.setDescription('An entry in the alEventStatsTable.')
alEventStatsClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsClass.setStatus('current')
if mibBuilder.loadTexts: alEventStatsClass.setDescription('The primary index of this row, the event class.')
alEventStatsEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsEventNumber.setStatus('current')
if mibBuilder.loadTexts: alEventStatsEventNumber.setDescription('The secondary index of this row, the event number.')
alEventStatsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsCount.setStatus('current')
if mibBuilder.loadTexts: alEventStatsCount.setDescription('The number of times that the given event for the give class has\n       been generated.')
altigaEventStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1))
altigaEventStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1))
altigaEventStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 1)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibCompliance = altigaEventStatsMibCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: altigaEventStatsMibCompliance.setDescription('The compliance statement for agents which \n       implement the Altiga Event Statistics MIB.')
altigaEventStatsMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibComplianceRev1 = altigaEventStatsMibComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: altigaEventStatsMibComplianceRev1.setDescription('The compliance statement for agents which \n        implement the Altiga Event Statistics MIB.')
altigaEventStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroup = altigaEventStatsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: altigaEventStatsGroup.setDescription('The objects for Event Statistics.')
altigaEventStatsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 3)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"), ("ALTIGA-EVENT-STATS-MIB", "alStatsEventNotificationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroupRev1 = altigaEventStatsGroupRev1.setStatus('current')
if mibBuilder.loadTexts: altigaEventStatsGroupRev1.setDescription('The objects for Event Statistics.')
mibBuilder.exportSymbols("ALTIGA-EVENT-STATS-MIB", alEventStatsTable=alEventStatsTable, alStatsEventGlobal=alStatsEventGlobal, altigaEventStatsMibModule=altigaEventStatsMibModule, alEventStatsEventNumber=alEventStatsEventNumber, altigaEventStatsMibCompliances=altigaEventStatsMibCompliances, altigaEventStatsMibConformance=altigaEventStatsMibConformance, alEventStatsCount=alEventStatsCount, PYSNMP_MODULE_ID=altigaEventStatsMibModule, altigaEventStatsGroupRev1=altigaEventStatsGroupRev1, alStatsEventNotificationId=alStatsEventNotificationId, alEventStatsEntry=alEventStatsEntry, alEventStatsClass=alEventStatsClass, altigaEventStatsGroup=altigaEventStatsGroup, altigaEventStatsMibCompliance=altigaEventStatsMibCompliance, altigaEventStatsMibComplianceRev1=altigaEventStatsMibComplianceRev1)
