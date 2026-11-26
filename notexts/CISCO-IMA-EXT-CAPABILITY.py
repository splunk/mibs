#
# PySNMP MIB module CISCO-IMA-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMA-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
MilliSeconds, = mibBuilder.importSymbols("IMA-MIB", "MilliSeconds")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImaExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 524))
ciscoImaExtCapability.setRevisions(('2006-11-24 00:00', '2006-09-26 00:00', '2002-03-04 00:00',))
if mibBuilder.loadTexts: ciscoImaExtCapability.setLastUpdated('200611240000Z')
if mibBuilder.loadTexts: ciscoImaExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoImaExtAxsmeCapabilityV3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV3R0 = ciscoImaExtAxsmeCapabilityV3R0.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV3R0 = ciscoImaExtAxsmeCapabilityV3R0.setStatus('current')
ciscoImaExtAxsmeCapabilityV5R320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV5R320 = ciscoImaExtAxsmeCapabilityV5R320.setProductRelease('MGX8850 Release 5.3.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV5R320 = ciscoImaExtAxsmeCapabilityV5R320.setStatus('current')
ciscoImaExtCapabilityV5R320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV5R320 = ciscoImaExtCapabilityV5R320.setProductRelease('MGX8950  and MGX8850 Release 5.3.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV5R320 = ciscoImaExtCapabilityV5R320.setStatus('current')
ciscoImaExtCapabilityV12R05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV12R05 = ciscoImaExtCapabilityV12R05.setProductRelease('IOS 12.5 for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV12R05 = ciscoImaExtCapabilityV12R05.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMA-EXT-CAPABILITY", ciscoImaExtAxsmeCapabilityV5R320=ciscoImaExtAxsmeCapabilityV5R320, ciscoImaExtCapabilityV12R05=ciscoImaExtCapabilityV12R05, ciscoImaExtAxsmeCapabilityV3R0=ciscoImaExtAxsmeCapabilityV3R0, ciscoImaExtCapabilityV5R320=ciscoImaExtCapabilityV5R320, PYSNMP_MODULE_ID=ciscoImaExtCapability, ciscoImaExtCapability=ciscoImaExtCapability)
