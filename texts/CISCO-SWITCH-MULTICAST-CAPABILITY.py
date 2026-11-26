#
# PySNMP MIB module CISCO-SWITCH-MULTICAST-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-MULTICAST-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchMulticastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 546))
ciscoSwitchMulticastCapability.setRevisions(('2010-11-11 00:00', '2008-10-30 00:00', '2007-07-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setRevisionsDescriptions(('Added capability statement\n        cswmCapabilityV12R0250SYPCat6kPfc4.', 'Added capability statement\n        cswmCapabilityV12R0233SXIPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setLastUpdated('201011110000Z')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setDescription('The capabilities description of\n        CISCO-SWITCH-MULTICAST-MIB.')
cswmCapabilityV12R0219SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cswmCapabilityV12R0219SXHPCat6k.setDescription('CISCO-SWITCH-MULTICAST-MIB capabilities.')
cswmCapabilityV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setStatus('current')
if mibBuilder.loadTexts: cswmCapabilityV12R0233SXIPCat6k.setDescription('CISCO-SWITCH-MULTICAST-MIB capabilities.')
cswmCapabilityV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: cswmCapabilityV12R0250SYPCat6kPfc4.setDescription('CISCO-SWITCH-MULTICAST-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-MULTICAST-CAPABILITY", cswmCapabilityV12R0250SYPCat6kPfc4=cswmCapabilityV12R0250SYPCat6kPfc4, cswmCapabilityV12R0219SXHPCat6k=cswmCapabilityV12R0219SXHPCat6k, cswmCapabilityV12R0233SXIPCat6k=cswmCapabilityV12R0233SXIPCat6k, PYSNMP_MODULE_ID=ciscoSwitchMulticastCapability, ciscoSwitchMulticastCapability=ciscoSwitchMulticastCapability)
