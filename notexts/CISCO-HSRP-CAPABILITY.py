#
# PySNMP MIB module CISCO-HSRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HSRP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:42 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHsrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10000))
ciscoHsrpCapability.setRevisions(('2007-11-27 00:00', '1998-08-25 00:00',))
if mibBuilder.loadTexts: ciscoHsrpCapability.setLastUpdated('200711270000Z')
if mibBuilder.loadTexts: ciscoHsrpCapability.setOrganization('Cisco Systems, Inc.')
ciscoHsrpCapabilityV12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV12R0 = ciscoHsrpCapabilityV12R0.setProductRelease('Cisco IOS 12.0(3)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV12R0 = ciscoHsrpCapabilityV12R0.setStatus('current')
ciscoHsrpCapabilityV3R6CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV3R6CRS1 = ciscoHsrpCapabilityV3R6CRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV3R6CRS1 = ciscoHsrpCapabilityV3R6CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-HSRP-CAPABILITY", ciscoHsrpCapability=ciscoHsrpCapability, PYSNMP_MODULE_ID=ciscoHsrpCapability, ciscoHsrpCapabilityV3R6CRS1=ciscoHsrpCapabilityV3R6CRS1, ciscoHsrpCapabilityV12R0=ciscoHsrpCapabilityV12R0)
