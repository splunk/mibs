#
# PySNMP MIB module CISCO-SIP-UA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SIP-UA-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSipUaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 172))
ciscoSipUaCapability.setRevisions(('2005-06-22 00:00', '2003-07-30 00:00', '2003-03-21 00:00', '2001-09-26 00:00', '2001-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSipUaCapability.setRevisionsDescriptions(('Adding AGENT-CAPABILITIES clause for IOS\n                         12.4(2)T.', 'Adding AGENT-CAPABILITIES clauses for IOS\n                         12.3(2).', 'Adding AGENT-CAPABILITIES clauses for IOS\n                         12.2(8), 12.2(11) & 12.2(15).', 'Adding AGENT-CAPABILITIES clause for IOS\n                         12.2(2).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSipUaCapability.setLastUpdated('200506220000Z')
if mibBuilder.loadTexts: ciscoSipUaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSipUaCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-sip@cisco.com')
if mibBuilder.loadTexts: ciscoSipUaCapability.setDescription('Agent capabilities for the CISCO-SIP-UA-MIB.')
ciscoSipUaCapabilityV12R0202 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setProductRelease('Cisco IOS 12.2(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0202.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0208 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setProductRelease('Cisco IOS 12.2(8).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0208.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0211 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setProductRelease('Cisco IOS 12.2(11).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0211.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0215 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setProductRelease('Cisco IOS 12.2(15).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0215.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0302 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setProductRelease('Cisco IOS 12.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0302.setDescription('IOS 12.3 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0402T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setProductRelease('Cisco IOS 12.4(2)T.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0402T.setDescription('IOS 12.4(2)T Cisco SIP User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SIP-UA-CAPABILITY", ciscoSipUaCapabilityV12R0302=ciscoSipUaCapabilityV12R0302, ciscoSipUaCapability=ciscoSipUaCapability, ciscoSipUaCapabilityV12R0215=ciscoSipUaCapabilityV12R0215, ciscoSipUaCapabilityV12R0402T=ciscoSipUaCapabilityV12R0402T, PYSNMP_MODULE_ID=ciscoSipUaCapability, ciscoSipUaCapabilityV12R0202=ciscoSipUaCapabilityV12R0202, ciscoSipUaCapabilityV12R0208=ciscoSipUaCapabilityV12R0208, ciscoSipUaCapabilityV12R0211=ciscoSipUaCapabilityV12R0211)
