#
# PySNMP MIB module CISCO-CONTEXT-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CONTEXT-MAPPING-CAPABILITY
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
ciscoContextMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 564))
ciscoContextMappingCapability.setRevisions(('2008-08-22 00:00', '2008-03-24 00:00', '2005-05-20 00:00',))
if mibBuilder.loadTexts: ciscoContextMappingCapability.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setOrganization('Cisco Systems, Inc.')
ciscoContextMappingCapV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setStatus('current')
ciscoContextMappingCapV12R02SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setProductRelease('Cisco IOS 12.2SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setStatus('current')
ciscoContextMappingIOSXRV3R7FCICRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setProductRelease('Cisco IOS XR 3.7FCI for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONTEXT-MAPPING-CAPABILITY", ciscoContextMappingIOSXRV3R7FCICRS1=ciscoContextMappingIOSXRV3R7FCICRS1, ciscoContextMappingCapV12R02SG=ciscoContextMappingCapV12R02SG, ciscoContextMappingCapV12R02S=ciscoContextMappingCapV12R02S, ciscoContextMappingCapability=ciscoContextMappingCapability, PYSNMP_MODULE_ID=ciscoContextMappingCapability)
