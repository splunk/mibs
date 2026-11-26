#
# PySNMP MIB module CISCO-WAN-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-TOPOLOGY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoWanTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 254))
ciscoWanTopologyCapability.setRevisions(('2003-01-15 00:00', '2002-10-31 00:00', '2001-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanTopologyCapability.setRevisionsDescriptions(('- Added ciscoWanTopologyV4R0000 capability for release\n              4.0.00.', '- Replace the objects cwtLanIP and cwtAtmIP in\n              ciscoWanTopologyCapabilityV3R00 with objects\n              cwtPrimIPIfType, cwtPrimIPIfName, cwtPrimIPAddrType,\n              cwtPrimIP, cwtSecIPIfType, cwtSecIPIfName,\n              cwtSecIPAddrType, cwtSecIP.\n\n            - Added ciscoWanTopologyV3R0020 capability for release\n              3.0.20.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setLastUpdated('200301150000Z')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanTopologyCapability.setDescription('The Agent Capabilities for CISCO-WAN-TOPOLOGY-MIB.\n\t    This MIB is used in the MGX8850 product family, which\n            contains the MGX8850 and MGX8950 switches.')
ciscoWanTopologyCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R00 = ciscoWanTopologyCapabilityV3R00.setProductRelease('MGX8850 and BPX-SES Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R00 = ciscoWanTopologyCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanTopologyCapabilityV3R00.setDescription('Persistent Topology MIB Capabilities.')
ciscoWanTopologyCapabilityV3R0020 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R0020 = ciscoWanTopologyCapabilityV3R0020.setProductRelease('MGX8850 and BPX-SES Release 3.0.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV3R0020 = ciscoWanTopologyCapabilityV3R0020.setStatus('current')
if mibBuilder.loadTexts: ciscoWanTopologyCapabilityV3R0020.setDescription('Persistent Topology MIB Capabilities.')
ciscoWanTopologyCapabilityV4R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 254, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV4R0000 = ciscoWanTopologyCapabilityV4R0000.setProductRelease('MGX8850 and BPX-SES Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanTopologyCapabilityV4R0000 = ciscoWanTopologyCapabilityV4R0000.setStatus('current')
if mibBuilder.loadTexts: ciscoWanTopologyCapabilityV4R0000.setDescription('Persistent Topology MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-WAN-TOPOLOGY-CAPABILITY", ciscoWanTopologyCapabilityV3R0020=ciscoWanTopologyCapabilityV3R0020, PYSNMP_MODULE_ID=ciscoWanTopologyCapability, ciscoWanTopologyCapability=ciscoWanTopologyCapability, ciscoWanTopologyCapabilityV3R00=ciscoWanTopologyCapabilityV3R00, ciscoWanTopologyCapabilityV4R0000=ciscoWanTopologyCapabilityV4R0000)
