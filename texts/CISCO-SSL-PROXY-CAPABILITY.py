#
# PySNMP MIB module CISCO-SSL-PROXY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SSL-PROXY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
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
ciscoSslProxyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 364))
ciscoSslProxyCapability.setRevisions(('2008-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSslProxyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSslProxyCapability.setLastUpdated('200804080000Z')
if mibBuilder.loadTexts: ciscoSslProxyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSslProxyCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:    +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com, cs-ssl@cisco.com')
if mibBuilder.loadTexts: ciscoSslProxyCapability.setDescription('Agent capabilities for the CISCO-SSL-PROXY-MIB')
ciscoSslProxyCapCat6KV02R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 364, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapCat6KV02R01 = ciscoSslProxyCapCat6KV02R01.setProductRelease('Cisco Catalyst 6000 SSL Module Release 2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapCat6KV02R01 = ciscoSslProxyCapCat6KV02R01.setStatus('current')
if mibBuilder.loadTexts: ciscoSslProxyCapCat6KV02R01.setDescription('MIB Agent Capability of Cisco Catalyst 6000 SSL Module\n        Release 2.1')
ciscoSslProxyCapACSWV03RA3006 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 364, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapACSWV03RA3006 = ciscoSslProxyCapACSWV03RA3006.setProductRelease('ACSW (Application Control Software) 3.0(0)A3(0.0.6)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapACSWV03RA3006 = ciscoSslProxyCapACSWV03RA3006.setStatus('current')
if mibBuilder.loadTexts: ciscoSslProxyCapACSWV03RA3006.setDescription('ACSW (Application Control Software) 3.0(0)A3(0.0.6)\n        CISCO-SSL-PROXY-MIB capabilities')
mibBuilder.exportSymbols("CISCO-SSL-PROXY-CAPABILITY", ciscoSslProxyCapability=ciscoSslProxyCapability, ciscoSslProxyCapACSWV03RA3006=ciscoSslProxyCapACSWV03RA3006, PYSNMP_MODULE_ID=ciscoSslProxyCapability, ciscoSslProxyCapCat6KV02R01=ciscoSslProxyCapCat6KV02R01)
