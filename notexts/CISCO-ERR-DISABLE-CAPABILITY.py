#
# PySNMP MIB module CISCO-ERR-DISABLE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ERR-DISABLE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoErrDisableCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 589))
ciscoErrDisableCapability.setRevisions(('2013-09-25 00:00', '2010-10-29 00:00', '2010-05-05 00:00', '2010-03-11 00:00',))
if mibBuilder.loadTexts: ciscoErrDisableCapability.setLastUpdated('201309250000Z')
if mibBuilder.loadTexts: ciscoErrDisableCapability.setOrganization('Cisco Systems, Inc.')
cErrDisableCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setStatus('current')
cErrDisableCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setStatus('current')
cErrDisableCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setStatus('current')
cErrDisableCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERR-DISABLE-CAPABILITY", cErrDisableCapV12R0233SXI4PCat6K=cErrDisableCapV12R0233SXI4PCat6K, ciscoErrDisableCapability=ciscoErrDisableCapability, cErrDisableCapV12R0250SYPCat6K=cErrDisableCapV12R0250SYPCat6K, PYSNMP_MODULE_ID=ciscoErrDisableCapability, cErrDisableCapV15R0102SYPCat6K=cErrDisableCapV15R0102SYPCat6K, cErrDisableCapV12R0254SGPCat4K=cErrDisableCapV12R0254SGPCat4K)
