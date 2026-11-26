#
# PySNMP MIB module ALTIGA-DNS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-DNS-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
alDnsMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alDnsMibModule")
alDnsGroup, alStatsDns = mibBuilder.importSymbols("ALTIGA-MIB", "alDnsGroup", "alStatsDns")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaDnsStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2))
altigaDnsStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaDnsStatsMibModule.setRevisionsDescriptions(('Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setDescription('The Altiga DNS Statistics MIB models counters and objects that are\n          of management interest for DNS.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            DNS:        Domain Name Service\n\n            MIB:        Management Information Base\n\n         ')
alStatsDnsResolverGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1))
alDnsStatsAttemptedQueries = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsAttemptedQueries.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsAttemptedQueries.setDescription('The number of DNS queries that were attempted.')
alDnsStatsSuccessfulResponses = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsSuccessfulResponses.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsSuccessfulResponses.setDescription('The number of queries that were successfully resolved.')
alDnsStatsTimeoutFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsTimeoutFailures.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsTimeoutFailures.setDescription('The number of failures because there was no response from \n       the server.')
alDnsStatsUnreachableServerFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsUnreachableServerFailures.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsUnreachableServerFailures.setDescription("The number of failures because the address of the server\n       is not reachable according to the Concentrator's routing \n       table.")
alDnsStatsMiscFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsMiscFailures.setStatus('current')
if mibBuilder.loadTexts: alDnsStatsMiscFailures.setDescription('The number of failures for an unspecified reason.')
altigaDnsStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1))
altigaDnsStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1))
altigaDnsStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1, 1)).setObjects(("ALTIGA-DNS-STATS-MIB", "altigaDnsStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsMibCompliance = altigaDnsStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaDnsStatsMibCompliance.setDescription('The compliance statement for agents which \n       implement the Altiga DNS Statistics MIB.')
altigaDnsStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 18, 2)).setObjects(("ALTIGA-DNS-STATS-MIB", "alDnsStatsAttemptedQueries"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsSuccessfulResponses"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsTimeoutFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsUnreachableServerFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsMiscFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsGroup = altigaDnsStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaDnsStatsGroup.setDescription('The objects for the DNS resolver module statistics.')
mibBuilder.exportSymbols("ALTIGA-DNS-STATS-MIB", altigaDnsStatsMibConformance=altigaDnsStatsMibConformance, altigaDnsStatsGroup=altigaDnsStatsGroup, altigaDnsStatsMibModule=altigaDnsStatsMibModule, alDnsStatsUnreachableServerFailures=alDnsStatsUnreachableServerFailures, alDnsStatsAttemptedQueries=alDnsStatsAttemptedQueries, altigaDnsStatsMibCompliances=altigaDnsStatsMibCompliances, PYSNMP_MODULE_ID=altigaDnsStatsMibModule, altigaDnsStatsMibCompliance=altigaDnsStatsMibCompliance, alDnsStatsTimeoutFailures=alDnsStatsTimeoutFailures, alStatsDnsResolverGlobal=alStatsDnsResolverGlobal, alDnsStatsSuccessfulResponses=alDnsStatsSuccessfulResponses, alDnsStatsMiscFailures=alDnsStatsMiscFailures)
