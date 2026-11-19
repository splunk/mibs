#
# PySNMP MIB module CISCO-ATM-VIRTUAL-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-VIRTUAL-IF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
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
ciscoAtmVirtualIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 279))
ciscoAtmVirtualIfCapability.setRevisions(('2005-11-14 00:00', '2003-09-10 00:00', '2003-03-24 00:00', '2002-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setRevisionsDescriptions(('Updated the imports such that Unsigned32 is imported from \n                SNMPv2-SMI instead of CISCO-TC.', 'Added cavIfCapabilityV5R00 for \n                 MPSM155 service module in Release 5.0.00', 'Added cavIfCapabilityV4R00 for :\n                 Service Modules AXSM-XG, AXSM-E and \n                 Processor Switch Module PXM1E in \n                 Release 4.0.00', 'Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setDescription('The Agent Capabilities for \n                CISCO-ATM-VIRTUAL-IF-MIB.\n  \n                - cavIfCapmVirtualIfCapabilityV2R00 is\n                  for AXSM module in Release 2.0.\n\n                - cavIfCapabilityAxsmV2R0010 is\n                  for AXSM Service Module in Release 2.0.10.       \n\n                - cavIfCapabilityAxsmeV2R0160 is\n                  for AXSM-E Service Module in Release 2.1.60.')
cavIfCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityAxsmV2R00.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for\n                 AXSM Service Module.')
cavIfCapabilityAxsmV2R0010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setProductRelease('MGX8850 Release 2.0.10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityAxsmV2R0010.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for\n                AXSM Service Module.')
cavIfCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityAxsmeV2R0160.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for\n                 Enhanced AXSM (AXSM-E)module.')
cavIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityV4R00.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for\n                 10 Gig. AXSM module (AXSM-XG), \n                 Enhanced AXSM module (AXSM-E) and\n                 Processor Switch Module Enhanced(PXM1E)\n                 controller card.')
cavIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setProductRelease('MGX8950, MGX8850 Release 5.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityV5R00.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for\n                 MPSM155 service module.')
mibBuilder.exportSymbols("CISCO-ATM-VIRTUAL-IF-CAPABILITY", cavIfCapabilityAxsmV2R0010=cavIfCapabilityAxsmV2R0010, cavIfCapabilityV4R00=cavIfCapabilityV4R00, cavIfCapabilityV5R00=cavIfCapabilityV5R00, cavIfCapabilityAxsmeV2R0160=cavIfCapabilityAxsmeV2R0160, ciscoAtmVirtualIfCapability=ciscoAtmVirtualIfCapability, PYSNMP_MODULE_ID=ciscoAtmVirtualIfCapability, cavIfCapabilityAxsmV2R00=cavIfCapabilityAxsmV2R00)
