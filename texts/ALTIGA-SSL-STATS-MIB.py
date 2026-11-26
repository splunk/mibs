#
# PySNMP MIB module ALTIGA-SSL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-SSL-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:43 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
alSslMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alSslMibModule")
alSslGroup, alStatsSsl = mibBuilder.importSymbols("ALTIGA-MIB", "alSslGroup", "alStatsSsl")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaSslStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2))
altigaSslStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaSslStatsMibModule.setRevisionsDescriptions(('Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaSslStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaSslStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaSslStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaSslStatsMibModule.setDescription('The Altiga SSL Statistics MIB models counters and objects that are\n          of management interest for SSL.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            MIB:        Management Information Base\n\n            SSL:        Secure Sockets Layer\n\n         ')
alStatsSslGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1))
alSslStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsTotalSessions.setStatus('current')
if mibBuilder.loadTexts: alSslStatsTotalSessions.setDescription('The number of total sessions.')
alSslStatsActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsActiveSessions.setStatus('current')
if mibBuilder.loadTexts: alSslStatsActiveSessions.setDescription('The current number of active sessions.')
alSslStatsMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsMaxSessions.setStatus('current')
if mibBuilder.loadTexts: alSslStatsMaxSessions.setDescription('The maximum number current of active sessions at \n      any one time.')
alSslStatsPreDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreDecryptOctets.setStatus('current')
if mibBuilder.loadTexts: alSslStatsPreDecryptOctets.setDescription('The number of octets sent to the decryption engine. Includes \n      octets used as part of negotiation.')
alSslStatsPostDecryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostDecryptOctets.setStatus('current')
if mibBuilder.loadTexts: alSslStatsPostDecryptOctets.setDescription('The number of octets received from the decryption engine.')
alSslStatsPreEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPreEncryptOctets.setStatus('current')
if mibBuilder.loadTexts: alSslStatsPreEncryptOctets.setDescription('The number of octets send to the encryption engine.')
alSslStatsPostEncryptOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 26, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alSslStatsPostEncryptOctets.setStatus('current')
if mibBuilder.loadTexts: alSslStatsPostEncryptOctets.setDescription('The number of octets received from the encryption engine.\n      Includes octets used as part of negitiation.')
altigaSslStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1))
altigaSslStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1))
altigaSslStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31, 2, 1, 1, 1)).setObjects(("ALTIGA-SSL-STATS-MIB", "altigaSslStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsMibCompliance = altigaSslStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaSslStatsMibCompliance.setDescription('The compliance statement for agents which \n       implement the Altiga SSL Statistics MIB.')
altigaSslStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 26, 2)).setObjects(("ALTIGA-SSL-STATS-MIB", "alSslStatsTotalSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsActiveSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsMaxSessions"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostDecryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPreEncryptOctets"), ("ALTIGA-SSL-STATS-MIB", "alSslStatsPostEncryptOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaSslStatsGroup = altigaSslStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaSslStatsGroup.setDescription('The objects for SSL statistics.')
mibBuilder.exportSymbols("ALTIGA-SSL-STATS-MIB", altigaSslStatsMibCompliance=altigaSslStatsMibCompliance, alSslStatsPostDecryptOctets=alSslStatsPostDecryptOctets, alSslStatsTotalSessions=alSslStatsTotalSessions, alSslStatsPostEncryptOctets=alSslStatsPostEncryptOctets, altigaSslStatsMibModule=altigaSslStatsMibModule, altigaSslStatsMibConformance=altigaSslStatsMibConformance, alSslStatsActiveSessions=alSslStatsActiveSessions, alStatsSslGlobal=alStatsSslGlobal, alSslStatsPreEncryptOctets=alSslStatsPreEncryptOctets, altigaSslStatsGroup=altigaSslStatsGroup, alSslStatsPreDecryptOctets=alSslStatsPreDecryptOctets, PYSNMP_MODULE_ID=altigaSslStatsMibModule, altigaSslStatsMibCompliances=altigaSslStatsMibCompliances, alSslStatsMaxSessions=alSslStatsMaxSessions)
