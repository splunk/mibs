#
# PySNMP MIB module CISCO-VLAN-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-GROUP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVlanGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 590))
ciscoVlanGroupCapability.setRevisions(('2012-04-10 00:00', '2011-09-22 00:00', '2011-03-31 00:00', '2011-03-23 00:00', '2010-03-22 00:00',))
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setLastUpdated('201204100000Z')
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setOrganization('Cisco Systems, Inc.')
ciscoVlanGroupCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXI4PCat6K = ciscoVlanGroupCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXI4PCat6K = ciscoVlanGroupCapV12R0233SXI4PCat6K.setStatus('current')
ciscoVlanGroupCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXJPCat6k = ciscoVlanGroupCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXJPCat6k = ciscoVlanGroupCapV12R0233SXJPCat6k.setStatus('current')
ciscoVlanGroupCapV15R0002SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0002SGPCat4k = ciscoVlanGroupCapV15R0002SGPCat4k.setProductRelease('Cisco IOS 15.0(2)SG on Cat4k family switches\n                    (excluding switches with SUP7).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0002SGPCat4k = ciscoVlanGroupCapV15R0002SGPCat4k.setStatus('current')
ciscoVlanGroupCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0001SYPCat6k = ciscoVlanGroupCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0001SYPCat6k = ciscoVlanGroupCapV15R0001SYPCat6k.setStatus('current')
ciscoVlanGroupCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0101SGPCat4k = ciscoVlanGroupCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4k family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0101SGPCat4k = ciscoVlanGroupCapV15R0101SGPCat4k.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-CAPABILITY", ciscoVlanGroupCapV12R0233SXJPCat6k=ciscoVlanGroupCapV12R0233SXJPCat6k, PYSNMP_MODULE_ID=ciscoVlanGroupCapability, ciscoVlanGroupCapV12R0233SXI4PCat6K=ciscoVlanGroupCapV12R0233SXI4PCat6K, ciscoVlanGroupCapV15R0002SGPCat4k=ciscoVlanGroupCapV15R0002SGPCat4k, ciscoVlanGroupCapV15R0001SYPCat6k=ciscoVlanGroupCapV15R0001SYPCat6k, ciscoVlanGroupCapV15R0101SGPCat4k=ciscoVlanGroupCapV15R0101SGPCat4k, ciscoVlanGroupCapability=ciscoVlanGroupCapability)
