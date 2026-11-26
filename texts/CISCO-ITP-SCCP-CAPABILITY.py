#
# PySNMP MIB module CISCO-ITP-SCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-SCCP-CAPABILITY
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
ciscoItpSccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 221))
ciscoItpSccpCapability.setRevisions(('2002-03-04 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpSccpCapability.setRevisionsDescriptions(('Changes required for the following modifications\n                    to the CISCO-ITP-SCCP-MIB.\n                    \n                    Added the following objects:\n                       CItpSccpGttPrefName\n                       cItpSccpPrefConfigLastChanged\n                       cItpSccpGttPrePrefConv\n                       cItpSccpGttPostPrefConv\n                       cItpSccpGttGtaAddrDispZB\n                       cItpSccpGttGtaAddrLenZB\n                       cItpSccpGttGtaAsName\n\n                    Added the following Tables:\n                       cItpSccpGttAppGrTable\n                       cItpSccpGttPrefTable\n\n                    Updated the following Textual Conventions:\n                       CItpSccpGttAppType\n                       CItpSccpGttGtaResType\n\n                    Deprecated the following objects:\n                       CItpSccpGttGtaAddrLen\n                       cItpSccpGttGtaAddrDisp\n                       cItpSccpGttGtaAddrLen\n\n                    Deprecated the following Tables:\n                       cItpSccpGttAppTable', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpSccpCapability.setLastUpdated('200203040000Z')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setDescription('Agent capabilities for the CISCO-ITP-SCCP-MIB.')
ciscoItpSccpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSccpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-SCCP-MIB.my User Agent\n                   MIB capabilities.')
ciscoItpSccpCapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSccpCapabilityV12R0204MB4.setDescription('IOS 12.2(4)MB4 Cisco CISCO-ITP-SCCP-MIB.my User Agent\n                   MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-SCCP-CAPABILITY", ciscoItpSccpCapabilityV12R0204MB4=ciscoItpSccpCapabilityV12R0204MB4, ciscoItpSccpCapability=ciscoItpSccpCapability, ciscoItpSccpCapabilityV12R024MB1=ciscoItpSccpCapabilityV12R024MB1, PYSNMP_MODULE_ID=ciscoItpSccpCapability)
