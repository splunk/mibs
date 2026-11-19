#
# PySNMP MIB module CISCO-ATM-CELL-LAYER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-CELL-LAYER-CAPABILITY
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
ciscoAtmCellLayerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 275))
ciscoAtmCellLayerCapability.setRevisions(('2003-01-30 00:00', '2002-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setRevisionsDescriptions(('Added cacLayerCapabilityAxsmxgV4R00.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setLastUpdated('200301300000Z')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setDescription('The Agent Capabilities for \n            CISCO-ATM-CELL-LAYER-MIB.\n\n            - cacLayerCapabilityAxsmV2R00 is for\n              ATM Switch Service Module(AXSM).\n\n            - cacLayerCapabilityAxsmeV2R0160 is for\n              Enhanced AXSM(AXSM-E).\n\n            - cacLayerCapabilityAxsmxgV4R00 is for\n              10 Gig. AXSM(AXSM-XG).')
cacLayerCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmV2R00.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for\n                AXSM Service Module.')
cacLayerCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmeV2R0160.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for\n                Enhanced AXSM(AXSM-E) Service Module.')
cacLayerCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmxgV4R00.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for\n                10 Gig. AXSM Service Module (AXSM-XG).')
mibBuilder.exportSymbols("CISCO-ATM-CELL-LAYER-CAPABILITY", cacLayerCapabilityAxsmeV2R0160=cacLayerCapabilityAxsmeV2R0160, PYSNMP_MODULE_ID=ciscoAtmCellLayerCapability, ciscoAtmCellLayerCapability=ciscoAtmCellLayerCapability, cacLayerCapabilityAxsmV2R00=cacLayerCapabilityAxsmV2R00, cacLayerCapabilityAxsmxgV4R00=cacLayerCapabilityAxsmxgV4R00)
