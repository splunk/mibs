#
# PySNMP MIB module CISCO-HSRP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HSRP-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHsrpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10001))
ciscoHsrpExtCapability.setRevisions(('2007-11-27 00:00', '1998-08-25 00:00',))
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setLastUpdated('200711270000Z')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoHsrpExtCapabilityV1R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10001, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV1R0 = ciscoHsrpExtCapabilityV1R0.setProductRelease('Cisco IOS/ENA 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV1R0 = ciscoHsrpExtCapabilityV1R0.setStatus('current')
ciscoHsrpExtCapabilityV3R6CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10001, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV3R6CRS1 = ciscoHsrpExtCapabilityV3R6CRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV3R6CRS1 = ciscoHsrpExtCapabilityV3R6CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-HSRP-EXT-CAPABILITY", ciscoHsrpExtCapabilityV1R0=ciscoHsrpExtCapabilityV1R0, ciscoHsrpExtCapability=ciscoHsrpExtCapability, PYSNMP_MODULE_ID=ciscoHsrpExtCapability, ciscoHsrpExtCapabilityV3R6CRS1=ciscoHsrpExtCapabilityV3R6CRS1)
