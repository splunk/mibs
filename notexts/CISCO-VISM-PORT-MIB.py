#
# PySNMP MIB module CISCO-VISM-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
vismPort, = mibBuilder.importSymbols("BASIS-MIB", "vismPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-VISM-PORT-MIB", vismPortCnfGrp=vismPortCnfGrp, ciscoVismPortMIBConformance=ciscoVismPortMIBConformance, vismPortRowStatus=vismPortRowStatus, vismPortCnfGrpEntry=vismPortCnfGrpEntry, vismPortLineNum=vismPortLineNum, PYSNMP_MODULE_ID=ciscoVismPortMIB, vismPortCnfGrpTable=vismPortCnfGrpTable, vismPortNum=vismPortNum, vismPortType=vismPortType, ciscoVismPortMIBCompliances=ciscoVismPortMIBCompliances, ciscoVismPortMIBGroups=ciscoVismPortMIBGroups, ciscoVismPortCompliance=ciscoVismPortCompliance, vismPortDs0ConfigBitMap=vismPortDs0ConfigBitMap, vismPortSpeed=vismPortSpeed, ciscoVismPortMIB=ciscoVismPortMIB, ciscoVismPortGroup=ciscoVismPortGroup, vismPortState=vismPortState)
