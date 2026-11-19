#
# PySNMP MIB module CISCO-CDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CDP-CAPABILITY
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
ciscoCdpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 43))
ciscoCdpCapability.setRevisions(('2007-07-18 00:00', '2006-10-26 00:00', '2006-02-06 00:00', '2005-05-24 00:00', '2003-09-03 00:00',))
if mibBuilder.loadTexts: ciscoCdpCapability.setLastUpdated('200707180000Z')
if mibBuilder.loadTexts: ciscoCdpCapability.setOrganization('Cisco Systems, Inc.')
ciscoCdpCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0111bEXCat6K = ciscoCdpCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0111bEXCat6K = ciscoCdpCapV12R0111bEXCat6K.setStatus('current')
ciscoCdpCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0217SXCat6K = ciscoCdpCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n\n                     and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0217SXCat6K = ciscoCdpCapV12R0217SXCat6K.setStatus('current')
ciscoCdpCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat6K = ciscoCdpCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n\n                     and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat6K = ciscoCdpCapCatOSV08R0101Cat6K.setStatus('current')
ciscoCdpCapCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat4K = ciscoCdpCapCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat4K = ciscoCdpCapCatOSV08R0101Cat4K.setStatus('current')
ciscoCdpCapSanOSV03R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapSanOSV03R0001 = ciscoCdpCapSanOSV03R0001.setProductRelease('Cisco SAN-OS 3.0(1) on MDS platform.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapSanOSV03R0001 = ciscoCdpCapSanOSV03R0001.setStatus('current')
ciscoCdpCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapIOSXRV2R0CRS1 = ciscoCdpCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapIOSXRV2R0CRS1 = ciscoCdpCapIOSXRV2R0CRS1.setStatus('current')
ciscoCdpCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTSV100 = ciscoCdpCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTSV100 = ciscoCdpCapCTSV100.setStatus('current')
ciscoCdpCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTMV1000 = ciscoCdpCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTMV1000 = ciscoCdpCapCTMV1000.setStatus('current')
ciscoCdpCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0233SXHPCat6K = ciscoCdpCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0233SXHPCat6K = ciscoCdpCapV12R0233SXHPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDP-CAPABILITY", ciscoCdpCapCatOSV08R0101Cat6K=ciscoCdpCapCatOSV08R0101Cat6K, ciscoCdpCapCatOSV08R0101Cat4K=ciscoCdpCapCatOSV08R0101Cat4K, ciscoCdpCapIOSXRV2R0CRS1=ciscoCdpCapIOSXRV2R0CRS1, ciscoCdpCapV12R0111bEXCat6K=ciscoCdpCapV12R0111bEXCat6K, ciscoCdpCapV12R0233SXHPCat6K=ciscoCdpCapV12R0233SXHPCat6K, ciscoCdpCapCTSV100=ciscoCdpCapCTSV100, ciscoCdpCapSanOSV03R0001=ciscoCdpCapSanOSV03R0001, PYSNMP_MODULE_ID=ciscoCdpCapability, ciscoCdpCapability=ciscoCdpCapability, ciscoCdpCapCTMV1000=ciscoCdpCapCTMV1000, ciscoCdpCapV12R0217SXCat6K=ciscoCdpCapV12R0217SXCat6K)
