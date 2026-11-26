#
# PySNMP MIB module CISCO-Q-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-Q-BRIDGE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-Q-BRIDGE-CAPABILITY", ciscoQBridgeCapCatOSV08R0301=ciscoQBridgeCapCatOSV08R0301, ciscoQBridgeCapability=ciscoQBridgeCapability, ciscoQBridgeCapV15R0001SYPCat6K=ciscoQBridgeCapV15R0001SYPCat6K, ciscoQBridgeCapNxOSV05R0201PN7K=ciscoQBridgeCapNxOSV05R0201PN7K, PYSNMP_MODULE_ID=ciscoQBridgeCapability, ciscoQBridgeCapV12R0233SXIPCat6K=ciscoQBridgeCapV12R0233SXIPCat6K)
