#
# PySNMP MIB module CISCO-MAU-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAU-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
mibBuilder.exportSymbols("CISCO-MAU-CAPABILITY", PYSNMP_MODULE_ID=ciscoMauCapability, ciscoMauCapV12R0233SXHPCat6K=ciscoMauCapV12R0233SXHPCat6K, ciscoMauCapV12R0233SXJPCat6K=ciscoMauCapV12R0233SXJPCat6K, ciscoMauCapV15R0001SYPCat6K=ciscoMauCapV15R0001SYPCat6K, ciscoMauCapCatOSV08R0401=ciscoMauCapCatOSV08R0401, ciscoMauCapability=ciscoMauCapability, ciscoMauCapV05R0003U0401PN3K=ciscoMauCapV05R0003U0401PN3K, ciscoMauCapV12R0233SXIPCat6K=ciscoMauCapV12R0233SXIPCat6K)
