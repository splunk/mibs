#
# PySNMP MIB module CISCO-VISM-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
vismPort, = mibBuilder.importSymbols("BASIS-MIB", "vismPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 92))
ciscoVismPortMIB.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: ciscoVismPortMIB.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: ciscoVismPortMIB.setOrganization('Cisco Systems, Inc.')
vismPortCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1))
vismPortCnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1), )
if mibBuilder.loadTexts: vismPortCnfGrpTable.setStatus('current')
vismPortCnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1), ).setIndexNames((0, "CISCO-VISM-PORT-MIB", "vismPortNum"))
if mibBuilder.loadTexts: vismPortCnfGrpEntry.setStatus('current')
vismPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortNum.setStatus('current')
vismPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortRowStatus.setStatus('current')
vismPortLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortLineNum.setStatus('current')
vismPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("voIP", 1), ("userPort", 2))).clone('voIP')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortType.setStatus('current')
vismPortDs0ConfigBitMap = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortDs0ConfigBitMap.setStatus('current')
vismPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5651320)).clone(5651320)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortSpeed.setStatus('current')
vismPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notConfigured", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortState.setStatus('current')
ciscoVismPortMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 92, 2))
ciscoVismPortMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 1))
ciscoVismPortMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 2))
ciscoVismPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 2, 1)).setObjects(("CISCO-VISM-PORT-MIB", "ciscoVismPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismPortCompliance = ciscoVismPortCompliance.setStatus('current')
ciscoVismPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 1, 1)).setObjects(("CISCO-VISM-PORT-MIB", "vismPortNum"), ("CISCO-VISM-PORT-MIB", "vismPortRowStatus"), ("CISCO-VISM-PORT-MIB", "vismPortLineNum"), ("CISCO-VISM-PORT-MIB", "vismPortType"), ("CISCO-VISM-PORT-MIB", "vismPortDs0ConfigBitMap"), ("CISCO-VISM-PORT-MIB", "vismPortSpeed"), ("CISCO-VISM-PORT-MIB", "vismPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismPortGroup = ciscoVismPortGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-PORT-MIB", vismPortDs0ConfigBitMap=vismPortDs0ConfigBitMap, vismPortNum=vismPortNum, ciscoVismPortMIB=ciscoVismPortMIB, vismPortCnfGrpEntry=vismPortCnfGrpEntry, vismPortLineNum=vismPortLineNum, ciscoVismPortGroup=ciscoVismPortGroup, vismPortType=vismPortType, PYSNMP_MODULE_ID=ciscoVismPortMIB, vismPortCnfGrpTable=vismPortCnfGrpTable, vismPortState=vismPortState, vismPortRowStatus=vismPortRowStatus, vismPortCnfGrp=vismPortCnfGrp, ciscoVismPortCompliance=ciscoVismPortCompliance, vismPortSpeed=vismPortSpeed, ciscoVismPortMIBConformance=ciscoVismPortMIBConformance, ciscoVismPortMIBGroups=ciscoVismPortMIBGroups, ciscoVismPortMIBCompliances=ciscoVismPortMIBCompliances)
