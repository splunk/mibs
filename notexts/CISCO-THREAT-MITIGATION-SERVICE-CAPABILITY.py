#
# PySNMP MIB module CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
mibBuilder.exportSymbols("CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY", ciscoTmsCapIOSV12R05T=ciscoTmsCapIOSV12R05T, ciscoThreatMitigationServiceCapability=ciscoThreatMitigationServiceCapability, PYSNMP_MODULE_ID=ciscoThreatMitigationServiceCapability, ciscoTmsCapIOSV12R02S=ciscoTmsCapIOSV12R02S)
