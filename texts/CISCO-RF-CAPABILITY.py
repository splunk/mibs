#
# PySNMP MIB module CISCO-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RF-CAPABILITY
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
ciscoRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoRFCapability.setRevisions(('2003-08-20 00:00', '2001-01-04 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFCapability.setRevisionsDescriptions(('Added ciscoRFCapabilityV12R0111bEXCat6k,\n         ciscoRFCapabilityV12R0113ECat6k, and\n         ciscoRFCapabilityCatOSV8R0101Cat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFCapability.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: ciscoRFCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFCapability.setContactInfo('Cisco Systems Customer Service\n         Postal: 170 West Tasman Drive\n                 San Jose, CA 95134\n                 USA\n         Tel: +1 800 553-NETS\n\n         E-mail: cs-rf-mib@cisco.com\n        ')
if mibBuilder.loadTexts: ciscoRFCapability.setDescription('Added agent Capabilities for CISCO-RF-MIB shipped as part of\n         the Cisco IOS 12.1 release.\n        ')
ciscoRFCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityV12R01.setDescription('Cisco RF MIB capabilities')
ciscoRFCapabilityV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11bEX) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityV12R0111bEXCat6k.setDescription('CISCO-RF-MIB capabilities.')
ciscoRFCapabilityV12R0113ECat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityV12R0113ECat6k.setDescription('CISCO-RF-MIB capabilities.')
ciscoRFCapabilityCatOSV8R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityCatOSV8R0101Cat6K.setDescription('CISCO-RF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RF-CAPABILITY", ciscoRFCapabilityV12R0113ECat6k=ciscoRFCapabilityV12R0113ECat6k, PYSNMP_MODULE_ID=ciscoRFCapability, ciscoRFCapabilityV12R0111bEXCat6k=ciscoRFCapabilityV12R0111bEXCat6k, ciscoRFCapabilityCatOSV8R0101Cat6K=ciscoRFCapabilityCatOSV8R0101Cat6K, ciscoRFCapabilityV12R01=ciscoRFCapabilityV12R01, ciscoRFCapability=ciscoRFCapability)
