#
# PySNMP MIB module CISCO-IGMP-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IGMP-SNOOPING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoIgmpSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 320))
ciscoIgmpSnoopingCapability.setRevisions(('2012-09-12 00:00', '2010-11-16 00:00', '2008-10-31 00:00', '2004-03-10 00:00', '2003-08-13 00:00',))
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setLastUpdated('201209120000Z')
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setOrganization('Cisco Systems, Inc.')
cisCapCatOSV08R0101Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc = cisCapCatOSV08R0101Cat6kPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc = cisCapCatOSV08R0101Cat6kPfc.setStatus('current')
cisCapCatOSV08R0101Cat6kPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc2 = cisCapCatOSV08R0101Cat6kPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc2 = cisCapCatOSV08R0101Cat6kPfc2.setStatus('current')
cisCapCatOSV08R0101Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc3 = cisCapCatOSV08R0101Cat6kPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc3 = cisCapCatOSV08R0101Cat6kPfc3.setStatus('current')
cisCapCatOSV08R0301Cat6kPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc2 = cisCapCatOSV08R0301Cat6kPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc2 = cisCapCatOSV08R0301Cat6kPfc2.setStatus('current')
cisCapCatOSV08R0301Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc3 = cisCapCatOSV08R0301Cat6kPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc3 = cisCapCatOSV08R0301Cat6kPfc3.setStatus('current')
cisCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0233SXIPCat6K = cisCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0233SXIPCat6K = cisCapV12R0233SXIPCat6K.setStatus('current')
cisCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0250SYPCat6K = cisCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0250SYPCat6K = cisCapV12R0250SYPCat6K.setStatus('current')
cisCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc3 = cisCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc3 = cisCapV15R0101SYPCat6kPfc3.setStatus('current')
cisCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc4 = cisCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc4 = cisCapV15R0101SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-IGMP-SNOOPING-CAPABILITY", cisCapCatOSV08R0301Cat6kPfc3=cisCapCatOSV08R0301Cat6kPfc3, cisCapV12R0250SYPCat6K=cisCapV12R0250SYPCat6K, cisCapCatOSV08R0101Cat6kPfc=cisCapCatOSV08R0101Cat6kPfc, cisCapV12R0233SXIPCat6K=cisCapV12R0233SXIPCat6K, ciscoIgmpSnoopingCapability=ciscoIgmpSnoopingCapability, cisCapV15R0101SYPCat6kPfc4=cisCapV15R0101SYPCat6kPfc4, PYSNMP_MODULE_ID=ciscoIgmpSnoopingCapability, cisCapCatOSV08R0301Cat6kPfc2=cisCapCatOSV08R0301Cat6kPfc2, cisCapV15R0101SYPCat6kPfc3=cisCapV15R0101SYPCat6kPfc3, cisCapCatOSV08R0101Cat6kPfc2=cisCapCatOSV08R0101Cat6kPfc2, cisCapCatOSV08R0101Cat6kPfc3=cisCapCatOSV08R0101Cat6kPfc3)
