#
# PySNMP MIB module CISCO-DS3-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DS3-EXT-CAPABILITY
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
ciscoDs3ExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 262))
ciscoDs3ExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-20 00:00', '2002-03-25 00:00',))
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoDs3ExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setStatus('current')
ciscoDs3ExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setStatus('current')
ciscoDs3ExtSrmCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setStatus('current')
ciscoDs3ExtFrsm12CapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setStatus('current')
ciscoDs3ExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release \n                         4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setStatus('current')
ciscoDs3ExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS3-EXT-CAPABILITY", ciscoDs3ExtAxsmCapabilityV2R00=ciscoDs3ExtAxsmCapabilityV2R00, PYSNMP_MODULE_ID=ciscoDs3ExtCapability, ciscoDs3ExtAxsmeCapabilityV21R60=ciscoDs3ExtAxsmeCapabilityV21R60, ciscoDs3ExtCapability=ciscoDs3ExtCapability, ciscoDs3ExtFrsm12CapabilityV3R00=ciscoDs3ExtFrsm12CapabilityV3R00, ciscoDs3ExtSrmCapabilityV3R00=ciscoDs3ExtSrmCapabilityV3R00, ciscoDs3ExtCapabilityV4R00=ciscoDs3ExtCapabilityV4R00, ciscoDs3ExtCapabilityV5R00=ciscoDs3ExtCapabilityV5R00)
