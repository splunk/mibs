#
# PySNMP MIB module ALTIGA-GENERAL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-GENERAL-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alGeneralMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alGeneralMibModule")
alStatsGeneral, alGeneralGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsGeneral", "alGeneralGroup")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaGeneralStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2))
altigaGeneralStatsMibModule.setRevisions(('2002-09-11 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setRevisionsDescriptions(('Added module compliance and fix comments.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setLastUpdated('200209111300Z')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setDescription('The Altiga General Statistics MIB models counters and \n          objects that are of management interest.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            AVP:        Attribute/Value Pair\n\n            CLID:       Calling Line ID\n\n            DNIS:       Dialed Number Identification Service\n\n            L2TP:       Layer 2 Tunnel Protocol\n\n            LAC:        L2TP Access Concentrator\n\n            LNS:        L2TP Network Server\n\n            RWS:        Receive Window Size\n         \n         ')
alStatsGeneralGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1))
alGeneralTime = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTime.setStatus('current')
if mibBuilder.loadTexts: alGeneralTime.setDescription("The current time on the box, represented as a time_t.\n\n       In 1.2, this was the box's local time.\n       \n       After 1.2, it was corrected to represent UTC (which is what it\n       is supposed to be). So all boxes should have this be the same \n       value +/- a few seconds.")
alGeneralGaugeCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeCpuUtil.setStatus('current')
if mibBuilder.loadTexts: alGeneralGaugeCpuUtil.setDescription('The value of the CPU Utilization gauge which indicates \n       percentage of CPU utilized.')
alGeneralGaugeActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeActiveSessions.setStatus('current')
if mibBuilder.loadTexts: alGeneralGaugeActiveSessions.setDescription('The value of the Active Sessions gauge which indicates the\n       percentage of total permitted session that are active.')
alGeneralGaugeThroughput = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeThroughput.setStatus('current')
if mibBuilder.loadTexts: alGeneralGaugeThroughput.setDescription('The value of the Throughput gauge which indicates the\n       percentage of total available throughput in-use.')
alGeneralTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTimeZone.setStatus('current')
if mibBuilder.loadTexts: alGeneralTimeZone.setDescription('The time zone configured on the box. Measured in minutes from\n       UTC. e.g. EST = -300.')
altigaGeneralStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1))
altigaGeneralStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1))
altigaGeneralStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1, 1)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "altigaGeneralStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsMibCompliance = altigaGeneralStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaGeneralStatsMibCompliance.setDescription('The compliance statement for agents which implement the\n       Altiga General Statistics MIB.')
altigaGeneralStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 25, 2)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "alGeneralTime"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeCpuUtil"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeActiveSessions"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeThroughput"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsGroup = altigaGeneralStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaGeneralStatsGroup.setDescription('The objects for general information.')
mibBuilder.exportSymbols("ALTIGA-GENERAL-STATS-MIB", alGeneralTimeZone=alGeneralTimeZone, altigaGeneralStatsMibModule=altigaGeneralStatsMibModule, altigaGeneralStatsMibCompliances=altigaGeneralStatsMibCompliances, alGeneralGaugeThroughput=alGeneralGaugeThroughput, altigaGeneralStatsMibConformance=altigaGeneralStatsMibConformance, alStatsGeneralGlobal=alStatsGeneralGlobal, alGeneralGaugeCpuUtil=alGeneralGaugeCpuUtil, altigaGeneralStatsGroup=altigaGeneralStatsGroup, PYSNMP_MODULE_ID=altigaGeneralStatsMibModule, altigaGeneralStatsMibCompliance=altigaGeneralStatsMibCompliance, alGeneralGaugeActiveSessions=alGeneralGaugeActiveSessions, alGeneralTime=alGeneralTime)
