#
# PySNMP MIB module ALTIGA-VERSION-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-VERSION-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alVersionMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alVersionMibModule")
alStatsVersion, alVersionGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsVersion", "alVersionGroup")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaVersionStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2))
altigaVersionStatsMibModule.setRevisions(('2002-09-05 13:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaVersionStatsMibModule.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaVersionStatsMibModule.setDescription('The Altiga (VPN 3000) Version MIB models counters and\n          objects that are of management interest.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            MIB:        Management Information Base\n\n         ')
alStatsVersionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1))
alVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMajor.setStatus('current')
if mibBuilder.loadTexts: alVersionMajor.setDescription('The major release number of the VPN 3000 software. In the\n       release identifier 1.4.2, the 1 is the major release\n       number.')
alVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionMinor.setStatus('current')
if mibBuilder.loadTexts: alVersionMinor.setDescription('The minor release number of the VPN 3000 software. In the\n       release identifier 1.4.2, the 4 is the minor release\n       number.')
alVersionInt = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionInt.setStatus('current')
if mibBuilder.loadTexts: alVersionInt.setDescription('The integration string of the VPN 3000 software. In the\n       release identifier 1.4.2, the 2 is the patch release\n       number.')
alVersionString = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionString.setStatus('current')
if mibBuilder.loadTexts: alVersionString.setDescription('The string representation of the VPN 3000 software \n       version.')
alVersionLong = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionLong.setStatus('current')
if mibBuilder.loadTexts: alVersionLong.setDescription('The long string representation of the VPN 3000 software\n       version.')
alVersionShort = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionShort.setStatus('current')
if mibBuilder.loadTexts: alVersionShort.setDescription('The short string representation of the VPN3000 software\n       version.')
alVersionBoot = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alVersionBoot.setStatus('current')
if mibBuilder.loadTexts: alVersionBoot.setDescription('The version of the Boot image.')
altigaVersionStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1))
altigaVersionStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1))
altigaVersionStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1, 1)).setObjects(("ALTIGA-VERSION-STATS-MIB", "altigaVersionStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsMibCompliance = altigaVersionStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaVersionStatsMibCompliance.setDescription('The compliance statement for agents which \n       implement the Altiga Version Statistics MIB.')
altigaVersionStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 1, 2)).setObjects(("ALTIGA-VERSION-STATS-MIB", "alVersionMajor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionMinor"), ("ALTIGA-VERSION-STATS-MIB", "alVersionInt"), ("ALTIGA-VERSION-STATS-MIB", "alVersionString"), ("ALTIGA-VERSION-STATS-MIB", "alVersionLong"), ("ALTIGA-VERSION-STATS-MIB", "alVersionShort"), ("ALTIGA-VERSION-STATS-MIB", "alVersionBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaVersionStatsGroup = altigaVersionStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaVersionStatsGroup.setDescription('The objects for the version statistics.')
mibBuilder.exportSymbols("ALTIGA-VERSION-STATS-MIB", alVersionMinor=alVersionMinor, alStatsVersionGlobal=alStatsVersionGlobal, alVersionShort=alVersionShort, altigaVersionStatsMibCompliance=altigaVersionStatsMibCompliance, altigaVersionStatsMibConformance=altigaVersionStatsMibConformance, PYSNMP_MODULE_ID=altigaVersionStatsMibModule, alVersionInt=alVersionInt, altigaVersionStatsGroup=altigaVersionStatsGroup, alVersionString=alVersionString, alVersionBoot=alVersionBoot, altigaVersionStatsMibModule=altigaVersionStatsMibModule, alVersionMajor=alVersionMajor, alVersionLong=alVersionLong, altigaVersionStatsMibCompliances=altigaVersionStatsMibCompliances)
