#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SVI-AUTOSTATE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoSVIAutostateCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 384))
ciscoSVIAutostateCapability.setRevisions(('2004-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setLastUpdated('200404080000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setDescription('The capabilities description of\n                 CISCO-SVI-AUTOSTATE-MIB.')
csaCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setStatus('current')
if mibBuilder.loadTexts: csaCapabilityCatOSV08R0301Cat6k.setDescription('CISCO-SVI-AUTOSTATE-MIB capabilities.')
csaCapabilityV12R0218SXDCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setStatus('current')
if mibBuilder.loadTexts: csaCapabilityV12R0218SXDCat6k.setDescription('CISCO-SVI-AUTOSTATE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-CAPABILITY", PYSNMP_MODULE_ID=ciscoSVIAutostateCapability, csaCapabilityCatOSV08R0301Cat6k=csaCapabilityCatOSV08R0301Cat6k, ciscoSVIAutostateCapability=ciscoSVIAutostateCapability, csaCapabilityV12R0218SXDCat6k=csaCapabilityV12R0218SXDCat6k)
