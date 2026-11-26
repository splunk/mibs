#
# PySNMP MIB module CISCO-ENTITY-ASSET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-ASSET-CAPABILITY
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
ciscoEntityAssetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 300))
ciscoEntityAssetCapability.setRevisions(('2003-09-04 00:00', '2003-04-30 00:00',))
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setLastUpdated('200309040000Z')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setOrganization('Cisco Systems, Inc.')
ceAssetCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapabilityV4R00 = ceAssetCapabilityV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapabilityV4R00 = ceAssetCapabilityV4R00.setStatus('current')
ceAssetCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapV12R0214SXCat6K = ceAssetCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapV12R0214SXCat6K = ceAssetCapV12R0214SXCat6K.setStatus('current')
ceAssetCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapCatOSV08R0101Cat6K = ceAssetCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapCatOSV08R0101Cat6K = ceAssetCapCatOSV08R0101Cat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-ASSET-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityAssetCapability, ceAssetCapabilityV4R00=ceAssetCapabilityV4R00, ceAssetCapV12R0214SXCat6K=ceAssetCapV12R0214SXCat6K, ceAssetCapCatOSV08R0101Cat6K=ceAssetCapCatOSV08R0101Cat6K, ciscoEntityAssetCapability=ciscoEntityAssetCapability)
