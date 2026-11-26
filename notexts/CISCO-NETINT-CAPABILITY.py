#
# PySNMP MIB module CISCO-NETINT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NETINT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoNetintCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 452))
ciscoNetintCapability.setRevisions(('2007-07-03 00:00',))
if mibBuilder.loadTexts: ciscoNetintCapability.setLastUpdated('200707030000Z')
if mibBuilder.loadTexts: ciscoNetintCapability.setOrganization('Cisco Systems, Inc.')
ciscoNetintCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 452, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintCapV12R0233SXHPCat6k = ciscoNetintCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintCapV12R0233SXHPCat6k = ciscoNetintCapV12R0233SXHPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETINT-CAPABILITY", ciscoNetintCapability=ciscoNetintCapability, ciscoNetintCapV12R0233SXHPCat6k=ciscoNetintCapV12R0233SXHPCat6k, PYSNMP_MODULE_ID=ciscoNetintCapability)
