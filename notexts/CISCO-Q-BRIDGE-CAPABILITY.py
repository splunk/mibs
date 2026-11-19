#
# PySNMP MIB module CISCO-Q-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-Q-BRIDGE-CAPABILITY
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
ciscoQBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 389))
ciscoQBridgeCapability.setRevisions(('2011-09-27 00:00', '2011-07-27 00:00', '2008-10-28 00:00', '2004-01-15 00:00',))
if mibBuilder.loadTexts: ciscoQBridgeCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setOrganization('Cisco Systems, Inc.')
ciscoQBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setStatus('current')
ciscoQBridgeCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setStatus('current')
ciscoQBridgeCapNxOSV05R0201PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setStatus('current')
ciscoQBridgeCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-Q-BRIDGE-CAPABILITY", ciscoQBridgeCapV12R0233SXIPCat6K=ciscoQBridgeCapV12R0233SXIPCat6K, ciscoQBridgeCapV15R0001SYPCat6K=ciscoQBridgeCapV15R0001SYPCat6K, PYSNMP_MODULE_ID=ciscoQBridgeCapability, ciscoQBridgeCapCatOSV08R0301=ciscoQBridgeCapCatOSV08R0301, ciscoQBridgeCapability=ciscoQBridgeCapability, ciscoQBridgeCapNxOSV05R0201PN7K=ciscoQBridgeCapNxOSV05R0201PN7K)
