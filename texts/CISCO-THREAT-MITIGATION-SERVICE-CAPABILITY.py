#
# PySNMP MIB module CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoThreatMitigationServiceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 532))
ciscoThreatMitigationServiceCapability.setRevisions(('2007-05-17 00:00', '2007-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setRevisionsDescriptions(('Added the agent capabilities statement for\n        ciscoTmsCapIOSV12R05T.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setLastUpdated('200705170000Z')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-tms@cisco.com')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setDescription('Agent capabilities for\n        CISCO-THREAT-MITIGATION-SERVICE-MIB.')
ciscoTmsCapIOSV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setProductRelease('Cisco IOS 12.2S ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoTmsCapIOSV12R02S.setDescription('CISCO-THREAT-MITIGATION-SERVICE-MIB capabilities.')
ciscoTmsCapIOSV12R05T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setProductRelease('Cisco IOS 12.5T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setStatus('current')
if mibBuilder.loadTexts: ciscoTmsCapIOSV12R05T.setDescription('CISCO-THREAT-MITIGATION-SERVICE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY", ciscoThreatMitigationServiceCapability=ciscoThreatMitigationServiceCapability, PYSNMP_MODULE_ID=ciscoThreatMitigationServiceCapability, ciscoTmsCapIOSV12R02S=ciscoTmsCapIOSV12R02S, ciscoTmsCapIOSV12R05T=ciscoTmsCapIOSV12R05T)
