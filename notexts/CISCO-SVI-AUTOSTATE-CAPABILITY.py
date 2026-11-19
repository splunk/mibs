#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SVI-AUTOSTATE-CAPABILITY
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
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoSVIAutostateCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 384))
ciscoSVIAutostateCapability.setRevisions(('2004-04-08 00:00',))
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setLastUpdated('200404080000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setOrganization('Cisco Systems, Inc.')
csaCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setStatus('current')
csaCapabilityV12R0218SXDCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-CAPABILITY", csaCapabilityV12R0218SXDCat6k=csaCapabilityV12R0218SXDCat6k, PYSNMP_MODULE_ID=ciscoSVIAutostateCapability, csaCapabilityCatOSV08R0301Cat6k=csaCapabilityCatOSV08R0301Cat6k, ciscoSVIAutostateCapability=ciscoSVIAutostateCapability)
