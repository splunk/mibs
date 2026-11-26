#
# PySNMP MIB module CISCO-ENTITY-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-EXT-CAPABILITY
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
ciscoEntityExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 392))
ciscoEntityExtCapability.setRevisions(('2007-09-06 00:00', '2004-03-31 00:00',))
if mibBuilder.loadTexts: ciscoEntityExtCapability.setLastUpdated('200709060000Z')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoEntityExtCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtCapCatOSV08R0301 = ciscoEntityExtCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtCapCatOSV08R0301 = ciscoEntityExtCapCatOSV08R0301.setStatus('current')
ceExtCapV12R0217SXPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0217SXPCat6k = ceExtCapV12R0217SXPCat6k.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0217SXPCat6k = ceExtCapV12R0217SXPCat6k.setStatus('current')
ceExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0233SXHPCat6k = ceExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0233SXHPCat6k = ceExtCapV12R0233SXHPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-EXT-CAPABILITY", ceExtCapV12R0217SXPCat6k=ceExtCapV12R0217SXPCat6k, ceExtCapV12R0233SXHPCat6k=ceExtCapV12R0233SXHPCat6k, ciscoEntityExtCapability=ciscoEntityExtCapability, PYSNMP_MODULE_ID=ciscoEntityExtCapability, ciscoEntityExtCapCatOSV08R0301=ciscoEntityExtCapCatOSV08R0301)
