#
# PySNMP MIB module CISCO-ITP-GACT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GACT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
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
ciscoGactCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 304))
ciscoGactCapability.setRevisions(('2007-04-26 00:00', '2003-12-08 00:00', '2003-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGactCapability.setRevisionsDescriptions(('Added ciscoGactCapabilityV12R0218IXA and\n        ciscoGactCapabilityV12R0411SW capability statements.', 'Support for cross instance global title\n        translation.  Added agent capability\n        ciscoGactCapabilityV12R022004SW statement for \n        IOS 12.2(20.4) and replaced \n        ciscoGactGttGroup object group with\n        ciscoGactGttGroupRev1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGactCapability.setLastUpdated('200704260000Z')
if mibBuilder.loadTexts: ciscoGactCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGactCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGactCapability.setDescription('Agent capabilities for the CISCO-ITP-GACT-MIB.')
ciscoGactCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0204MB10 = ciscoGactCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0204MB10 = ciscoGactCapabilityV12R0204MB10.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0204MB10.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R022004SW = ciscoGactCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R022004SW = ciscoGactCapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R022004SW.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0218IXA = ciscoGactCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0218IXA = ciscoGactCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0218IXA.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0411SW = ciscoGactCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0411SW = ciscoGactCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0411SW.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GACT-CAPABILITY", ciscoGactCapabilityV12R0411SW=ciscoGactCapabilityV12R0411SW, PYSNMP_MODULE_ID=ciscoGactCapability, ciscoGactCapabilityV12R0218IXA=ciscoGactCapabilityV12R0218IXA, ciscoGactCapability=ciscoGactCapability, ciscoGactCapabilityV12R0204MB10=ciscoGactCapabilityV12R0204MB10, ciscoGactCapabilityV12R022004SW=ciscoGactCapabilityV12R022004SW)
