#
# PySNMP MIB module ALTIGA-IP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ALTIGA-IP-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
alIpMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alIpMibModule")
alStatsIp, alIpGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsIp", "alIpGroup")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaIpStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2))
altigaIpStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaIpStatsMibModule.setRevisionsDescriptions(('Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaIpStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setDescription('The Altiga IP Statistics MIB models counters and objects that are\n          of management interest for IP.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            IP:         Internet Protocol\n\n            LAN:        Local-Area Network \n\n            MIB:        Management Information Base\n\n         ')
alStatsIpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1))
alIpInterfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1), )
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setDescription('IP Interface Statistics table.')
alIpInterfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1), ).setIndexNames((0, "ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"))
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setDescription('An entry in the alIpInterfaceStatsTable.')
alIpInterfaceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setDescription('The ifIndex of this row.')
alIpInterfaceStatsCurrentDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("full", 2), ("half", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setDescription('The current LAN duplex mode for this interface.')
altigaIpStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1))
altigaIpStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1))
altigaIpStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1, 1)).setObjects(("ALTIGA-IP-STATS-MIB", "altigaIpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsMibCompliance = altigaIpStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaIpStatsMibCompliance.setDescription('The compliance statement for agents which \n       implement the Altiga IP Statistics MIB.')
altigaIpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 8, 2)).setObjects(("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"), ("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsCurrentDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsGroup = altigaIpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaIpStatsGroup.setDescription('The objects for Ip Statistics.')
mibBuilder.exportSymbols("ALTIGA-IP-STATS-MIB", alStatsIpGlobal=alStatsIpGlobal, PYSNMP_MODULE_ID=altigaIpStatsMibModule, altigaIpStatsGroup=altigaIpStatsGroup, alIpInterfaceStatsTable=alIpInterfaceStatsTable, alIpInterfaceStatsCurrentDuplex=alIpInterfaceStatsCurrentDuplex, altigaIpStatsMibCompliances=altigaIpStatsMibCompliances, altigaIpStatsMibCompliance=altigaIpStatsMibCompliance, altigaIpStatsMibModule=altigaIpStatsMibModule, alIpInterfaceStatsEntry=alIpInterfaceStatsEntry, alIpInterfaceStatsIndex=alIpInterfaceStatsIndex, altigaIpStatsMibConformance=altigaIpStatsMibConformance)
