#
# PySNMP MIB module CISCO-SWITCH-USAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-USAGE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchUsageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 201))
ciscoSwitchUsageMIB.setRevisions(('2001-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setLastUpdated('200105020000Z')
if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-switch-usage-mib@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setDescription('This MIB defines objects related to statistics \n                for the usage of switch fabric. The switch fabric\n                is used by the incoming packets from the line/network\n                to a interface. Such packets are called ingress packets.\n                Counters are maintained for number of ingress packets/\n                octets switched by the switch fabric for each \n                interface.\n                NOTE: These counters are not counting the total number \n                of incoming packets and octets for a particular \n                interface. Instead only the counts of packets and \n                octets that actually use the switch-fabric are being\n                accounted for by this MIB.  Therefore, the counters in \n                this MIB are distinctly different from packet and octet \n                counters found in the IF-MIB.')
ciscoSwitchUsageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 1))
ciscoSwitchUsageStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1))
cswitchUsageStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1), )
if mibBuilder.loadTexts: cswitchUsageStatTable.setStatus('current')
if mibBuilder.loadTexts: cswitchUsageStatTable.setDescription('A list of switch resouce usage statistics \n                entries. The statistics will give information \n                on the switch usage by each interface.')
cswitchUsageStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cswitchUsageStatEntry.setStatus('current')
if mibBuilder.loadTexts: cswitchUsageStatEntry.setDescription('Entry contains information of a particular \n                interface in terms of how much switch resource \n                it has used.\n                An entry in this table exists for each ifEntry \n                with an ifType of fastEther(62) for FastEthernet\n                interface and gigabitEthernet (117) for Gigabit\n                interface.')
cswitchUsageByIngrsIntfPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfPkts.setStatus('current')
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfPkts.setDescription('The number of ingress packets of a interface \n                which use the switch resource.')
cswitchUsageByIngrsIntfHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfHCPkts.setStatus('current')
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfHCPkts.setDescription('The number of ingress packets of a interface\n                which use the switch resource.\n\n                This is a 64 bit (High Capacity) version of\n                the cswitchUsageByIngrsIntfPkts counter for\n                use with SNMP v2c or v3 Managers.')
cswitchUsageByIngrsIntfOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfOctets.setStatus('current')
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfOctets.setDescription('The number of ingress octets of a interface \n                which use the switch resource.')
cswitchUsageByIngrsIntfHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfHCOctets.setStatus('current')
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfHCOctets.setDescription('The number of ingress octets of a interface\n                which use the switch resource.\n                This is a 64 bit (High Capacity) version of\n                the cswitchUsageByIngrsIntfOctets counter for\n                use with SNMP v2c or v3 Managers.')
ciscoSwitchUsageMIBNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 2))
ciscoSwitchUsageMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 2, 0))
ciscoSwitchUsageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 3))
ciscoSwitchUsageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 1))
ciscoSwitchUsageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 2))
ciscoSwitchUsageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 1, 1)).setObjects(("CISCO-SWITCH-USAGE-MIB", "ciscoSwitchUsageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchUsageMIBCompliance = ciscoSwitchUsageMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchUsageMIBCompliance.setDescription('The compliance statement for the switch usage \n                statistics group.')
ciscoSwitchUsageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 2, 1)).setObjects(("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfPkts"), ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfHCPkts"), ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfOctets"), ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchUsageMIBGroup = ciscoSwitchUsageMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchUsageMIBGroup.setDescription('The Object Group for switch usage statistics')
mibBuilder.exportSymbols("CISCO-SWITCH-USAGE-MIB", ciscoSwitchUsageMIBGroup=ciscoSwitchUsageMIBGroup, cswitchUsageStatEntry=cswitchUsageStatEntry, ciscoSwitchUsageMIBNotifications=ciscoSwitchUsageMIBNotifications, cswitchUsageStatTable=cswitchUsageStatTable, ciscoSwitchUsageMIBCompliance=ciscoSwitchUsageMIBCompliance, PYSNMP_MODULE_ID=ciscoSwitchUsageMIB, ciscoSwitchUsageMIB=ciscoSwitchUsageMIB, ciscoSwitchUsageMIBConformance=ciscoSwitchUsageMIBConformance, cswitchUsageByIngrsIntfHCOctets=cswitchUsageByIngrsIntfHCOctets, ciscoSwitchUsageStats=ciscoSwitchUsageStats, cswitchUsageByIngrsIntfPkts=cswitchUsageByIngrsIntfPkts, cswitchUsageByIngrsIntfHCPkts=cswitchUsageByIngrsIntfHCPkts, ciscoSwitchUsageMIBGroups=ciscoSwitchUsageMIBGroups, ciscoSwitchUsageMIBCompliances=ciscoSwitchUsageMIBCompliances, ciscoSwitchUsageMIBObjects=ciscoSwitchUsageMIBObjects, cswitchUsageByIngrsIntfOctets=cswitchUsageByIngrsIntfOctets, ciscoSwitchUsageMIBNotifyPrefix=ciscoSwitchUsageMIBNotifyPrefix)
