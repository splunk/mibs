#
# PySNMP MIB module CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
cSwitchHwCapacityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 572))
cSwitchHwCapacityCapability.setRevisions(('2014-03-03 00:01', '2013-07-26 00:01', '2013-07-16 00:01', '2011-09-28 00:01', '2008-10-29 00:00',))
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setLastUpdated('201403030001Z')
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setOrganization('Cisco Systems, Inc.')
cSwitchHwCapacityCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV12R0233SXIPCat6k = cSwitchHwCapacityCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV12R0233SXIPCat6k = cSwitchHwCapacityCapV12R0233SXIPCat6k.setStatus('current')
cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                         series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setStatus('current')
cSwitchHwCapacityCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0104PN7k = cSwitchHwCapacityCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0104PN7k = cSwitchHwCapacityCapNxOSV06R0104PN7k.setStatus('current')
cSwitchHwCapacityCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0202PN7k = cSwitchHwCapacityCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0202PN7k = cSwitchHwCapacityCapNxOSV06R0202PN7k.setStatus('current')
cSwitchHwCapacityCapNxOSV06R0208PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0208PN7k = cSwitchHwCapacityCapNxOSV06R0208PN7k.setProductRelease('Cisco NX-OS 6.2(8) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0208PN7k = cSwitchHwCapacityCapNxOSV06R0208PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY", cSwitchHwCapacityCapV15R0001SYPCat6kSup2T=cSwitchHwCapacityCapV15R0001SYPCat6kSup2T, PYSNMP_MODULE_ID=cSwitchHwCapacityCapability, cSwitchHwCapacityCapV12R0233SXIPCat6k=cSwitchHwCapacityCapV12R0233SXIPCat6k, cSwitchHwCapacityCapNxOSV06R0104PN7k=cSwitchHwCapacityCapNxOSV06R0104PN7k, cSwitchHwCapacityCapNxOSV06R0202PN7k=cSwitchHwCapacityCapNxOSV06R0202PN7k, cSwitchHwCapacityCapability=cSwitchHwCapacityCapability, cSwitchHwCapacityCapNxOSV06R0208PN7k=cSwitchHwCapacityCapNxOSV06R0208PN7k)
