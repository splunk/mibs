#
# PySNMP MIB module ALTIGA-VERSION-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-VERSION-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alVersionMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alVersionMibModule")
alStatsVersion, alVersionGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsVersion", "alVersionGroup")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaVersionStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2))
altigaVersionStatsMibModule.setRevisions(('2002-09-05 13:00',))
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsVersionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1))
alVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMajor.setStatus('current')
alVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMinor.setStatus('current')
alVersionInt = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionInt.setStatus('current')
alVersionString = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionString.setStatus('current')
alVersionLong = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionLong.setStatus('current')
alVersionShort = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionShort.setStatus('current')
alVersionBoot = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionBoot.setStatus('current')
altigaVersionStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1))
altigaVersionStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1))
altigaVersionStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1, 1)).setObjects(("ALTIGA-VERSION-STATS-MIB", "altigaVersionStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsMibCompliance = altigaVersionStatsMibCompliance.setStatus('current')
altigaVersionStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 1, 2)).setObjects(("ALTIGA-VERSION-STATS-MIB", "alVersionMajor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionMinor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionInt"), ("ALTIGA-VERSION-STATS-MIB", "alVersionString"), ("ALTIGA-VERSION-STATS-MIB", "alVersionLong"), ("ALTIGA-VERSION-STATS-MIB", "alVersionShort"), ("ALTIGA-VERSION-STATS-MIB", "alVersionBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsGroup = altigaVersionStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-VERSION-STATS-MIB", PYSNMP_MODULE_ID=altigaVersionStatsMibModule, altigaVersionStatsMibModule=altigaVersionStatsMibModule, alVersionString=alVersionString, altigaVersionStatsMibConformance=altigaVersionStatsMibConformance, altigaVersionStatsMibCompliance=altigaVersionStatsMibCompliance, altigaVersionStatsMibCompliances=altigaVersionStatsMibCompliances, alVersionMajor=alVersionMajor, alVersionLong=alVersionLong, alVersionMinor=alVersionMinor, alVersionInt=alVersionInt, altigaVersionStatsGroup=altigaVersionStatsGroup, alStatsVersionGlobal=alStatsVersionGlobal, alVersionShort=alVersionShort, alVersionBoot=alVersionBoot)
