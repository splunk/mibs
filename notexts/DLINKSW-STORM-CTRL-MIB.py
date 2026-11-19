#
# PySNMP MIB module DLINKSW-STORM-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-STORM-CTRL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, ModuleIdentity, Unsigned32, Gauge32, iso, Bits, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Unsigned32", "Gauge32", "iso", "Bits", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwStormCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 25))
dlinkSwStormCtrlMIB.setRevisions(('2013-06-13 00:00',))
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setLastUpdated('201306130000Z')
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setOrganization('D-Link Corp.')
class DStormCtlTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("broadcast", 1), ("multicast", 2), ("unicast", 3))

class DStormCtlThrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pps", 1), ("kbps", 2), ("percentage", 3))

class DStormCtlThrTypeValue(TextualConvention, Integer32):
    status = 'current'

dStormCtrlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 0))
dStormCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1))
dStormCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2))
dStormCtrlGentrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1))
dStormCtrlNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("stormOccurred", 2), ("stormCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlNotifyEnable.setStatus('current')
dStormCtrlPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 600)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlPollingInterval.setStatus('current')
dStormCtrlPollingRetries = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 360), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlPollingRetries.setStatus('current')
dStormCtrlThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2), )
if mibBuilder.loadTexts: dStormCtrlThresholdTable.setStatus('current')
dStormCtrlThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"))
if mibBuilder.loadTexts: dStormCtrlThresholdEntry.setStatus('current')
dStormCtrlTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 1), DStormCtlTrafficType())
if mibBuilder.loadTexts: dStormCtrlTrafficType.setStatus('current')
dStormCtrlThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 2), DStormCtlThrType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlThresholdType.setStatus('current')
dStormCtrlRiseThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 3), DStormCtlThrTypeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlRiseThresholdValue.setStatus('current')
dStormCtrlLowThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 4), DStormCtlThrTypeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlLowThresholdValue.setStatus('current')
dStormCtrlIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3), )
if mibBuilder.loadTexts: dStormCtrlIfTable.setStatus('current')
dStormCtrlIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dStormCtrlIfEntry.setStatus('current')
dStormCtrlIfActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("shutdown", 2), ("drop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlIfActionType.setStatus('current')
dStormCtrlTrafficInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4), )
if mibBuilder.loadTexts: dStormCtrlTrafficInfoTable.setStatus('current')
dStormCtrlTrafficInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"))
if mibBuilder.loadTexts: dStormCtrlTrafficInfoEntry.setStatus('current')
dStormCtrlCurTrafficUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 1), DStormCtlThrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlCurTrafficUnitType.setStatus('current')
dStormCtrlCurTrafficValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 2), DStormCtlThrTypeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlCurTrafficValue.setStatus('current')
dStormCtrlTrafficInfoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("forwarding", 1), ("dropped", 2), ("errorDisabled", 3), ("linkDown", 4), ("inactive", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlTrafficInfoStatus.setStatus('current')
dStormCtrlNotifyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5))
dStormCtrlNotifyTrafficType = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5, 1), DStormCtlTrafficType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dStormCtrlNotifyTrafficType.setStatus('current')
dStormCtrlOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if mibBuilder.loadTexts: dStormCtrlOccurred.setStatus('current')
dStormCtrlStormCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if mibBuilder.loadTexts: dStormCtrlStormCleared.setStatus('current')
dStormCtrlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1))
dStormCtrlCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1, 1)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlBaiscGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlCompliance = dStormCtrlCompliance.setStatus('current')
dStormCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2))
dStormCtrlBaiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 1)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyEnable"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingInterval"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingRetries"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlThresholdType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlRiseThresholdValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlLowThresholdValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlIfActionType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficUnitType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficInfoStatus"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlBaiscGroup = dStormCtrlBaiscGroup.setStatus('current')
dStormCtrlNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 2)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlOccurred"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlStormCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlNotifyGroup = dStormCtrlNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-STORM-CTRL-MIB", dStormCtrlCurTrafficUnitType=dStormCtrlCurTrafficUnitType, dStormCtrlCurTrafficValue=dStormCtrlCurTrafficValue, dStormCtrlNotifyInfo=dStormCtrlNotifyInfo, dStormCtrlGentrl=dStormCtrlGentrl, dStormCtrlPollingRetries=dStormCtrlPollingRetries, dStormCtrlThresholdEntry=dStormCtrlThresholdEntry, dStormCtrlTrafficType=dStormCtrlTrafficType, dStormCtrlCompliances=dStormCtrlCompliances, DStormCtlThrType=DStormCtlThrType, dStormCtrlIfTable=dStormCtrlIfTable, dStormCtrlNotifyEnable=dStormCtrlNotifyEnable, dStormCtrlIfEntry=dStormCtrlIfEntry, PYSNMP_MODULE_ID=dlinkSwStormCtrlMIB, dStormCtrlNotifyGroup=dStormCtrlNotifyGroup, dStormCtrlTrafficInfoStatus=dStormCtrlTrafficInfoStatus, dStormCtrlOccurred=dStormCtrlOccurred, dStormCtrlTrafficInfoEntry=dStormCtrlTrafficInfoEntry, dStormCtrlTrafficInfoTable=dStormCtrlTrafficInfoTable, dStormCtrlMIBConformance=dStormCtrlMIBConformance, dStormCtrlThresholdType=dStormCtrlThresholdType, dStormCtrlMIBObjects=dStormCtrlMIBObjects, dStormCtrlRiseThresholdValue=dStormCtrlRiseThresholdValue, dStormCtrlStormCleared=dStormCtrlStormCleared, dStormCtrlPollingInterval=dStormCtrlPollingInterval, DStormCtlThrTypeValue=DStormCtlThrTypeValue, dStormCtrlThresholdTable=dStormCtrlThresholdTable, dStormCtrlMIBNotifications=dStormCtrlMIBNotifications, DStormCtlTrafficType=DStormCtlTrafficType, dStormCtrlNotifyTrafficType=dStormCtrlNotifyTrafficType, dStormCtrlIfActionType=dStormCtrlIfActionType, dStormCtrlCompliance=dStormCtrlCompliance, dStormCtrlGroup=dStormCtrlGroup, dStormCtrlBaiscGroup=dStormCtrlBaiscGroup, dStormCtrlLowThresholdValue=dStormCtrlLowThresholdValue, dlinkSwStormCtrlMIB=dlinkSwStormCtrlMIB)
