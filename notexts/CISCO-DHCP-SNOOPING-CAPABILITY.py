#
# PySNMP MIB module CISCO-DHCP-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DHCP-SNOOPING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoDhcpSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 383))
ciscoDhcpSnoopingCapability.setRevisions(('2011-09-28 00:00', '2010-10-27 00:00', '2010-03-18 00:00', '2008-03-20 00:00', '2007-07-02 09:00', '2006-06-28 00:00', '2004-03-09 00:00',))
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setLastUpdated('201109280000Z')
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setOrganization('Cisco Systems, Inc.')
cdsCapabilityV08R0301Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc = cdsCapabilityV08R0301Cat6kPfc.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          of PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc = cdsCapabilityV08R0301Cat6kPfc.setStatus('current')
cdsCapabilityV08R0301Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc3 = cdsCapabilityV08R0301Cat6kPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc3 = cdsCapabilityV08R0301Cat6kPfc3.setStatus('current')
cdsCapabilityV08R0601Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc = cdsCapabilityV08R0601Cat6kPfc.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          or PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc = cdsCapabilityV08R0601Cat6kPfc.setStatus('current')
cdsCapabilityV08R0601Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc3 = cdsCapabilityV08R0601Cat6kPfc3.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc3 = cdsCapabilityV08R0601Cat6kPfc3.setStatus('current')
cdsCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXHPCat6k = cdsCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXHPCat6k = cdsCapV12R0233SXHPCat6k.setStatus('current')
cdsCapabilityV08R0701Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc = cdsCapabilityV08R0701Cat6kPfc.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          or PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc = cdsCapabilityV08R0701Cat6kPfc.setStatus('current')
cdsCapabilityV08R0701Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc3 = cdsCapabilityV08R0701Cat6kPfc3.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc3 = cdsCapabilityV08R0701Cat6kPfc3.setStatus('current')
cdsCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXI4PCat6k = cdsCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXI4PCat6k = cdsCapV12R0233SXI4PCat6k.setStatus('current')
cdsCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0250SYPCat6k = cdsCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0250SYPCat6k = cdsCapV12R0250SYPCat6k.setStatus('current')
cdsCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV15R0001SYPCat6k = cdsCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV15R0001SYPCat6k = cdsCapV15R0001SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-DHCP-SNOOPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoDhcpSnoopingCapability, cdsCapabilityV08R0601Cat6kPfc3=cdsCapabilityV08R0601Cat6kPfc3, cdsCapV12R0233SXI4PCat6k=cdsCapV12R0233SXI4PCat6k, cdsCapabilityV08R0601Cat6kPfc=cdsCapabilityV08R0601Cat6kPfc, cdsCapabilityV08R0301Cat6kPfc3=cdsCapabilityV08R0301Cat6kPfc3, ciscoDhcpSnoopingCapability=ciscoDhcpSnoopingCapability, cdsCapV12R0233SXHPCat6k=cdsCapV12R0233SXHPCat6k, cdsCapabilityV08R0701Cat6kPfc=cdsCapabilityV08R0701Cat6kPfc, cdsCapV15R0001SYPCat6k=cdsCapV15R0001SYPCat6k, cdsCapabilityV08R0301Cat6kPfc=cdsCapabilityV08R0301Cat6kPfc, cdsCapabilityV08R0701Cat6kPfc3=cdsCapabilityV08R0701Cat6kPfc3, cdsCapV12R0250SYPCat6k=cdsCapV12R0250SYPCat6k)
