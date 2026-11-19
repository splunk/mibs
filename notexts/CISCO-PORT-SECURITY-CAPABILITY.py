#
# PySNMP MIB module CISCO-PORT-SECURITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-SECURITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
ciscoPortSecurityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 393))
ciscoPortSecurityCapability.setRevisions(('2005-07-14 00:00', '2004-03-07 00:00',))
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setLastUpdated('200507140000Z')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setOrganization('Cisco Systems, Inc.')
ciscoPortSecurityC6kCapV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 393, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortSecurityC6kCapV08R0301 = ciscoPortSecurityC6kCapV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortSecurityC6kCapV08R0301 = ciscoPortSecurityC6kCapV08R0301.setStatus('current')
ciscoPSecureCapV12R0218SXFPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 393, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPSecureCapV12R0218SXFPCat6K = ciscoPSecureCapV12R0218SXFPCat6K.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPSecureCapV12R0218SXFPCat6K = ciscoPSecureCapV12R0218SXFPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-SECURITY-CAPABILITY", ciscoPortSecurityCapability=ciscoPortSecurityCapability, ciscoPortSecurityC6kCapV08R0301=ciscoPortSecurityC6kCapV08R0301, ciscoPSecureCapV12R0218SXFPCat6K=ciscoPSecureCapV12R0218SXFPCat6K, PYSNMP_MODULE_ID=ciscoPortSecurityCapability)
