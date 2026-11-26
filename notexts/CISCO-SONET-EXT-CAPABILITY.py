#
# PySNMP MIB module CISCO-SONET-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SONET-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSonetExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 261))
ciscoSonetExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-13 00:00', '2002-02-17 00:00',))
if mibBuilder.loadTexts: ciscoSonetExtCapability.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSonetExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setStatus('current')
ciscoSonetExtAxsmCapabilityV2R11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setProductRelease('MGX8850 Release 2.0.11')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setStatus('current')
ciscoSonetExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setStatus('current')
ciscoSonetExtSrmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setProductRelease('MGX8800 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setStatus('current')
ciscoSonetExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setProductRelease('MGX8850, MGX8950 Release 4.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setStatus('current')
ciscoSonetExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-SONET-EXT-CAPABILITY", ciscoSonetExtAxsmCapabilityV2R11=ciscoSonetExtAxsmCapabilityV2R11, ciscoSonetExtCapabilityV4R00=ciscoSonetExtCapabilityV4R00, PYSNMP_MODULE_ID=ciscoSonetExtCapability, ciscoSonetExtAxsmCapabilityV2R00=ciscoSonetExtAxsmCapabilityV2R00, ciscoSonetExtSrmeCapabilityV3R00=ciscoSonetExtSrmeCapabilityV3R00, ciscoSonetExtCapability=ciscoSonetExtCapability, ciscoSonetExtAxsmeCapabilityV21R60=ciscoSonetExtAxsmeCapabilityV21R60, ciscoSonetExtCapabilityV5R00=ciscoSonetExtCapabilityV5R00)
