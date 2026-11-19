#
# PySNMP MIB module CISCO-FLASH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FLASH-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoFlashCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 222))
ciscoFlashCapability.setRevisions(('2008-01-18 00:00', '2004-04-01 00:00', '2003-10-21 00:00', '2001-09-25 12:34',))
if mibBuilder.loadTexts: ciscoFlashCapability.setLastUpdated('200801180000Z')
if mibBuilder.loadTexts: ciscoFlashCapability.setOrganization('Cisco Systems, Inc.')
ciscoFlashCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setStatus('current')
ciscoFlashCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setStatus('current')
ciscoFlashCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setStatus('current')
ciscoFlashMibCapCatOSV7R0501Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setProductRelease('Cisco CatOS 7.5(1) on  Catalyst 4000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setStatus('current')
ciscoFlashMibCapCatOSV7R0501Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setStatus('current')
ciscoFlashMibCapV12R0113ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500 and Cisco\n                7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setStatus('current')
ciscoFlashMibCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1)on Catalyst 6000/6500\n                and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setStatus('current')
ciscoFlashMibCapXRV03R06PCRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLASH-CAPABILITY", PYSNMP_MODULE_ID=ciscoFlashCapability, ciscoFlashMibCapCatOSV7R0501Cat6k=ciscoFlashMibCapCatOSV7R0501Cat6k, ciscoFlashCapabilityV12R01=ciscoFlashCapabilityV12R01, ciscoFlashMibCapCatOSV08R0301=ciscoFlashMibCapCatOSV08R0301, ciscoFlashMibCapXRV03R06PCRS1=ciscoFlashMibCapXRV03R06PCRS1, ciscoFlashCapabilityV12R00S=ciscoFlashCapabilityV12R00S, ciscoFlashMibCapCatOSV7R0501Cat4k=ciscoFlashMibCapCatOSV7R0501Cat4k, ciscoFlashMibCapV12R0113ECat6K=ciscoFlashMibCapV12R0113ECat6K, ciscoFlashCapabilityV12R02=ciscoFlashCapabilityV12R02, ciscoFlashCapability=ciscoFlashCapability)
