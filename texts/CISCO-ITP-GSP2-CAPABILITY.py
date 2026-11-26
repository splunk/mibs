#
# PySNMP MIB module CISCO-ITP-GSP2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GSP2-CAPABILITY
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
ciscoGsp2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 307))
ciscoGsp2Capability.setRevisions(('2004-08-25 00:00', '2003-11-24 00:00', '2003-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGsp2Capability.setRevisionsDescriptions(('Added support for objects to indicate whether device \n              support non-stop operations feature.  Added \n              ciscoGsp2CapabilityV12R023000SW1 agent capability \n              statement.', 'Added ciscoGsp2Mtp3ErrorsGroup.\n            Added ciscoGsp2CapabilityV12R022004SW agent capability \n            statement. This capability contains groups from \n            ciscoGsp2CapabilityV12R0204MB4 agent capability \n            statement as well as ciscoGsp2Mtp3ErrorsGroup.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGsp2Capability.setLastUpdated('200408250000Z')
if mibBuilder.loadTexts: ciscoGsp2Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGsp2Capability.setContactInfo('Cisco Systems\n                         Customer Service\n                        \n                         Postal: 170 West Tasman Drive\n                                 San Jose, CA  95134\n                                 USA\n                        \n                         Tel: +1 800 553-NETS\n                        \n                         E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGsp2Capability.setDescription('Agent capabilities for the CISCO-ITP-GSP2-MIB.')
ciscoGsp2CapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R0204MB4 = ciscoGsp2CapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R0204MB4 = ciscoGsp2CapabilityV12R0204MB4.setStatus('current')
if mibBuilder.loadTexts: ciscoGsp2CapabilityV12R0204MB4.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GSP2-MIB.my\n            User Agent MIB capabilities.')
ciscoGsp2CapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022004SW = ciscoGsp2CapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022004SW = ciscoGsp2CapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGsp2CapabilityV12R022004SW.setDescription('IOS 12.2(20.4)SW Cisco CISCO-ITP-GSP2-MIB.my\n            User Agent MIB capabilities.')
ciscoGsp2CapabilityV12R022300SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 307, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022300SW1 = ciscoGsp2CapabilityV12R022300SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsp2CapabilityV12R022300SW1 = ciscoGsp2CapabilityV12R022300SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoGsp2CapabilityV12R022300SW1.setDescription('IOS 12.2(23)SW1 Cisco CISCO-ITP-GSP2-MIB.my\n            User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GSP2-CAPABILITY", PYSNMP_MODULE_ID=ciscoGsp2Capability, ciscoGsp2CapabilityV12R022300SW1=ciscoGsp2CapabilityV12R022300SW1, ciscoGsp2Capability=ciscoGsp2Capability, ciscoGsp2CapabilityV12R022004SW=ciscoGsp2CapabilityV12R022004SW, ciscoGsp2CapabilityV12R0204MB4=ciscoGsp2CapabilityV12R0204MB4)
