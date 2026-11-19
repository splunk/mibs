#
# PySNMP MIB module CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY
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
ciscoThreatMitigationServiceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 532))
ciscoThreatMitigationServiceCapability.setRevisions(('2007-05-17 00:00', '2007-01-29 00:00',))
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setLastUpdated('200705170000Z')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setOrganization('Cisco Systems, Inc.')
ciscoTmsCapIOSV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setProductRelease('Cisco IOS 12.2S ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setStatus('current')
ciscoTmsCapIOSV12R05T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setProductRelease('Cisco IOS 12.5T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setStatus('current')
mibBuilder.exportSymbols("CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY", ciscoTmsCapIOSV12R05T=ciscoTmsCapIOSV12R05T, ciscoTmsCapIOSV12R02S=ciscoTmsCapIOSV12R02S, ciscoThreatMitigationServiceCapability=ciscoThreatMitigationServiceCapability, PYSNMP_MODULE_ID=ciscoThreatMitigationServiceCapability)
