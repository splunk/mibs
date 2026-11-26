#
# PySNMP MIB module CISCO-PORT-SECURITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PORT-SECURITY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
