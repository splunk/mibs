#
# PySNMP MIB module CISCO-HSRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HSRP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-HSRP-CAPABILITY", ciscoHsrpCapabilityV12R0=ciscoHsrpCapabilityV12R0, ciscoHsrpCapability=ciscoHsrpCapability, PYSNMP_MODULE_ID=ciscoHsrpCapability, ciscoHsrpCapabilityV3R6CRS1=ciscoHsrpCapabilityV3R6CRS1)
