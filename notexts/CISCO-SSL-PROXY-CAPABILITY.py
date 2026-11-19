#
# PySNMP MIB module CISCO-SSL-PROXY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SSL-PROXY-CAPABILITY
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
ciscoSslProxyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 364))
ciscoSslProxyCapability.setRevisions(('2008-04-08 00:00',))
if mibBuilder.loadTexts: ciscoSslProxyCapability.setLastUpdated('200804080000Z')
if mibBuilder.loadTexts: ciscoSslProxyCapability.setOrganization('Cisco Systems, Inc.')
ciscoSslProxyCapCat6KV02R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 364, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapCat6KV02R01 = ciscoSslProxyCapCat6KV02R01.setProductRelease('Cisco Catalyst 6000 SSL Module Release 2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapCat6KV02R01 = ciscoSslProxyCapCat6KV02R01.setStatus('current')
ciscoSslProxyCapACSWV03RA3006 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 364, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapACSWV03RA3006 = ciscoSslProxyCapACSWV03RA3006.setProductRelease('ACSW (Application Control Software) 3.0(0)A3(0.0.6)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapACSWV03RA3006 = ciscoSslProxyCapACSWV03RA3006.setStatus('current')
mibBuilder.exportSymbols("CISCO-SSL-PROXY-CAPABILITY", PYSNMP_MODULE_ID=ciscoSslProxyCapability, ciscoSslProxyCapACSWV03RA3006=ciscoSslProxyCapACSWV03RA3006, ciscoSslProxyCapCat6KV02R01=ciscoSslProxyCapCat6KV02R01, ciscoSslProxyCapability=ciscoSslProxyCapability)
