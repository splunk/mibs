#
# PySNMP MIB module CISCO-PRIVATE-VLAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PRIVATE-VLAN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrivateVlanCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 402))
ciscoPrivateVlanCapability.setRevisions(('2004-03-31 00:00',))
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setLastUpdated('200403310000Z')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setOrganization('Cisco Systems, Inc.')
cPrivateVlanCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setStatus('current')
cPrivateVlanCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRIVATE-VLAN-CAPABILITY", cPrivateVlanCapCatOSV08R0101=cPrivateVlanCapCatOSV08R0101, ciscoPrivateVlanCapability=ciscoPrivateVlanCapability, PYSNMP_MODULE_ID=ciscoPrivateVlanCapability, cPrivateVlanCapV12R0111ECat6K=cPrivateVlanCapV12R0111ECat6K)
