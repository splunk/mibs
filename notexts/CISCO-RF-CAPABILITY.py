#
# PySNMP MIB module CISCO-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
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
ciscoRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoRFCapability.setRevisions(('2003-08-20 00:00', '2001-01-04 10:00',))
if mibBuilder.loadTexts: ciscoRFCapability.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: ciscoRFCapability.setOrganization('Cisco Systems, Inc.')
ciscoRFCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setStatus('current')
ciscoRFCapabilityV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11bEX) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setStatus('current')
ciscoRFCapabilityV12R0113ECat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setStatus('current')
ciscoRFCapabilityCatOSV8R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-RF-CAPABILITY", ciscoRFCapabilityV12R0113ECat6k=ciscoRFCapabilityV12R0113ECat6k, ciscoRFCapabilityV12R0111bEXCat6k=ciscoRFCapabilityV12R0111bEXCat6k, PYSNMP_MODULE_ID=ciscoRFCapability, ciscoRFCapabilityV12R01=ciscoRFCapabilityV12R01, ciscoRFCapabilityCatOSV8R0101Cat6K=ciscoRFCapabilityCatOSV8R0101Cat6K, ciscoRFCapability=ciscoRFCapability)
