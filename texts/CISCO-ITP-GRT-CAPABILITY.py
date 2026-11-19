#
# PySNMP MIB module CISCO-ITP-GRT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GRT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpGrtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 309))
ciscoItpGrtCapability.setRevisions(('2007-04-25 00:00', '2006-10-13 00:00', '2003-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpGrtCapability.setRevisionsDescriptions(('Added ciscoGrtCapabilityV12R0411SW capability statements.', 'Added ciscoGrtCapabilityV12R0218IXA capability statement. Added\n        cosmetic changes to MIB sections.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpGrtCapability.setLastUpdated('200704250000Z')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setDescription('Agent capabilities for the CISCO-ITP-GRT-MIB.')
ciscoGrtCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0204MB10.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GRT-MIB.my\n        User Agent MIB capabilities.')
ciscoGrtCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-GRT-MIB.my\n        User Agent MIB capabilities.')
ciscoGrtCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW Cisco CISCO-ITP-GRT-MIB.my User Agent MIB\n        capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GRT-CAPABILITY", ciscoGrtCapabilityV12R0204MB10=ciscoGrtCapabilityV12R0204MB10, PYSNMP_MODULE_ID=ciscoItpGrtCapability, ciscoItpGrtCapability=ciscoItpGrtCapability, ciscoGrtCapabilityV12R0218IXA=ciscoGrtCapabilityV12R0218IXA, ciscoGrtCapabilityV12R0411SW=ciscoGrtCapabilityV12R0411SW)
