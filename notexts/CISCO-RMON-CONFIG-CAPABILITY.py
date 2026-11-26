#
# PySNMP MIB module CISCO-RMON-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RMON-CONFIG-CAPABILITY
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
ciscoRmonConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 346))
ciscoRmonConfigCapability.setRevisions(('2008-10-28 00:00', '2008-05-09 00:00', '2007-06-28 00:00', '2006-01-18 00:00', '2005-08-24 10:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setLastUpdated('200810280000Z')
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setOrganization('Cisco Systems, Inc.')
ciscoRmonConfigCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapV12R0111ECat6K = ciscoRmonConfigCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapV12R0111ECat6K = ciscoRmonConfigCapV12R0111ECat6K.setStatus('current')
ciscoRmonConfigCapCatOSV6R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV6R0301 = ciscoRmonConfigCapCatOSV6R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV6R0301 = ciscoRmonConfigCapCatOSV6R0301.setStatus('current')
ciscoRmonConfigCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV08R0501 = ciscoRmonConfigCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV08R0501 = ciscoRmonConfigCapCatOSV08R0501.setStatus('current')
crcCapV12R0218SXDPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXDPCat6k = crcCapV12R0218SXDPCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXDPCat6k = crcCapV12R0218SXDPCat6k.setStatus('current')
crcCapV12R0218SXEPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXEPCat6k = crcCapV12R0218SXEPCat6k.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXEPCat6k = crcCapV12R0218SXEPCat6k.setStatus('current')
crcCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXHPCat6k = crcCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXHPCat6k = crcCapV12R0233SXHPCat6k.setStatus('current')
ciscoRmonConfigCapSanOSV34R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapSanOSV34R1 = ciscoRmonConfigCapSanOSV34R1.setProductRelease('Cisco SanOS 3.4(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapSanOSV34R1 = ciscoRmonConfigCapSanOSV34R1.setStatus('current')
crcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXIPCat6K = crcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXIPCat6K = crcCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON-CONFIG-CAPABILITY", ciscoRmonConfigCapV12R0111ECat6K=ciscoRmonConfigCapV12R0111ECat6K, ciscoRmonConfigCapCatOSV08R0501=ciscoRmonConfigCapCatOSV08R0501, ciscoRmonConfigCapCatOSV6R0301=ciscoRmonConfigCapCatOSV6R0301, crcCapV12R0218SXEPCat6k=crcCapV12R0218SXEPCat6k, ciscoRmonConfigCapability=ciscoRmonConfigCapability, ciscoRmonConfigCapSanOSV34R1=ciscoRmonConfigCapSanOSV34R1, crcCapV12R0233SXIPCat6K=crcCapV12R0233SXIPCat6K, crcCapV12R0233SXHPCat6k=crcCapV12R0233SXHPCat6k, crcCapV12R0218SXDPCat6k=crcCapV12R0218SXDPCat6k, PYSNMP_MODULE_ID=ciscoRmonConfigCapability)
