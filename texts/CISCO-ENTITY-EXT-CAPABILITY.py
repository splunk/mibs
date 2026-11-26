#
# PySNMP MIB module CISCO-ENTITY-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntityExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 392))
ciscoEntityExtCapability.setRevisions(('2007-09-06 00:00', '2004-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityExtCapability.setRevisionsDescriptions(('Addition of ceExtCapV12R0217SXPCat6k and\n                ceExtCapV12R0233SXHPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityExtCapability.setLastUpdated('200709060000Z')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setDescription('The agent capabilities description of \n                CISCO-ENTITY-EXT-MIB.')
ciscoEntityExtCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtCapCatOSV08R0301 = ciscoEntityExtCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtCapCatOSV08R0301 = ciscoEntityExtCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityExtCapCatOSV08R0301.setDescription('CISCO-ENTITY-EXT-MIB agent capabilities.')
ceExtCapV12R0217SXPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0217SXPCat6k = ceExtCapV12R0217SXPCat6k.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0217SXPCat6k = ceExtCapV12R0217SXPCat6k.setStatus('current')
if mibBuilder.loadTexts: ceExtCapV12R0217SXPCat6k.setDescription('CISCO-ENTITY-EXT-MIB capabilities.')
ceExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0233SXHPCat6k = ceExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0233SXHPCat6k = ceExtCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: ceExtCapV12R0233SXHPCat6k.setDescription('CISCO-ENTITY-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityExtCapability, ciscoEntityExtCapCatOSV08R0301=ciscoEntityExtCapCatOSV08R0301, ceExtCapV12R0217SXPCat6k=ceExtCapV12R0217SXPCat6k, ceExtCapV12R0233SXHPCat6k=ceExtCapV12R0233SXHPCat6k, ciscoEntityExtCapability=ciscoEntityExtCapability)
