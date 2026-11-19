#
# PySNMP MIB module CISCO-MAU-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAU-CAPABILITY
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
ciscoMauCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 411))
ciscoMauCapability.setRevisions(('2014-07-30 00:00', '2011-09-28 00:00', '2008-10-28 00:00', '2007-07-13 00:00', '2004-10-22 00:00',))
if mibBuilder.loadTexts: ciscoMauCapability.setLastUpdated('201407300000Z')
if mibBuilder.loadTexts: ciscoMauCapability.setOrganization('Cisco Systems, Inc.')
ciscoMauCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapCatOSV08R0401 = ciscoMauCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapCatOSV08R0401 = ciscoMauCapCatOSV08R0401.setStatus('current')
ciscoMauCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXHPCat6K = ciscoMauCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXHPCat6K = ciscoMauCapV12R0233SXHPCat6K.setStatus('current')
ciscoMauCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXIPCat6K = ciscoMauCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXIPCat6K = ciscoMauCapV12R0233SXIPCat6K.setStatus('current')
ciscoMauCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXJPCat6K = ciscoMauCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXJPCat6K = ciscoMauCapV12R0233SXJPCat6K.setStatus('current')
ciscoMauCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV15R0001SYPCat6K = ciscoMauCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV15R0001SYPCat6K = ciscoMauCapV15R0001SYPCat6K.setStatus('current')
ciscoMauCapV05R0003U0401PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV05R0003U0401PN3K = ciscoMauCapV05R0003U0401PN3K.setProductRelease('Cisco NX-OS 5.0(3)U4(1) on Nexus 3000 series\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV05R0003U0401PN3K = ciscoMauCapV05R0003U0401PN3K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-CAPABILITY", ciscoMauCapV05R0003U0401PN3K=ciscoMauCapV05R0003U0401PN3K, ciscoMauCapV15R0001SYPCat6K=ciscoMauCapV15R0001SYPCat6K, ciscoMauCapCatOSV08R0401=ciscoMauCapCatOSV08R0401, ciscoMauCapV12R0233SXIPCat6K=ciscoMauCapV12R0233SXIPCat6K, ciscoMauCapability=ciscoMauCapability, PYSNMP_MODULE_ID=ciscoMauCapability, ciscoMauCapV12R0233SXJPCat6K=ciscoMauCapV12R0233SXJPCat6K, ciscoMauCapV12R0233SXHPCat6K=ciscoMauCapV12R0233SXHPCat6K)
