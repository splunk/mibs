#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ETHERLIKE-EXT-CAPABILITY
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
ciscoEtherlikeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 587))
ciscoEtherlikeExtCapability.setRevisions(('2011-04-01 00:00', '2010-10-29 00:00', '2010-03-12 00:00',))
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setOrganization('Cisco Systems, Inc.')
ceeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setStatus('current')
ceeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setStatus('current')
ceeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-CAPABILITY", ciscoEtherlikeExtCapability=ciscoEtherlikeExtCapability, PYSNMP_MODULE_ID=ciscoEtherlikeExtCapability, ceeCapV12R0250SYPCat6K=ceeCapV12R0250SYPCat6K, ceeCapV15R0002SGPCat4K=ceeCapV15R0002SGPCat4K, ceeCapV12R0233SXI4PCat6K=ceeCapV12R0233SXI4PCat6K)
