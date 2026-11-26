#
# PySNMP MIB module CISCO-HSRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HSRP-CAPABILITY
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
ciscoHsrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10000))
ciscoHsrpCapability.setRevisions(('2007-11-27 00:00', '1998-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHsrpCapability.setRevisionsDescriptions(('Added agent capability for IOS-XR 3.6', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHsrpCapability.setLastUpdated('200711270000Z')
if mibBuilder.loadTexts: ciscoHsrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHsrpCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-hsrp@cisco.com')
if mibBuilder.loadTexts: ciscoHsrpCapability.setDescription('Agent capabilities for CISCO-HSRP-MIB')
ciscoHsrpCapabilityV12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV12R0 = ciscoHsrpCapabilityV12R0.setProductRelease('Cisco IOS 12.0(3)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV12R0 = ciscoHsrpCapabilityV12R0.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpCapabilityV12R0.setDescription('Cisco Hsrp MIB capabilities')
ciscoHsrpCapabilityV3R6CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV3R6CRS1 = ciscoHsrpCapabilityV3R6CRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV3R6CRS1 = ciscoHsrpCapabilityV3R6CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpCapabilityV3R6CRS1.setDescription('Cisco Hsrp MIB capabilities')
mibBuilder.exportSymbols("CISCO-HSRP-CAPABILITY", PYSNMP_MODULE_ID=ciscoHsrpCapability, ciscoHsrpCapabilityV3R6CRS1=ciscoHsrpCapabilityV3R6CRS1, ciscoHsrpCapabilityV12R0=ciscoHsrpCapabilityV12R0, ciscoHsrpCapability=ciscoHsrpCapability)
