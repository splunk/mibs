#
# PySNMP MIB module CISCO-SSL-PROXY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SSL-PROXY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-SSL-PROXY-CAPABILITY", PYSNMP_MODULE_ID=ciscoSslProxyCapability, ciscoSslProxyCapACSWV03RA3006=ciscoSslProxyCapACSWV03RA3006, ciscoSslProxyCapability=ciscoSslProxyCapability, ciscoSslProxyCapCat6KV02R01=ciscoSslProxyCapCat6KV02R01)
