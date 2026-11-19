#
# PySNMP MIB module CISCO-HSRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HSRP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-HSRP-CAPABILITY", ciscoHsrpCapabilityV12R0=ciscoHsrpCapabilityV12R0, ciscoHsrpCapabilityV3R6CRS1=ciscoHsrpCapabilityV3R6CRS1, PYSNMP_MODULE_ID=ciscoHsrpCapability, ciscoHsrpCapability=ciscoHsrpCapability)
