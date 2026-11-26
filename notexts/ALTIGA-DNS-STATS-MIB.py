#
# PySNMP MIB module ALTIGA-DNS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-DNS-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
alDnsMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alDnsMibModule")
alDnsGroup, alStatsDns = mibBuilder.importSymbols("ALTIGA-MIB", "alDnsGroup", "alStatsDns")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaDnsStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2))
altigaDnsStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsDnsResolverGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1))
alDnsStatsAttemptedQueries = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsAttemptedQueries.setStatus('current')
alDnsStatsSuccessfulResponses = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsSuccessfulResponses.setStatus('current')
alDnsStatsTimeoutFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsTimeoutFailures.setStatus('current')
alDnsStatsUnreachableServerFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsUnreachableServerFailures.setStatus('current')
alDnsStatsMiscFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsMiscFailures.setStatus('current')
altigaDnsStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1))
altigaDnsStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1))
altigaDnsStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1, 1)).setObjects(("ALTIGA-DNS-STATS-MIB", "altigaDnsStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsMibCompliance = altigaDnsStatsMibCompliance.setStatus('current')
altigaDnsStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 18, 2)).setObjects(("ALTIGA-DNS-STATS-MIB", "alDnsStatsAttemptedQueries"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsSuccessfulResponses"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsTimeoutFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsUnreachableServerFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsMiscFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsGroup = altigaDnsStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-DNS-STATS-MIB", alStatsDnsResolverGlobal=alStatsDnsResolverGlobal, altigaDnsStatsMibCompliance=altigaDnsStatsMibCompliance, altigaDnsStatsMibConformance=altigaDnsStatsMibConformance, alDnsStatsSuccessfulResponses=alDnsStatsSuccessfulResponses, altigaDnsStatsMibModule=altigaDnsStatsMibModule, alDnsStatsUnreachableServerFailures=alDnsStatsUnreachableServerFailures, alDnsStatsAttemptedQueries=alDnsStatsAttemptedQueries, altigaDnsStatsGroup=altigaDnsStatsGroup, PYSNMP_MODULE_ID=altigaDnsStatsMibModule, alDnsStatsTimeoutFailures=alDnsStatsTimeoutFailures, alDnsStatsMiscFailures=alDnsStatsMiscFailures, altigaDnsStatsMibCompliances=altigaDnsStatsMibCompliances)
