#
# PySNMP MIB module CISCO-SONET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SONET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
mibBuilder.exportSymbols("CISCO-SONET-CAPABILITY", ciscoSonetCapabilitySrmeV3R00=ciscoSonetCapabilitySrmeV3R00, ciscoSonetCapability=ciscoSonetCapability, ciscoSonetCapabilityV4R00=ciscoSonetCapabilityV4R00, PYSNMP_MODULE_ID=ciscoSonetCapability, ciscoSonetCapabilityAxsmV2R0100=ciscoSonetCapabilityAxsmV2R0100, ciscoSonetCapabilityV5R00=ciscoSonetCapabilityV5R00)
