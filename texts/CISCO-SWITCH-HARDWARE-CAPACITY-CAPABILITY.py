#
# PySNMP MIB module CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cSwitchHwCapacityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 572))
cSwitchHwCapacityCapability.setRevisions(('2014-03-03 00:01', '2013-07-26 00:01', '2013-07-16 00:01', '2011-09-28 00:01', '2008-10-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setRevisionsDescriptions(('Add agent capability statement\n        cSwitchHwCapacityCapNxOSV06R0208PN7k.', 'Add agent capability statement\n        cSwitchHwCapacityCapNxOSV06R0202PN7k.', 'Add agent capability statement\n        cSwitchHwCapacityCapNxOSV06R0104PN7k.', 'Add agent capability statement\n        cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setLastUpdated('201403030001Z')
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setDescription('The capabilities description of\n        CISCO-SWITCH-HARDWARE-CAPACITY-MIB.')
cSwitchHwCapacityCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV12R0233SXIPCat6k = cSwitchHwCapacityCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV12R0233SXIPCat6k = cSwitchHwCapacityCapV12R0233SXIPCat6k.setStatus('current')
if mibBuilder.loadTexts: cSwitchHwCapacityCapV12R0233SXIPCat6k.setDescription('CISCO-SWITCH-HARDWARE-CAPACITY-MIB\n        capabilities.')
cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                         series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setDescription('CISCO-SWITCH-HARDWARE-CAPACITY-MIB\n        capabilities.')
cSwitchHwCapacityCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0104PN7k = cSwitchHwCapacityCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0104PN7k = cSwitchHwCapacityCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: cSwitchHwCapacityCapNxOSV06R0104PN7k.setDescription('CISCO-SWITCH-HARDWARE-CAPACITY-MIB agent capabilities.')
cSwitchHwCapacityCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0202PN7k = cSwitchHwCapacityCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0202PN7k = cSwitchHwCapacityCapNxOSV06R0202PN7k.setStatus('current')
if mibBuilder.loadTexts: cSwitchHwCapacityCapNxOSV06R0202PN7k.setDescription('CISCO-SWITCH-HARDWARE-CAPACITY-MIB agent capabilities.')
cSwitchHwCapacityCapNxOSV06R0208PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0208PN7k = cSwitchHwCapacityCapNxOSV06R0208PN7k.setProductRelease('Cisco NX-OS 6.2(8) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0208PN7k = cSwitchHwCapacityCapNxOSV06R0208PN7k.setStatus('current')
if mibBuilder.loadTexts: cSwitchHwCapacityCapNxOSV06R0208PN7k.setDescription('CISCO-SWITCH-HARDWARE-CAPACITY-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY", cSwitchHwCapacityCapV12R0233SXIPCat6k=cSwitchHwCapacityCapV12R0233SXIPCat6k, PYSNMP_MODULE_ID=cSwitchHwCapacityCapability, cSwitchHwCapacityCapNxOSV06R0104PN7k=cSwitchHwCapacityCapNxOSV06R0104PN7k, cSwitchHwCapacityCapNxOSV06R0208PN7k=cSwitchHwCapacityCapNxOSV06R0208PN7k, cSwitchHwCapacityCapNxOSV06R0202PN7k=cSwitchHwCapacityCapNxOSV06R0202PN7k, cSwitchHwCapacityCapability=cSwitchHwCapacityCapability, cSwitchHwCapacityCapV15R0001SYPCat6kSup2T=cSwitchHwCapacityCapV15R0001SYPCat6kSup2T)
