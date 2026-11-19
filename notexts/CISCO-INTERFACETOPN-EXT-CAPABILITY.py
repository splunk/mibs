#
# PySNMP MIB module CISCO-INTERFACETOPN-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-INTERFACETOPN-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoTopNExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 543))
ciscoTopNExtCapability.setRevisions(('2012-09-07 01:00', '2007-07-06 00:00',))
if mibBuilder.loadTexts: ciscoTopNExtCapability.setLastUpdated('201209070100Z')
if mibBuilder.loadTexts: ciscoTopNExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoTopNExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setStatus('current')
ciscoTopNExtCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-EXT-CAPABILITY", ciscoTopNExtCapV15R0001SY1PCat6K=ciscoTopNExtCapV15R0001SY1PCat6K, ciscoTopNExtCapV12R0233SXHPCat6k=ciscoTopNExtCapV12R0233SXHPCat6k, PYSNMP_MODULE_ID=ciscoTopNExtCapability, ciscoTopNExtCapability=ciscoTopNExtCapability)
