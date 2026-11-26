#
# PySNMP MIB module CISCO-ITP-RT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-RT-CAPABILITY
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
ciscoItpRtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 216))
ciscoItpRtCapability.setRevisions(('2002-01-21 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpRtCapability.setRevisionsDescriptions(('Updated capabilities MIB as required for \n                         new groups.\n                         \n                         cItpRtNotificationsGroup,\n                         cItpRtScalarGroupRev1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpRtCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoItpRtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpRtCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpRtCapability.setDescription('Agent capabilities for the CISCO-ITP-RT-MIB.')
ciscoItpRtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 216, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R024MB1 = ciscoItpRtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R024MB1 = ciscoItpRtCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpRtCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-RT-MIB.my User Agent\n                       MIB capabilities.')
ciscoItpRtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 216, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R0204MB3 = ciscoItpRtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R0204MB3 = ciscoItpRtCapabilityV12R0204MB3.setStatus('current')
if mibBuilder.loadTexts: ciscoItpRtCapabilityV12R0204MB3.setDescription('IOS 12.2(4)MB3 Cisco CISCO-ITP-RT-MIB.my User Agent\n                       MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-RT-CAPABILITY", ciscoItpRtCapability=ciscoItpRtCapability, ciscoItpRtCapabilityV12R024MB1=ciscoItpRtCapabilityV12R024MB1, PYSNMP_MODULE_ID=ciscoItpRtCapability, ciscoItpRtCapabilityV12R0204MB3=ciscoItpRtCapabilityV12R0204MB3)
