#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ETHERLIKE-EXT-CAPABILITY
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
ciscoEtherlikeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 587))
ciscoEtherlikeExtCapability.setRevisions(('2011-04-01 00:00', '2010-10-29 00:00', '2010-03-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setRevisionsDescriptions(('Add capability statement ceeCapV15R0002SGPCat4K.', 'Add capability statement ceeCapV12R0250SYPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setDescription('Agent capabilities for CISCO-ETHERLIKE-EXT-MIB.')
ceeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: ceeCapV12R0233SXI4PCat6K.setDescription('CISCO-ETHERLIKE-EXT-MIB agent capabilities.')
ceeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ceeCapV12R0250SYPCat6K.setDescription('CISCO-ETHERLIKE-EXT-MIB agent capabilities.')
ceeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ceeCapV15R0002SGPCat4K.setDescription('CISCO-ETHERLIKE-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherlikeExtCapability, ceeCapV12R0250SYPCat6K=ceeCapV12R0250SYPCat6K, ceeCapV15R0002SGPCat4K=ceeCapV15R0002SGPCat4K, ciscoEtherlikeExtCapability=ciscoEtherlikeExtCapability, ceeCapV12R0233SXI4PCat6K=ceeCapV12R0233SXI4PCat6K)
