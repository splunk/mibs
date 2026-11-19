#
# PySNMP MIB module ALTIGA-SSL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-SSL-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alSslMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alSslMibModule")
alStatsSsl, alSslGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsSsl", "alSslGroup")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaSslStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2))
altigaSslStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaSslStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaSslStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsSslGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1))
alSslStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsTotalSessions.setStatus('current')
alSslStatsActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsActiveSessions.setStatus('current')
alSslStatsMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsMaxSessions.setStatus('current')
alSslStatsPreDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreDecryptOctets.setStatus('current')
alSslStatsPostDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostDecryptOctets.setStatus('current')
alSslStatsPreEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreEncryptOctets.setStatus('current')
alSslStatsPostEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostEncryptOctets.setStatus('current')
altigaSslStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1))
altigaSslStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1))
altigaSslStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1, 1)).setObjects(("ALTIGA-SSL-STATS-MIB", "altigaSslStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsMibCompliance = altigaSslStatsMibCompliance.setStatus('current')
altigaSslStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 26, 2)).setObjects(("ALTIGA-SSL-STATS-MIB", "alSslStatsTotalSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsActiveSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsMaxSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreEncryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostEncryptOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsGroup = altigaSslStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-SSL-STATS-MIB", alStatsSslGlobal=alStatsSslGlobal, altigaSslStatsGroup=altigaSslStatsGroup, altigaSslStatsMibConformance=altigaSslStatsMibConformance, altigaSslStatsMibCompliance=altigaSslStatsMibCompliance, alSslStatsMaxSessions=alSslStatsMaxSessions, alSslStatsTotalSessions=alSslStatsTotalSessions, PYSNMP_MODULE_ID=altigaSslStatsMibModule, alSslStatsPreDecryptOctets=alSslStatsPreDecryptOctets, alSslStatsPostDecryptOctets=alSslStatsPostDecryptOctets, altigaSslStatsMibModule=altigaSslStatsMibModule, alSslStatsPreEncryptOctets=alSslStatsPreEncryptOctets, altigaSslStatsMibCompliances=altigaSslStatsMibCompliances, alSslStatsActiveSessions=alSslStatsActiveSessions, alSslStatsPostEncryptOctets=alSslStatsPostEncryptOctets)
