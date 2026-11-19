#
# PySNMP MIB module CISCO-IP-NW-DISCOVERY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-NW-DISCOVERY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpNwDiscoveryCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 523))
ciscoIpNwDiscoveryCapability.setRevisions(('2006-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setLastUpdated('200611070000Z')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setDescription('The capabilities description of\n        CISCO-IP-NW-DISCOVERY-MIB.')
cIpNwDiscoverCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 523, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNwDiscoverCapSanOSV30R1MDS9000 = cIpNwDiscoverCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0 on Cisco MDS 9000                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNwDiscoverCapSanOSV30R1MDS9000 = cIpNwDiscoverCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIpNwDiscoverCapSanOSV30R1MDS9000.setDescription('Cisco IP NW Discovery MIB capabilities')
mibBuilder.exportSymbols("CISCO-IP-NW-DISCOVERY-CAPABILITY", ciscoIpNwDiscoveryCapability=ciscoIpNwDiscoveryCapability, PYSNMP_MODULE_ID=ciscoIpNwDiscoveryCapability, cIpNwDiscoverCapSanOSV30R1MDS9000=cIpNwDiscoverCapSanOSV30R1MDS9000)
