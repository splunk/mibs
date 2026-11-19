#
# PySNMP MIB module CISCO-ENTITY-ASSET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-ASSET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-ENTITY-ASSET-CAPABILITY", ceAssetCapV12R0214SXCat6K=ceAssetCapV12R0214SXCat6K, ciscoEntityAssetCapability=ciscoEntityAssetCapability, PYSNMP_MODULE_ID=ciscoEntityAssetCapability, ceAssetCapabilityV4R00=ceAssetCapabilityV4R00, ceAssetCapCatOSV08R0101Cat6K=ceAssetCapCatOSV08R0101Cat6K)
