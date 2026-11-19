#
# PySNMP MIB module CISCO-IMA-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMA-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
MilliSeconds, = mibBuilder.importSymbols("IMA-MIB", "MilliSeconds")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-IMA-EXT-CAPABILITY", ciscoImaExtCapabilityV12R05=ciscoImaExtCapabilityV12R05, ciscoImaExtCapability=ciscoImaExtCapability, ciscoImaExtCapabilityV5R320=ciscoImaExtCapabilityV5R320, PYSNMP_MODULE_ID=ciscoImaExtCapability, ciscoImaExtAxsmeCapabilityV3R0=ciscoImaExtAxsmeCapabilityV3R0, ciscoImaExtAxsmeCapabilityV5R320=ciscoImaExtAxsmeCapabilityV5R320)
