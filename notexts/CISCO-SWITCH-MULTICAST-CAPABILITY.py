#
# PySNMP MIB module CISCO-SWITCH-MULTICAST-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-MULTICAST-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchMulticastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 546))
ciscoSwitchMulticastCapability.setRevisions(('2010-11-11 00:00', '2008-10-30 00:00', '2007-07-16 00:00',))
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setLastUpdated('201011110000Z')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setOrganization('Cisco Systems, Inc.')
cswmCapabilityV12R0219SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setStatus('current')
cswmCapabilityV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setStatus('current')
cswmCapabilityV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-MULTICAST-CAPABILITY", cswmCapabilityV12R0233SXIPCat6k=cswmCapabilityV12R0233SXIPCat6k, ciscoSwitchMulticastCapability=ciscoSwitchMulticastCapability, cswmCapabilityV12R0219SXHPCat6k=cswmCapabilityV12R0219SXHPCat6k, PYSNMP_MODULE_ID=ciscoSwitchMulticastCapability, cswmCapabilityV12R0250SYPCat6kPfc4=cswmCapabilityV12R0250SYPCat6kPfc4)
