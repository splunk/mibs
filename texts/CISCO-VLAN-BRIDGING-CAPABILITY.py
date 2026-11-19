#
# PySNMP MIB module CISCO-VLAN-BRIDGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-BRIDGING-CAPABILITY
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
ciscoVlanBridgingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 339))
ciscoVlanBridgingCapability.setRevisions(('2004-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setLastUpdated('200406110000Z')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-vlans@cisco.com')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setDescription('The agent capabilities description of \n                 CISCO-VLAN-BRIDGING-MIB.')
cVlanBridgingCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cVlanBridgingCapCatOSV08R0101.setDescription('CISCO-VLAN-BRIDGING-MIB capabilities.')
cVlanBridgingCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setStatus('current')
if mibBuilder.loadTexts: cVlanBridgingCapCatOSV08R0201.setDescription('CISCO-VLAN-BRIDGING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-CAPABILITY", ciscoVlanBridgingCapability=ciscoVlanBridgingCapability, cVlanBridgingCapCatOSV08R0101=cVlanBridgingCapCatOSV08R0101, cVlanBridgingCapCatOSV08R0201=cVlanBridgingCapCatOSV08R0201, PYSNMP_MODULE_ID=ciscoVlanBridgingCapability)
