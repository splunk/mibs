#
# PySNMP MIB module CISCO-MGX82XX-RPM-SUBIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX82XX-RPM-SUBIF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
rpmPort, = mibBuilder.importSymbols("BASIS-MIB", "rpmPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, IpAddress, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, NotificationType, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "NotificationType", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-MGX82XX-RPM-SUBIF-MIB", rpmPortState=rpmPortState, rpmPortEntry=rpmPortEntry, rpmPortInterface=rpmPortInterface, rpmPortRowStatus=rpmPortRowStatus, rpmPortSubInterface=rpmPortSubInterface, rpmPortSubNetMask=rpmPortSubNetMask, rpmPortTable=rpmPortTable, ciscoMgx82xxRpmSubIfMIB=ciscoMgx82xxRpmSubIfMIB, rpmPortIpAddress=rpmPortIpAddress, PYSNMP_MODULE_ID=ciscoMgx82xxRpmSubIfMIB, cmrSubIfMIBConformance=cmrSubIfMIBConformance, cmrSubIfMIBGroups=cmrSubIfMIBGroups, cmrSubIfMIBCompliance=cmrSubIfMIBCompliance, cmrSubIfMIBGroup=cmrSubIfMIBGroup, cmrSubIfMIBCompliances=cmrSubIfMIBCompliances, rpmPortSlotNum=rpmPortSlotNum)
