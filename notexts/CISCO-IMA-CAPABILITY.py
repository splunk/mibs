#
# PySNMP MIB module CISCO-IMA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMA-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoImaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 257))
ciscoImaCapability.setRevisions(('2002-08-15 00:00', '2002-04-29 00:00',))
if mibBuilder.loadTexts: ciscoImaCapability.setLastUpdated('200208150000Z')
if mibBuilder.loadTexts: ciscoImaCapability.setOrganization('Cisco Systems, Inc.')
ciscoImaAxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 257, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaAxsmeCapabilityV3R00 = ciscoImaAxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaAxsmeCapabilityV3R00 = ciscoImaAxsmeCapabilityV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMA-CAPABILITY", ciscoImaAxsmeCapabilityV3R00=ciscoImaAxsmeCapabilityV3R00, ciscoImaCapability=ciscoImaCapability, PYSNMP_MODULE_ID=ciscoImaCapability)
