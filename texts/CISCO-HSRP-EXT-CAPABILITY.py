#
# PySNMP MIB module CISCO-HSRP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HSRP-EXT-CAPABILITY
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
ciscoHsrpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10001))
ciscoHsrpExtCapability.setRevisions(('2007-11-27 00:00', '1998-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHsrpExtCapability.setRevisionsDescriptions(('Added agent capabilities for IOS-XR 3.6', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setLastUpdated('200711270000Z')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-hsrp@cisco.com')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setDescription('Agent capabilities for CISCO-HSRP-EXT-MIB')
ciscoHsrpExtCapabilityV1R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10001, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV1R0 = ciscoHsrpExtCapabilityV1R0.setProductRelease('Cisco IOS/ENA 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV1R0 = ciscoHsrpExtCapabilityV1R0.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpExtCapabilityV1R0.setDescription('Cisco Hsrp Ext MIB capabilities')
ciscoHsrpExtCapabilityV3R6CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10001, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV3R6CRS1 = ciscoHsrpExtCapabilityV3R6CRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV3R6CRS1 = ciscoHsrpExtCapabilityV3R6CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpExtCapabilityV3R6CRS1.setDescription('Cisco Hsrp Ext MIB capabilities')
mibBuilder.exportSymbols("CISCO-HSRP-EXT-CAPABILITY", ciscoHsrpExtCapabilityV1R0=ciscoHsrpExtCapabilityV1R0, ciscoHsrpExtCapabilityV3R6CRS1=ciscoHsrpExtCapabilityV3R6CRS1, PYSNMP_MODULE_ID=ciscoHsrpExtCapability, ciscoHsrpExtCapability=ciscoHsrpExtCapability)
