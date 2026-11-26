#
# PySNMP MIB module CISCO-RF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
TimeStamp, TruthValue, TextualConvention, TimeInterval, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "TextualConvention", "TimeInterval", "DisplayString", "DateAndTime")
ciscoRFMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 176))
ciscoRFMIB.setRevisions(('2005-09-01 00:00', '2004-04-01 00:00', '2004-02-04 00:00', '2003-10-02 00:00', '2002-01-07 00:00', '2001-07-20 00:00', '2001-06-26 00:00', '2001-04-03 09:45',))
if mibBuilder.loadTexts: ciscoRFMIB.setLastUpdated('200509010000Z')
if mibBuilder.loadTexts: ciscoRFMIB.setOrganization('Cisco Systems, Inc.')
class RFState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("notKnown", 1), ("disabled", 2), ("initialization", 3), ("negotiation", 4), ("standbyCold", 5), ("standbyColdConfig", 6), ("standbyColdFileSys", 7), ("standbyColdBulk", 8), ("standbyHot", 9), ("activeFast", 10), ("activeDrain", 11), ("activePreconfig", 12), ("activePostconfig", 13), ("active", 14), ("activeExtraload", 15), ("activeHandback", 16))

class RFMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("nonRedundant", 1), ("staticLoadShareNonRedundant", 2), ("dynamicLoadShareNonRedundant", 3), ("staticLoadShareRedundant", 4), ("dynamicLoadShareRedundant", 5), ("coldStandbyRedundant", 6), ("warmStandbyRedundant", 7), ("hotStandbyRedundant", 8))

class RFAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noAction", 0), ("reloadPeer", 1), ("reloadShelf", 2), ("switchActivity", 3), ("forceSwitchActivity", 4))

class RFSwactReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unsupported", 1), ("none", 2), ("notKnown", 3), ("userInitiated", 4), ("userForced", 5), ("activeUnitFailed", 6), ("activeUnitRemoved", 7))

class RFUnitIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RFIssuState(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unset", 0), ("init", 1), ("loadVersion", 2), ("runVersion", 3), ("commitVersion", 4))

class RFIssuStateRev1(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 6, 7, 9))
    namedValues = NamedValues(("init", 0), ("systemReset", 1), ("loadVersion", 3), ("loadVersionSwitchover", 4), ("runVersion", 6), ("runVersionSwitchover", 7), ("commitVersion", 9))

class RFClientStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noStatus", 1), ("clientNotRedundant", 2), ("clientRedundancyInProgress", 3), ("clientRedundant", 4))

ciscoRFMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 1))
cRFStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1))
cRFCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2))
cRFHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3))
cRFClient = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4))
cRFStatusUnitId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 1), RFUnitIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusUnitId.setStatus('current')
cRFStatusUnitState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 2), RFState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusUnitState.setStatus('current')
cRFStatusPeerUnitId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 3), RFUnitIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusPeerUnitId.setStatus('current')
cRFStatusPeerUnitState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 4), RFState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusPeerUnitState.setStatus('current')
cRFStatusPrimaryMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusPrimaryMode.setStatus('current')
cRFStatusDuplexMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusDuplexMode.setStatus('current')
cRFStatusManualSwactInhibit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusManualSwactInhibit.setStatus('current')
cRFStatusLastSwactReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 8), RFSwactReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusLastSwactReasonCode.setStatus('current')
cRFStatusFailoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusFailoverTime.setStatus('current')
cRFStatusPeerStandByEntryTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusPeerStandByEntryTime.setStatus('current')
cRFStatusRFModeCapsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11), )
if mibBuilder.loadTexts: cRFStatusRFModeCapsTable.setStatus('current')
cRFStatusRFModeCapsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11, 1), ).setIndexNames((0, "CISCO-RF-MIB", "cRFStatusRFModeCapsMode"))
if mibBuilder.loadTexts: cRFStatusRFModeCapsEntry.setStatus('current')
cRFStatusRFModeCapsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11, 1, 1), RFMode())
if mibBuilder.loadTexts: cRFStatusRFModeCapsMode.setStatus('current')
cRFStatusRFModeCapsModeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusRFModeCapsModeDescr.setStatus('current')
cRFStatusIssuState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 12), RFIssuState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusIssuState.setStatus('deprecated')
cRFStatusIssuStateRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 13), RFIssuStateRev1()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusIssuStateRev1.setStatus('current')
cRFStatusIssuFromVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusIssuFromVersion.setStatus('current')
cRFStatusIssuToVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusIssuToVersion.setStatus('current')
cRFStatusRFClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1), )
if mibBuilder.loadTexts: cRFStatusRFClientTable.setStatus('current')
cRFStatusRFClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-RF-MIB", "cRFStatusRFClientID"))
if mibBuilder.loadTexts: cRFStatusRFClientEntry.setStatus('current')
cRFStatusRFClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cRFStatusRFClientID.setStatus('current')
cRFStatusRFClientDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusRFClientDescr.setStatus('current')
cRFStatusRFClientSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusRFClientSeq.setStatus('current')
cRFStatusRFClientRedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 4), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusRFClientRedTime.setStatus('current')
cRFStatusRFClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 5), RFClientStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFStatusRFClientStatus.setStatus('current')
cRFCfgSplitMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgSplitMode.setStatus('deprecated')
cRFCfgKeepaliveThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgKeepaliveThresh.setStatus('current')
cRFCfgKeepaliveThreshMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgKeepaliveThreshMin.setStatus('current')
cRFCfgKeepaliveThreshMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgKeepaliveThreshMax.setStatus('current')
cRFCfgKeepaliveTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 5), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgKeepaliveTimer.setStatus('current')
cRFCfgKeepaliveTimerMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgKeepaliveTimerMin.setStatus('current')
cRFCfgKeepaliveTimerMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 7), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgKeepaliveTimerMax.setStatus('current')
cRFCfgNotifTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 8), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgNotifTimer.setStatus('current')
cRFCfgNotifTimerMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 9), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgNotifTimerMin.setStatus('current')
cRFCfgNotifTimerMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 10), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgNotifTimerMax.setStatus('current')
cRFCfgAdminAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 11), RFAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgAdminAction.setStatus('current')
cRFCfgNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgNotifsEnabled.setStatus('current')
cRFCfgMaintenanceMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgMaintenanceMode.setStatus('current')
cRFCfgRedundancyMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 14), RFMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFCfgRedundancyMode.setStatus('current')
cRFCfgRedundancyModeDescr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgRedundancyModeDescr.setStatus('current')
cRFCfgRedundancyOperMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 16), RFMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFCfgRedundancyOperMode.setStatus('current')
cRFHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 50)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRFHistoryTableMaxLength.setStatus('current')
cRFHistorySwitchOverTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2), )
if mibBuilder.loadTexts: cRFHistorySwitchOverTable.setStatus('current')
cRFHistorySwitchOverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-RF-MIB", "cRFHistorySwitchOverIndex"))
if mibBuilder.loadTexts: cRFHistorySwitchOverEntry.setStatus('current')
cRFHistorySwitchOverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cRFHistorySwitchOverIndex.setStatus('current')
cRFHistoryPrevActiveUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 2), RFUnitIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFHistoryPrevActiveUnitId.setStatus('current')
cRFHistoryCurrActiveUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 3), RFUnitIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFHistoryCurrActiveUnitId.setStatus('current')
cRFHistorySwitchOverReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 4), RFSwactReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFHistorySwitchOverReason.setStatus('current')
cRFHistorySwactTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFHistorySwactTime.setStatus('current')
cRFHistoryColdStarts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFHistoryColdStarts.setStatus('current')
cRFHistoryStandByAvailTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRFHistoryStandByAvailTime.setStatus('current')
ciscoRFMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 2))
ciscoRFMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0))
ciscoRFSwactNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 1)).setObjects(("CISCO-RF-MIB", "cRFStatusUnitId"), ("SNMPv2-MIB", "sysUpTime"), ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"))
if mibBuilder.loadTexts: ciscoRFSwactNotif.setStatus('current')
ciscoRFProgressionNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 2)).setObjects(("CISCO-RF-MIB", "cRFStatusUnitId"), ("CISCO-RF-MIB", "cRFStatusUnitState"), ("CISCO-RF-MIB", "cRFStatusPeerUnitId"), ("CISCO-RF-MIB", "cRFStatusPeerUnitState"))
if mibBuilder.loadTexts: ciscoRFProgressionNotif.setStatus('current')
ciscoRFIssuStateNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 3)).setObjects(("CISCO-RF-MIB", "cRFStatusUnitId"), ("CISCO-RF-MIB", "cRFStatusUnitState"), ("CISCO-RF-MIB", "cRFStatusIssuState"))
if mibBuilder.loadTexts: ciscoRFIssuStateNotif.setStatus('deprecated')
ciscoRFIssuStateNotifRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 4)).setObjects(("CISCO-RF-MIB", "cRFStatusIssuStateRev1"), ("CISCO-RF-MIB", "cRFStatusIssuFromVersion"), ("CISCO-RF-MIB", "cRFStatusIssuToVersion"), ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"))
if mibBuilder.loadTexts: ciscoRFIssuStateNotifRev1.setStatus('current')
ciscoRFMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 3))
ciscoRFMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1))
ciscoRFMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2))
ciscoRFMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 1)).setObjects(("CISCO-RF-MIB", "ciscoRFStatusGroup"), ("CISCO-RF-MIB", "ciscoRFConfigGroup"), ("CISCO-RF-MIB", "ciscoRFNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFMIBCompliance = ciscoRFMIBCompliance.setStatus('deprecated')
ciscoRFMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 2)).setObjects(("CISCO-RF-MIB", "ciscoRFStatusGroup"), ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"), ("CISCO-RF-MIB", "ciscoRFNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFMIBComplianceRev1 = ciscoRFMIBComplianceRev1.setStatus('deprecated')
ciscoRFMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 3)).setObjects(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"), ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"), ("CISCO-RF-MIB", "ciscoRFNotifGroup"), ("CISCO-RF-MIB", "ciscoRFHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFMIBComplianceRev2 = ciscoRFMIBComplianceRev2.setStatus('deprecated')
ciscoRFMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 4)).setObjects(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"), ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"), ("CISCO-RF-MIB", "ciscoRFNotifGroup"), ("CISCO-RF-MIB", "ciscoRFHistoryGroup"), ("CISCO-RF-MIB", "ciscoRFConfigRFOperModeGroup"), ("CISCO-RF-MIB", "ciscoRFStatusRFModeCapsGroup"), ("CISCO-RF-MIB", "ciscoRFIssuStateNotifGroup"), ("CISCO-RF-MIB", "ciscoRFIssuStateObjGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFMIBComplianceRev3 = ciscoRFMIBComplianceRev3.setStatus('deprecated')
ciscoRFMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 5)).setObjects(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"), ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"), ("CISCO-RF-MIB", "ciscoRFNotifGroup"), ("CISCO-RF-MIB", "ciscoRFHistoryGroup"), ("CISCO-RF-MIB", "ciscoRFConfigRFOperModeGroup"), ("CISCO-RF-MIB", "ciscoRFStatusRFModeCapsGroup"), ("CISCO-RF-MIB", "ciscoRFIssuStateNotifGroupRev1"), ("CISCO-RF-MIB", "ciscoRFIssuStateObjGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFMIBComplianceRev4 = ciscoRFMIBComplianceRev4.setStatus('deprecated')
ciscoRFMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 6)).setObjects(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"), ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"), ("CISCO-RF-MIB", "ciscoRFNotifGroup"), ("CISCO-RF-MIB", "ciscoRFHistoryGroup"), ("CISCO-RF-MIB", "ciscoRFConfigRFOperModeGroup"), ("CISCO-RF-MIB", "ciscoRFStatusRFModeCapsGroup"), ("CISCO-RF-MIB", "ciscoRFIssuStateNotifGroupRev1"), ("CISCO-RF-MIB", "ciscoRFIssuStateObjGroupRev1"), ("CISCO-RF-MIB", "ciscoRFStatusClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFMIBComplianceRev5 = ciscoRFMIBComplianceRev5.setStatus('current')
ciscoRFStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 1)).setObjects(("CISCO-RF-MIB", "cRFStatusUnitId"), ("CISCO-RF-MIB", "cRFStatusUnitState"), ("CISCO-RF-MIB", "cRFStatusPeerUnitId"), ("CISCO-RF-MIB", "cRFStatusPeerUnitState"), ("CISCO-RF-MIB", "cRFStatusPrimaryMode"), ("CISCO-RF-MIB", "cRFStatusDuplexMode"), ("CISCO-RF-MIB", "cRFStatusManualSwactInhibit"), ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFStatusGroup = ciscoRFStatusGroup.setStatus('deprecated')
ciscoRFConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 2)).setObjects(("CISCO-RF-MIB", "cRFCfgSplitMode"), ("CISCO-RF-MIB", "cRFCfgKeepaliveThresh"), ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMin"), ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMax"), ("CISCO-RF-MIB", "cRFCfgKeepaliveTimer"), ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMin"), ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMax"), ("CISCO-RF-MIB", "cRFCfgNotifTimer"), ("CISCO-RF-MIB", "cRFCfgNotifTimerMin"), ("CISCO-RF-MIB", "cRFCfgNotifTimerMax"), ("CISCO-RF-MIB", "cRFCfgAdminAction"), ("CISCO-RF-MIB", "cRFCfgNotifsEnabled"), ("CISCO-RF-MIB", "cRFCfgRedundancyMode"), ("CISCO-RF-MIB", "cRFCfgRedundancyModeDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFConfigGroup = ciscoRFConfigGroup.setStatus('deprecated')
ciscoRFNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 3)).setObjects(("CISCO-RF-MIB", "ciscoRFSwactNotif"), ("CISCO-RF-MIB", "ciscoRFProgressionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFNotifGroup = ciscoRFNotifGroup.setStatus('current')
ciscoRFConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 4)).setObjects(("CISCO-RF-MIB", "cRFCfgKeepaliveThresh"), ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMin"), ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMax"), ("CISCO-RF-MIB", "cRFCfgKeepaliveTimer"), ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMin"), ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMax"), ("CISCO-RF-MIB", "cRFCfgNotifTimer"), ("CISCO-RF-MIB", "cRFCfgNotifTimerMin"), ("CISCO-RF-MIB", "cRFCfgNotifTimerMax"), ("CISCO-RF-MIB", "cRFCfgAdminAction"), ("CISCO-RF-MIB", "cRFCfgNotifsEnabled"), ("CISCO-RF-MIB", "cRFCfgMaintenanceMode"), ("CISCO-RF-MIB", "cRFCfgRedundancyMode"), ("CISCO-RF-MIB", "cRFCfgRedundancyModeDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFConfigGroupRev1 = ciscoRFConfigGroupRev1.setStatus('current')
ciscoRFStatusGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 5)).setObjects(("CISCO-RF-MIB", "cRFStatusUnitId"), ("CISCO-RF-MIB", "cRFStatusUnitState"), ("CISCO-RF-MIB", "cRFStatusPeerUnitId"), ("CISCO-RF-MIB", "cRFStatusPeerUnitState"), ("CISCO-RF-MIB", "cRFStatusPrimaryMode"), ("CISCO-RF-MIB", "cRFStatusDuplexMode"), ("CISCO-RF-MIB", "cRFStatusManualSwactInhibit"), ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"), ("CISCO-RF-MIB", "cRFStatusFailoverTime"), ("CISCO-RF-MIB", "cRFStatusPeerStandByEntryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFStatusGroupRev1 = ciscoRFStatusGroupRev1.setStatus('current')
ciscoRFHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 6)).setObjects(("CISCO-RF-MIB", "cRFHistoryPrevActiveUnitId"), ("CISCO-RF-MIB", "cRFHistoryCurrActiveUnitId"), ("CISCO-RF-MIB", "cRFHistorySwitchOverReason"), ("CISCO-RF-MIB", "cRFHistorySwactTime"), ("CISCO-RF-MIB", "cRFHistoryColdStarts"), ("CISCO-RF-MIB", "cRFHistoryStandByAvailTime"), ("CISCO-RF-MIB", "cRFHistoryTableMaxLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFHistoryGroup = ciscoRFHistoryGroup.setStatus('current')
ciscoRFConfigRFOperModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 7)).setObjects(("CISCO-RF-MIB", "cRFCfgRedundancyOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFConfigRFOperModeGroup = ciscoRFConfigRFOperModeGroup.setStatus('current')
ciscoRFStatusRFModeCapsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 8)).setObjects(("CISCO-RF-MIB", "cRFStatusRFModeCapsModeDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFStatusRFModeCapsGroup = ciscoRFStatusRFModeCapsGroup.setStatus('current')
ciscoRFIssuStateNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 9)).setObjects(("CISCO-RF-MIB", "ciscoRFIssuStateNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFIssuStateNotifGroup = ciscoRFIssuStateNotifGroup.setStatus('deprecated')
ciscoRFIssuStateNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 10)).setObjects(("CISCO-RF-MIB", "ciscoRFIssuStateNotifRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFIssuStateNotifGroupRev1 = ciscoRFIssuStateNotifGroupRev1.setStatus('current')
ciscoRFIssuStateObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 11)).setObjects(("CISCO-RF-MIB", "cRFStatusIssuState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFIssuStateObjGroup = ciscoRFIssuStateObjGroup.setStatus('deprecated')
ciscoRFIssuStateObjGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 12)).setObjects(("CISCO-RF-MIB", "cRFStatusIssuStateRev1"), ("CISCO-RF-MIB", "cRFStatusIssuFromVersion"), ("CISCO-RF-MIB", "cRFStatusIssuToVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFIssuStateObjGroupRev1 = ciscoRFIssuStateObjGroupRev1.setStatus('current')
ciscoRFStatusClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 13)).setObjects(("CISCO-RF-MIB", "cRFStatusRFClientDescr"), ("CISCO-RF-MIB", "cRFStatusRFClientSeq"), ("CISCO-RF-MIB", "cRFStatusRFClientRedTime"), ("CISCO-RF-MIB", "cRFStatusRFClientStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFStatusClientGroup = ciscoRFStatusClientGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-RF-MIB", cRFStatusRFModeCapsMode=cRFStatusRFModeCapsMode, cRFStatusRFClientRedTime=cRFStatusRFClientRedTime, ciscoRFIssuStateObjGroup=ciscoRFIssuStateObjGroup, cRFStatusRFClientTable=cRFStatusRFClientTable, cRFHistorySwitchOverIndex=cRFHistorySwitchOverIndex, cRFCfgMaintenanceMode=cRFCfgMaintenanceMode, ciscoRFIssuStateNotifGroup=ciscoRFIssuStateNotifGroup, ciscoRFIssuStateNotifRev1=ciscoRFIssuStateNotifRev1, cRFStatusRFModeCapsEntry=cRFStatusRFModeCapsEntry, ciscoRFStatusGroupRev1=ciscoRFStatusGroupRev1, ciscoRFMIBComplianceRev2=ciscoRFMIBComplianceRev2, cRFCfgKeepaliveTimerMin=cRFCfgKeepaliveTimerMin, ciscoRFConfigRFOperModeGroup=ciscoRFConfigRFOperModeGroup, RFState=RFState, cRFCfg=cRFCfg, ciscoRFMIBCompliances=ciscoRFMIBCompliances, cRFStatusRFClientEntry=cRFStatusRFClientEntry, RFMode=RFMode, cRFCfgNotifTimer=cRFCfgNotifTimer, ciscoRFMIBNotificationsPrefix=ciscoRFMIBNotificationsPrefix, cRFStatus=cRFStatus, ciscoRFConfigGroupRev1=ciscoRFConfigGroupRev1, cRFStatusLastSwactReasonCode=cRFStatusLastSwactReasonCode, cRFHistoryStandByAvailTime=cRFHistoryStandByAvailTime, ciscoRFMIBCompliance=ciscoRFMIBCompliance, cRFHistorySwitchOverReason=cRFHistorySwitchOverReason, cRFStatusIssuState=cRFStatusIssuState, cRFCfgKeepaliveThreshMax=cRFCfgKeepaliveThreshMax, ciscoRFMIBComplianceRev4=ciscoRFMIBComplianceRev4, ciscoRFMIBComplianceRev5=ciscoRFMIBComplianceRev5, cRFHistoryPrevActiveUnitId=cRFHistoryPrevActiveUnitId, cRFStatusFailoverTime=cRFStatusFailoverTime, ciscoRFConfigGroup=ciscoRFConfigGroup, ciscoRFStatusClientGroup=ciscoRFStatusClientGroup, cRFHistoryCurrActiveUnitId=cRFHistoryCurrActiveUnitId, cRFHistoryColdStarts=cRFHistoryColdStarts, cRFCfgNotifsEnabled=cRFCfgNotifsEnabled, cRFCfgKeepaliveTimerMax=cRFCfgKeepaliveTimerMax, cRFStatusRFModeCapsModeDescr=cRFStatusRFModeCapsModeDescr, ciscoRFIssuStateNotifGroupRev1=ciscoRFIssuStateNotifGroupRev1, ciscoRFIssuStateNotif=ciscoRFIssuStateNotif, ciscoRFSwactNotif=ciscoRFSwactNotif, RFClientStatus=RFClientStatus, cRFStatusRFClientDescr=cRFStatusRFClientDescr, cRFHistorySwitchOverEntry=cRFHistorySwitchOverEntry, RFUnitIdentifier=RFUnitIdentifier, cRFCfgKeepaliveTimer=cRFCfgKeepaliveTimer, cRFStatusManualSwactInhibit=cRFStatusManualSwactInhibit, cRFCfgSplitMode=cRFCfgSplitMode, ciscoRFStatusRFModeCapsGroup=ciscoRFStatusRFModeCapsGroup, cRFStatusDuplexMode=cRFStatusDuplexMode, ciscoRFMIBConformance=ciscoRFMIBConformance, cRFCfgNotifTimerMax=cRFCfgNotifTimerMax, cRFStatusPeerStandByEntryTime=cRFStatusPeerStandByEntryTime, cRFStatusRFClientID=cRFStatusRFClientID, ciscoRFMIB=ciscoRFMIB, ciscoRFHistoryGroup=ciscoRFHistoryGroup, ciscoRFStatusGroup=ciscoRFStatusGroup, cRFHistorySwactTime=cRFHistorySwactTime, ciscoRFMIBObjects=ciscoRFMIBObjects, cRFClient=cRFClient, cRFStatusPeerUnitId=cRFStatusPeerUnitId, cRFCfgRedundancyOperMode=cRFCfgRedundancyOperMode, ciscoRFMIBGroups=ciscoRFMIBGroups, ciscoRFMIBComplianceRev1=ciscoRFMIBComplianceRev1, cRFStatusUnitState=cRFStatusUnitState, cRFStatusUnitId=cRFStatusUnitId, ciscoRFMIBComplianceRev3=ciscoRFMIBComplianceRev3, cRFCfgNotifTimerMin=cRFCfgNotifTimerMin, ciscoRFNotifGroup=ciscoRFNotifGroup, cRFStatusRFModeCapsTable=cRFStatusRFModeCapsTable, cRFStatusPeerUnitState=cRFStatusPeerUnitState, RFIssuStateRev1=RFIssuStateRev1, cRFCfgAdminAction=cRFCfgAdminAction, PYSNMP_MODULE_ID=ciscoRFMIB, cRFStatusPrimaryMode=cRFStatusPrimaryMode, cRFCfgKeepaliveThreshMin=cRFCfgKeepaliveThreshMin, ciscoRFMIBNotifications=ciscoRFMIBNotifications, RFAction=RFAction, ciscoRFProgressionNotif=ciscoRFProgressionNotif, RFSwactReasonType=RFSwactReasonType, cRFStatusRFClientStatus=cRFStatusRFClientStatus, cRFHistoryTableMaxLength=cRFHistoryTableMaxLength, cRFCfgRedundancyMode=cRFCfgRedundancyMode, ciscoRFIssuStateObjGroupRev1=ciscoRFIssuStateObjGroupRev1, cRFStatusRFClientSeq=cRFStatusRFClientSeq, cRFStatusIssuFromVersion=cRFStatusIssuFromVersion, cRFHistory=cRFHistory, cRFStatusIssuToVersion=cRFStatusIssuToVersion, cRFCfgKeepaliveThresh=cRFCfgKeepaliveThresh, cRFStatusIssuStateRev1=cRFStatusIssuStateRev1, cRFCfgRedundancyModeDescr=cRFCfgRedundancyModeDescr, cRFHistorySwitchOverTable=cRFHistorySwitchOverTable, RFIssuState=RFIssuState)
