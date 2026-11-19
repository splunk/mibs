#
# PySNMP MIB module CISCO-ENHANCED-IMAGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENHANCED-IMAGE-CAPABILITY
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
ceImageCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 474))
ceImageCapability.setRevisions(('2005-12-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ceImageCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ceImageCapability.setLastUpdated('200512290000Z')
if mibBuilder.loadTexts: ceImageCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ceImageCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com\n                        cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ceImageCapability.setDescription('Agent capabilities for CISCO-ENHANCED-IMAGE-MIB')
ceImageCapabilityIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 474, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceImageCapabilityIOSXRV3R2R0CRS1 = ceImageCapabilityIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceImageCapabilityIOSXRV3R2R0CRS1 = ceImageCapabilityIOSXRV3R2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ceImageCapabilityIOSXRV3R2R0CRS1.setDescription('CISCO-ENHANCED-IMAGE-MIB capabilities\n                         for IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-ENHANCED-IMAGE-CAPABILITY", ceImageCapability=ceImageCapability, ceImageCapabilityIOSXRV3R2R0CRS1=ceImageCapabilityIOSXRV3R2R0CRS1, PYSNMP_MODULE_ID=ceImageCapability)
