#
# PySNMP MIB module CISCO-MEMORY-POOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MEMORY-POOL-CAPABILITY
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
ciscoMemoryPoolCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 338))
ciscoMemoryPoolCapability.setRevisions(('2006-05-02 00:00', '2005-10-26 00:00', '2003-08-07 00:00',))
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setLastUpdated('200605020000Z')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setOrganization('Cisco Systems, Inc.')
ciscoMemoryPoolCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setStatus('current')
ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEMORY-POOL-CAPABILITY", ciscoMemoryPoolCapCatOSV08R0101=ciscoMemoryPoolCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoMemoryPoolCapability, ciscoMemoryPoolCapabilityIOSXRV2R0CRS1=ciscoMemoryPoolCapabilityIOSXRV2R0CRS1, ciscoMemoryPoolCapability=ciscoMemoryPoolCapability)
