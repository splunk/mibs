#
# PySNMP MIB module CISCO-MGX82XX-RPM-SUBIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX82XX-RPM-SUBIF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
rpmPort, = mibBuilder.importSymbols("BASIS-MIB", "rpmPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxRpmSubIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 60))
ciscoMgx82xxRpmSubIfMIB.setRevisions(('2002-09-08 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxRpmSubIfMIB.setLastUpdated('200209080000Z')
if mibBuilder.loadTexts: ciscoMgx82xxRpmSubIfMIB.setOrganization('Cisco Systems, Inc.')
rpmPortTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1), )
if mibBuilder.loadTexts: rpmPortTable.setStatus('current')
rpmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"), (0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"))
if mibBuilder.loadTexts: rpmPortEntry.setStatus('current')
rpmPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSlotNum.setStatus('current')
rpmPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortInterface.setStatus('current')
rpmPortSubInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSubInterface.setStatus('current')
rpmPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortRowStatus.setStatus('current')
rpmPortIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortIpAddress.setStatus('current')
rpmPortSubNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSubNetMask.setStatus('current')
rpmPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConfigured", 1), ("active", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortState.setStatus('current')
cmrSubIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2))
cmrSubIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1))
cmrSubIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2))
cmrSubIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1, 1)).setObjects(("CISCO-MGX82XX-RPM-SUBIF-MIB", "cmrSubIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmrSubIfMIBCompliance = cmrSubIfMIBCompliance.setStatus('current')
cmrSubIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2, 1)).setObjects(("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortInterface"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortRowStatus"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortIpAddress"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubNetMask"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmrSubIfMIBGroup = cmrSubIfMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-RPM-SUBIF-MIB", PYSNMP_MODULE_ID=ciscoMgx82xxRpmSubIfMIB, rpmPortSlotNum=rpmPortSlotNum, rpmPortIpAddress=rpmPortIpAddress, rpmPortInterface=rpmPortInterface, cmrSubIfMIBGroup=cmrSubIfMIBGroup, rpmPortSubInterface=rpmPortSubInterface, ciscoMgx82xxRpmSubIfMIB=ciscoMgx82xxRpmSubIfMIB, rpmPortEntry=rpmPortEntry, rpmPortRowStatus=rpmPortRowStatus, cmrSubIfMIBConformance=cmrSubIfMIBConformance, rpmPortTable=rpmPortTable, rpmPortSubNetMask=rpmPortSubNetMask, cmrSubIfMIBGroups=cmrSubIfMIBGroups, cmrSubIfMIBCompliance=cmrSubIfMIBCompliance, cmrSubIfMIBCompliances=cmrSubIfMIBCompliances, rpmPortState=rpmPortState)
