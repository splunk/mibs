#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-QOS-POLICY-CONFIG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosPolicyConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 363))
ciscoQosPolicyConfigCapability.setRevisions(('2007-06-28 00:00', '2003-10-20 00:00',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setLastUpdated('200706280000Z')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setOrganization('Cisco Systems, Inc.')
cqpcCapabilityCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setStatus('current')
cqpcCapabilityV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-CAPABILITY", cqpcCapabilityV12R0233SXHPCat6k=cqpcCapabilityV12R0233SXHPCat6k, cqpcCapabilityCatOSV08R0101Cat6k=cqpcCapabilityCatOSV08R0101Cat6k, PYSNMP_MODULE_ID=ciscoQosPolicyConfigCapability, ciscoQosPolicyConfigCapability=ciscoQosPolicyConfigCapability)
