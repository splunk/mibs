#
# PySNMP MIB module CISCO-SWITCH-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-QOS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
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
ciscoSwitchQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 541))
ciscoSwitchQosCapability.setRevisions(('2014-10-03 00:00', '2014-04-03 00:00', '2013-10-16 00:00', '2011-09-26 00:00', '2010-11-17 00:00', '2010-03-19 00:00', '2008-06-04 00:00', '2007-06-29 00:00',))
if mibBuilder.loadTexts: ciscoSwitchQosCapability.setLastUpdated('201410030000Z')
if mibBuilder.loadTexts: ciscoSwitchQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoSwitchQosCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXHPCat6k = ciscoSwitchQosCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXHPCat6k = ciscoSwitchQosCapV12R0233SXHPCat6k.setStatus('current')
ciscoSwitchQosCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXIPCat6k = ciscoSwitchQosCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXIPCat6k = ciscoSwitchQosCapV12R0233SXIPCat6k.setStatus('current')
ciscoSwitchQosCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXI4PCat6k = ciscoSwitchQosCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXI4PCat6k = ciscoSwitchQosCapV12R0233SXI4PCat6k.setStatus('current')
ciscoSwitchQosCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0250SYPCat6k = ciscoSwitchQosCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0250SYPCat6k = ciscoSwitchQosCapV12R0250SYPCat6k.setStatus('current')
ciscoSwitchQosCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV15R0001SYPCat6k = ciscoSwitchQosCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV15R0001SYPCat6k = ciscoSwitchQosCapV15R0001SYPCat6k.setStatus('current')
ciscoSwitchQosCapV5R0003U0501gPN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV5R0003U0501gPN3K = ciscoSwitchQosCapV5R0003U0501gPN3K.setProductRelease('Cisco NX-OS 5.0(3)U5(1g) on Nexus 3000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV5R0003U0501gPN3K = ciscoSwitchQosCapV5R0003U0501gPN3K.setStatus('current')
ciscoSwitchQosCapV6R0002U0101PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV6R0002U0101PN3K = ciscoSwitchQosCapV6R0002U0101PN3K.setProductRelease('Cisco NX-OS 6.0(2)U1(1) on Nexus 3000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV6R0002U0101PN3K = ciscoSwitchQosCapV6R0002U0101PN3K.setStatus('current')
ciscoSwitchQosCapV06R0002U0201PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV06R0002U0201PN3K = ciscoSwitchQosCapV06R0002U0201PN3K.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus 3000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV06R0002U0201PN3K = ciscoSwitchQosCapV06R0002U0201PN3K.setStatus('current')
ciscoSwitchQosCapNxOSV06R0210PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapNxOSV06R0210PN7K = ciscoSwitchQosCapNxOSV06R0210PN7K.setProductRelease('Cisco NX-OS 6.2(10) on Nexus 7000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapNxOSV06R0210PN7K = ciscoSwitchQosCapNxOSV06R0210PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-QOS-CAPABILITY", ciscoSwitchQosCapV6R0002U0101PN3K=ciscoSwitchQosCapV6R0002U0101PN3K, ciscoSwitchQosCapV12R0250SYPCat6k=ciscoSwitchQosCapV12R0250SYPCat6k, ciscoSwitchQosCapV12R0233SXI4PCat6k=ciscoSwitchQosCapV12R0233SXI4PCat6k, ciscoSwitchQosCapability=ciscoSwitchQosCapability, ciscoSwitchQosCapNxOSV06R0210PN7K=ciscoSwitchQosCapNxOSV06R0210PN7K, ciscoSwitchQosCapV5R0003U0501gPN3K=ciscoSwitchQosCapV5R0003U0501gPN3K, ciscoSwitchQosCapV12R0233SXHPCat6k=ciscoSwitchQosCapV12R0233SXHPCat6k, PYSNMP_MODULE_ID=ciscoSwitchQosCapability, ciscoSwitchQosCapV06R0002U0201PN3K=ciscoSwitchQosCapV06R0002U0201PN3K, ciscoSwitchQosCapV12R0233SXIPCat6k=ciscoSwitchQosCapV12R0233SXIPCat6k, ciscoSwitchQosCapV15R0001SYPCat6k=ciscoSwitchQosCapV15R0001SYPCat6k)
