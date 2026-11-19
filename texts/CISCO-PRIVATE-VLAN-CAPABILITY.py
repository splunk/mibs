#
# PySNMP MIB module CISCO-PRIVATE-VLAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PRIVATE-VLAN-CAPABILITY
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
ciscoPrivateVlanCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 402))
ciscoPrivateVlanCapability.setRevisions(('2004-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setLastUpdated('200403310000Z')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setDescription('The capabilities description of\n                CISCO-PRIVATE-VLAN-MIB.')
cPrivateVlanCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setStatus('current')
if mibBuilder.loadTexts: cPrivateVlanCapV12R0111ECat6K.setDescription('CISCO-PRIVATE-VLAN-MIB capabilities.')
cPrivateVlanCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cPrivateVlanCapCatOSV08R0101.setDescription('CISCO-PRIVATE-VLAN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PRIVATE-VLAN-CAPABILITY", PYSNMP_MODULE_ID=ciscoPrivateVlanCapability, cPrivateVlanCapV12R0111ECat6K=cPrivateVlanCapV12R0111ECat6K, cPrivateVlanCapCatOSV08R0101=cPrivateVlanCapCatOSV08R0101, ciscoPrivateVlanCapability=ciscoPrivateVlanCapability)
