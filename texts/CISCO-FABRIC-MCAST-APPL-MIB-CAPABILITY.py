#
# PySNMP MIB module CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoFabricMcastApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 510))
ciscoFabricMcastApplCapability.setRevisions(('2006-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-fabric@cisco.com')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setDescription('The capabilities description of\n                 CISCO-FABRIC-MCAST-APPL-MIB.')
cfmaCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 510, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setStatus('current')
if mibBuilder.loadTexts: cfmaCapabilityIOSXRV3R03.setDescription('CISCO-FABRIC-MCAST-APPL-MIB\n                        capabilities for IOS XR release 3.3')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY", cfmaCapabilityIOSXRV3R03=cfmaCapabilityIOSXRV3R03, PYSNMP_MODULE_ID=ciscoFabricMcastApplCapability, ciscoFabricMcastApplCapability=ciscoFabricMcastApplCapability)
