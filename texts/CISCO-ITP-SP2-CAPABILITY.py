#
# PySNMP MIB module CISCO-ITP-SP2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-SP2-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:43 2026
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
ciscoItpSp2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 272))
ciscoItpSp2Capability.setRevisions(('2002-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpSp2Capability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpSp2Capability.setLastUpdated('200206050000Z')
if mibBuilder.loadTexts: ciscoItpSp2Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpSp2Capability.setContactInfo('Cisco Systems\n                         Customer Service\n                        \n                         Postal: 170 West Tasman Drive\n                                 San Jose, CA  95134\n                                 USA\n                        \n                         Tel: +1 800 553-NETS\n                        \n                         E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpSp2Capability.setDescription('Agent capabilities for the CISCO-ITP-SP2-MIB.')
ciscoItpSp2CapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 272, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSp2CapabilityV12R0204MB4 = ciscoItpSp2CapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSp2CapabilityV12R0204MB4 = ciscoItpSp2CapabilityV12R0204MB4.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSp2CapabilityV12R0204MB4.setDescription('IOS 12.2(4)MB4 Cisco CISCO-ITP-SP2-MIB.my\n                 User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-SP2-CAPABILITY", ciscoItpSp2Capability=ciscoItpSp2Capability, PYSNMP_MODULE_ID=ciscoItpSp2Capability, ciscoItpSp2CapabilityV12R0204MB4=ciscoItpSp2CapabilityV12R0204MB4)
