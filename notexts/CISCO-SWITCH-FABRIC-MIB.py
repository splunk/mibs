#
# PySNMP MIB module CISCO-SWITCH-FABRIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-FABRIC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "DateAndTime")
ciscoSwitchFabricMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 803))
ciscoSwitchFabricMIB.setRevisions(('2014-07-30 00:00', '2012-06-12 00:00',))
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setLastUpdated('201407300000Z')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setOrganization('Cisco Systems, Inc.')
ciscoSwitchFabricMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 0))
ciscoSwitchFabricMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1))
ciscoSwitchFabricMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2))
csfFabricStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1))
csfNotifsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2))
csfNotifsOnlyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3))
class CsfFabricLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("qEngineFacingLcXbarLink", 2), ("fabricXbarLink", 3), ("fabricFacingLcXbarLink", 4), ("lcXbarInterLink", 5), ("fabricXbarInterLink", 6), ("centralXbarLink", 7))

class CsfPercentOrMinusOne(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
csfFabricUtilTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1), )
if mibBuilder.loadTexts: csfFabricUtilTable.setStatus('current')
csfFabricUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilLinkType"), (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIndex"))
if mibBuilder.loadTexts: csfFabricUtilEntry.setStatus('current')
csfFabricUtilLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 1), CsfFabricLinkType())
if mibBuilder.loadTexts: csfFabricUtilLinkType.setStatus('current')
csfFabricUtilIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: csfFabricUtilIndex.setStatus('current')
csfFabricUtilDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilDescr.setStatus('current')
csfFabricUtilBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 4), Unsigned32()).setUnits('gigabits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilBandwidth.setStatus('current')
csfFabricUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 5), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilIn.setStatus('current')
csfFabricUtilInPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 6), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilInPeak.setStatus('current')
csfFabricUtilInPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilInPeakTime.setStatus('current')
csfFabricUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 8), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOut.setStatus('current')
csfFabricUtilOutPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 9), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOutPeak.setStatus('current')
csfFabricUtilOutPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOutPeakTime.setStatus('current')
csfFabricCrcErrorNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfFabricCrcErrorNotifEnable.setStatus('current')
csfFabricCrcErrorEntPhysicalIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: csfFabricCrcErrorEntPhysicalIndex.setStatus('current')
csfFabricCrcErrorDescr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: csfFabricCrcErrorDescr.setStatus('current')
csfFabricCrcErrorNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 803, 0, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
if mibBuilder.loadTexts: csfFabricCrcErrorNotif.setStatus('current')
csfSwitchFabricMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1))
csfSwitchFabricMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2))
csfSwitchFabricMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfSwitchFabricMIBCompliance = csfSwitchFabricMIBCompliance.setStatus('deprecated')
csfSwitchFabricMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 2)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsControlGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsInfoGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfSwitchFabricMIBCompliance1 = csfSwitchFabricMIBCompliance1.setStatus('current')
csfFabricUtilGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilDescr"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilBandwidth"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIn"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeak"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeakTime"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOut"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeak"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricUtilGroup = csfFabricUtilGroup.setStatus('current')
csfFabricCrcErrorNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 2)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsControlGroup = csfFabricCrcErrorNotifsControlGroup.setStatus('current')
csfFabricCrcErrorNotifsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 3)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsInfoGroup = csfFabricCrcErrorNotifsInfoGroup.setStatus('current')
csfFabricCrcErrorNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 4)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsGroup = csfFabricCrcErrorNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-FABRIC-MIB", csfFabricUtilGroup=csfFabricUtilGroup, csfFabricCrcErrorNotifsInfoGroup=csfFabricCrcErrorNotifsInfoGroup, csfFabricUtilInPeakTime=csfFabricUtilInPeakTime, csfFabricCrcErrorNotifsControlGroup=csfFabricCrcErrorNotifsControlGroup, csfNotifsControl=csfNotifsControl, ciscoSwitchFabricMIB=ciscoSwitchFabricMIB, ciscoSwitchFabricMIBNotifs=ciscoSwitchFabricMIBNotifs, csfSwitchFabricMIBCompliance1=csfSwitchFabricMIBCompliance1, csfSwitchFabricMIBGroups=csfSwitchFabricMIBGroups, PYSNMP_MODULE_ID=ciscoSwitchFabricMIB, ciscoSwitchFabricMIBConform=ciscoSwitchFabricMIBConform, csfFabricUtilEntry=csfFabricUtilEntry, CsfFabricLinkType=CsfFabricLinkType, csfFabricUtilOutPeakTime=csfFabricUtilOutPeakTime, csfFabricUtilBandwidth=csfFabricUtilBandwidth, csfFabricStatistics=csfFabricStatistics, csfFabricUtilTable=csfFabricUtilTable, csfSwitchFabricMIBCompliance=csfSwitchFabricMIBCompliance, csfFabricUtilIndex=csfFabricUtilIndex, csfFabricCrcErrorEntPhysicalIndex=csfFabricCrcErrorEntPhysicalIndex, csfFabricUtilIn=csfFabricUtilIn, ciscoSwitchFabricMIBObjects=ciscoSwitchFabricMIBObjects, csfFabricUtilDescr=csfFabricUtilDescr, csfFabricUtilInPeak=csfFabricUtilInPeak, csfFabricUtilOut=csfFabricUtilOut, csfFabricCrcErrorNotifEnable=csfFabricCrcErrorNotifEnable, csfNotifsOnlyInfo=csfNotifsOnlyInfo, CsfPercentOrMinusOne=CsfPercentOrMinusOne, csfFabricCrcErrorNotifsGroup=csfFabricCrcErrorNotifsGroup, csfFabricCrcErrorNotif=csfFabricCrcErrorNotif, csfSwitchFabricMIBCompliances=csfSwitchFabricMIBCompliances, csfFabricCrcErrorDescr=csfFabricCrcErrorDescr, csfFabricUtilOutPeak=csfFabricUtilOutPeak, csfFabricUtilLinkType=csfFabricUtilLinkType)
