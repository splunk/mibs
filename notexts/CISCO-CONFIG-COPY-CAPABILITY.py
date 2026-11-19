#
# PySNMP MIB module CISCO-CONFIG-COPY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CONFIG-COPY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ConfigCopyState, ConfigCopyProtocol, ConfigFileType, ConfigCopyFailCause = mibBuilder.importSymbols("CISCO-CONFIG-COPY-MIB", "ConfigCopyState", "ConfigCopyProtocol", "ConfigFileType", "ConfigCopyFailCause")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoConfigCopyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 128))
ciscoConfigCopyCapability.setRevisions(('2006-02-08 00:00', '2005-05-24 00:00', '2004-06-08 00:00', '2004-03-17 00:00', '2002-04-29 00:00', '2000-09-06 00:00', '1999-10-07 00:00',))
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setOrganization('Cisco Systems, Inc.')
ciscoConfigCopyCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R00 = ciscoConfigCopyCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R00 = ciscoConfigCopyCapabilityV12R00.setStatus('current')
ciscoConfigCopyCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R01 = ciscoConfigCopyCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R01 = ciscoConfigCopyCapabilityV12R01.setStatus('current')
ciscoConfigCopyCapabilityV2R0175 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV2R0175 = ciscoConfigCopyCapabilityV2R0175.setProductRelease('MGX8850 Release 2.1.75')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV2R0175 = ciscoConfigCopyCapabilityV2R0175.setStatus('current')
ciscoConfigCopyCapabilityV12R30S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R30S = ciscoConfigCopyCapabilityV12R30S.setProductRelease('Cisco IOS 12.30S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R30S = ciscoConfigCopyCapabilityV12R30S.setStatus('current')
ciscoConfigCopyCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapCatOSV08R0401 = ciscoConfigCopyCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapCatOSV08R0401 = ciscoConfigCopyCapCatOSV08R0401.setStatus('current')
ciscoConfigCopyCapMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapMDS3R0 = ciscoConfigCopyCapMDS3R0.setProductRelease('Cisco MDS 3.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapMDS3R0 = ciscoConfigCopyCapMDS3R0.setStatus('current')
ciscoConfigCopyCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapIOSXRV2R0CRS1 = ciscoConfigCopyCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapIOSXRV2R0CRS1 = ciscoConfigCopyCapIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONFIG-COPY-CAPABILITY", ciscoConfigCopyCapIOSXRV2R0CRS1=ciscoConfigCopyCapIOSXRV2R0CRS1, ciscoConfigCopyCapCatOSV08R0401=ciscoConfigCopyCapCatOSV08R0401, ciscoConfigCopyCapMDS3R0=ciscoConfigCopyCapMDS3R0, PYSNMP_MODULE_ID=ciscoConfigCopyCapability, ciscoConfigCopyCapabilityV2R0175=ciscoConfigCopyCapabilityV2R0175, ciscoConfigCopyCapabilityV12R01=ciscoConfigCopyCapabilityV12R01, ciscoConfigCopyCapabilityV12R30S=ciscoConfigCopyCapabilityV12R30S, ciscoConfigCopyCapabilityV12R00=ciscoConfigCopyCapabilityV12R00, ciscoConfigCopyCapability=ciscoConfigCopyCapability)
