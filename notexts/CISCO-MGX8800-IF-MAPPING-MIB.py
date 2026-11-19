#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX8800-IF-MAPPING-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMGX8800IfMappingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 7))
ciscoMGX8800IfMappingMIB.setRevisions(('2004-05-25 00:00', '2004-04-30 00:00', '2003-12-04 00:00', '2003-03-20 00:00', '2002-10-21 00:00', '2002-10-16 00:00', '2002-05-21 00:00', '2002-02-17 00:00', '2001-10-16 00:00', '2001-07-08 00:00', '2000-02-12 00:00',))
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setLastUpdated('200405250000Z')
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setOrganization('Cisco Systems, Inc.')
class CmimIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("physicalLine", 1), ("atmIma", 2), ("atm", 3), ("atmVirtual", 4), ("ds1Inds3", 5), ("adjCardApsLine", 6), ("propAtm", 7), ("sonetVT", 8), ("imaGrpAtmPhy", 9), ("srmBertLine", 10), ("srmBertPort", 11), ("sonetPath", 12), ("ds3SonetPath", 13), ("atmSonetPath", 14), ("atmDs3SonetPath", 15), ("frameRelayPort", 16), ("ces", 17), ("ds1VTPath", 18), ("ds1Ds3SonetPath", 19), ("atmVciEndPt", 20), ("mfrBundle", 21), ("ppplink", 22), ("pppMpbundle", 23), ("lapd", 24))

cmimMappingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 1))
cmimPhysToIf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1))
cmimPhysToIfTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1), )
if mibBuilder.loadTexts: cmimPhysToIfTable.setStatus('current')
cmimPhysToIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimModuleIndex"), (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfNumber"), (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfType"))
if mibBuilder.loadTexts: cmimPhysToIfEntry.setStatus('current')
cmimModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cmimModuleIndex.setStatus('current')
cmimIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cmimIfNumber.setStatus('current')
cmimIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 3), CmimIfType())
if mibBuilder.loadTexts: cmimIfType.setStatus('current')
cmimIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmimIfIndex.setStatus('current')
cmimPhysToIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3))
cmimPhysToIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1))
cmimPhysToIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2))
cmimPhysToIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1, 1)).setObjects(("CISCO-MGX8800-IF-MAPPING-MIB", "cmimPhysToIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmimPhysToIfMIBCompliance = cmimPhysToIfMIBCompliance.setStatus('current')
cmimPhysToIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2, 1)).setObjects(("CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmimPhysToIfMIBGroup = cmimPhysToIfMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-MIB", cmimPhysToIfMIBGroups=cmimPhysToIfMIBGroups, ciscoMGX8800IfMappingMIB=ciscoMGX8800IfMappingMIB, PYSNMP_MODULE_ID=ciscoMGX8800IfMappingMIB, cmimPhysToIfTable=cmimPhysToIfTable, cmimPhysToIf=cmimPhysToIf, cmimIfNumber=cmimIfNumber, cmimPhysToIfEntry=cmimPhysToIfEntry, cmimIfType=cmimIfType, cmimPhysToIfMIBGroup=cmimPhysToIfMIBGroup, cmimPhysToIfMIBCompliances=cmimPhysToIfMIBCompliances, cmimIfIndex=cmimIfIndex, cmimMappingObjects=cmimMappingObjects, cmimPhysToIfMIBCompliance=cmimPhysToIfMIBCompliance, cmimModuleIndex=cmimModuleIndex, CmimIfType=CmimIfType, cmimPhysToIfMIBConformance=cmimPhysToIfMIBConformance)
