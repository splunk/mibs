#
# PySNMP MIB module CISCO-SONET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SONET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoSonetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 266))
ciscoSonetCapability.setRevisions(('2004-02-19 00:00', '2003-03-11 00:00', '2002-03-12 00:00',))
if mibBuilder.loadTexts: ciscoSonetCapability.setLastUpdated('200402190000Z')
if mibBuilder.loadTexts: ciscoSonetCapability.setOrganization('Cisco Systems, Inc.')
ciscoSonetCapabilityAxsmV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityAxsmV2R0100 = ciscoSonetCapabilityAxsmV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityAxsmV2R0100 = ciscoSonetCapabilityAxsmV2R0100.setStatus('current')
ciscoSonetCapabilitySrmeV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilitySrmeV3R00 = ciscoSonetCapabilitySrmeV3R00.setProductRelease('MGX8850 Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilitySrmeV3R00 = ciscoSonetCapabilitySrmeV3R00.setStatus('current')
ciscoSonetCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV4R00 = ciscoSonetCapabilityV4R00.setProductRelease('MGX8950  and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV4R00 = ciscoSonetCapabilityV4R00.setStatus('current')
ciscoSonetCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV5R00 = ciscoSonetCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV5R00 = ciscoSonetCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-SONET-CAPABILITY", ciscoSonetCapabilityV4R00=ciscoSonetCapabilityV4R00, ciscoSonetCapabilityAxsmV2R0100=ciscoSonetCapabilityAxsmV2R0100, ciscoSonetCapability=ciscoSonetCapability, ciscoSonetCapabilitySrmeV3R00=ciscoSonetCapabilitySrmeV3R00, ciscoSonetCapabilityV5R00=ciscoSonetCapabilityV5R00, PYSNMP_MODULE_ID=ciscoSonetCapability)
