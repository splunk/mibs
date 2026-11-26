#
# PySNMP MIB module CISCO-MGX82XX-MODULE-RSRC-PART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX82XX-MODULE-RSRC-PART-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxModuleRsrcPartMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 73))
ciscoMgx82xxModuleRsrcPartMIB.setRevisions(('2003-04-18 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxModuleRsrcPartMIB.setLastUpdated('200304180000Z')
if mibBuilder.loadTexts: ciscoMgx82xxModuleRsrcPartMIB.setOrganization('Cisco Systems, Inc.')
cardResourcePartition = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 9))
cardLcnPartitionType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noPartition", 1), ("controllerBased", 2), ("portControllerBased", 3))).clone('noPartition')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardLcnPartitionType.setStatus('current')
cardResPartGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2), )
if mibBuilder.loadTexts: cardResPartGrpTable.setStatus('current')
cardResPartGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1), ).setIndexNames((0, "CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"))
if mibBuilder.loadTexts: cardResPartGrpEntry.setStatus('current')
cardResPartCtrlrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("par", 1), ("pnni", 2), ("tag", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardResPartCtrlrNum.setStatus('current')
cardResPartRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardResPartRowStatus.setStatus('current')
cardResPartNumOfLcnAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardResPartNumOfLcnAvail.setStatus('current')
cmmRsrcPartMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2))
cmmRsrcPartMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1))
cmmRsrcPartMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2))
cmmRsrcPartCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1, 1)).setObjects(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cmmRsrcPartGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmRsrcPartCompliance = cmmRsrcPartCompliance.setStatus('current')
cmmRsrcPartGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2, 1)).setObjects(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardLcnPartitionType"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartRowStatus"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartNumOfLcnAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmRsrcPartGroup = cmmRsrcPartGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", PYSNMP_MODULE_ID=ciscoMgx82xxModuleRsrcPartMIB, cardResPartNumOfLcnAvail=cardResPartNumOfLcnAvail, cmmRsrcPartGroup=cmmRsrcPartGroup, cmmRsrcPartMIBConformance=cmmRsrcPartMIBConformance, cmmRsrcPartMIBCompliances=cmmRsrcPartMIBCompliances, cardResPartGrpEntry=cardResPartGrpEntry, cardResPartRowStatus=cardResPartRowStatus, ciscoMgx82xxModuleRsrcPartMIB=ciscoMgx82xxModuleRsrcPartMIB, cmmRsrcPartCompliance=cmmRsrcPartCompliance, cardResPartGrpTable=cardResPartGrpTable, cardResPartCtrlrNum=cardResPartCtrlrNum, cardLcnPartitionType=cardLcnPartitionType, cmmRsrcPartMIBGroups=cmmRsrcPartMIBGroups, cardResourcePartition=cardResourcePartition)
