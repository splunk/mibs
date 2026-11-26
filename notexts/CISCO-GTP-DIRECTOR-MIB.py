#
# PySNMP MIB module CISCO-GTP-DIRECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GTP-DIRECTOR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoGtpDirectorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 245))
ciscoGtpDirectorMIB.setRevisions(('2001-09-13 14:00',))
if mibBuilder.loadTexts: ciscoGtpDirectorMIB.setLastUpdated('200109131400Z')
if mibBuilder.loadTexts: ciscoGtpDirectorMIB.setOrganization('Cisco Systems, Inc.')
ciscoGtpDirectorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 1))
cgdConfigurations = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 1))
cgdStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 2))
cgdStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3))
cgdNotifMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 4))
cgdCreatePdpRequestInfoSaveTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgdCreatePdpRequestInfoSaveTimer.setStatus('current')
cgdPendingPdps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgdPendingPdps.setStatus('current')
cgdCreatePdpRequestFwded = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgdCreatePdpRequestFwded.setStatus('current')
cgdTotalCreatePdpRequestFwded = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgdTotalCreatePdpRequestFwded.setStatus('current')
cgdCreateRequestRejected = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgdCreateRequestRejected.setStatus('current')
cgdTotalUnsupportedMessages = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgdTotalUnsupportedMessages.setStatus('current')
cgdPdpRequestDropped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgdPdpRequestDropped.setStatus('current')
cgdNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgdNotifEnable.setStatus('current')
cgdNotifType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 245, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gdmServiceUp", 1), ("gdmServiceDown", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgdNotifType.setStatus('current')
ciscoGtpDirectorNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 2))
ciscoGtpDirectorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 2, 0))
ciscoGtpDirectorNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 245, 2, 0, 1)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "cgdNotifType"))
if mibBuilder.loadTexts: ciscoGtpDirectorNotification.setStatus('current')
ciscoGtpDirectorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 3))
ciscoGtpDirectorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 1))
ciscoGtpDirectorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2))
ciscoGtpDirectorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 1, 1)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorConfigurationsGroup"), ("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorStatusGroup"), ("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorStatisticsGroup"), ("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorNotifMgmtGroup"), ("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGtpDirectorMIBCompliance = ciscoGtpDirectorMIBCompliance.setStatus('current')
ciscoGtpDirectorConfigurationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 1)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "cgdCreatePdpRequestInfoSaveTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGtpDirectorConfigurationsGroup = ciscoGtpDirectorConfigurationsGroup.setStatus('current')
ciscoGtpDirectorStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 2)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "cgdPendingPdps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGtpDirectorStatusGroup = ciscoGtpDirectorStatusGroup.setStatus('current')
ciscoGtpDirectorStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 3)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "cgdCreatePdpRequestFwded"), ("CISCO-GTP-DIRECTOR-MIB", "cgdTotalCreatePdpRequestFwded"), ("CISCO-GTP-DIRECTOR-MIB", "cgdCreateRequestRejected"), ("CISCO-GTP-DIRECTOR-MIB", "cgdTotalUnsupportedMessages"), ("CISCO-GTP-DIRECTOR-MIB", "cgdPdpRequestDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGtpDirectorStatisticsGroup = ciscoGtpDirectorStatisticsGroup.setStatus('current')
ciscoGtpDirectorNotifMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 4)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "cgdNotifEnable"), ("CISCO-GTP-DIRECTOR-MIB", "cgdNotifType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGtpDirectorNotifMgmtGroup = ciscoGtpDirectorNotifMgmtGroup.setStatus('current')
ciscoGtpDirectorNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 245, 3, 2, 5)).setObjects(("CISCO-GTP-DIRECTOR-MIB", "ciscoGtpDirectorNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGtpDirectorNotifGroup = ciscoGtpDirectorNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GTP-DIRECTOR-MIB", cgdStatistics=cgdStatistics, ciscoGtpDirectorNotifPrefix=ciscoGtpDirectorNotifPrefix, ciscoGtpDirectorConfigurationsGroup=ciscoGtpDirectorConfigurationsGroup, ciscoGtpDirectorStatisticsGroup=ciscoGtpDirectorStatisticsGroup, cgdNotifType=cgdNotifType, cgdTotalCreatePdpRequestFwded=cgdTotalCreatePdpRequestFwded, ciscoGtpDirectorMIBObjects=ciscoGtpDirectorMIBObjects, ciscoGtpDirectorMIBConformance=ciscoGtpDirectorMIBConformance, cgdCreatePdpRequestFwded=cgdCreatePdpRequestFwded, cgdPdpRequestDropped=cgdPdpRequestDropped, ciscoGtpDirectorMIBCompliances=ciscoGtpDirectorMIBCompliances, cgdCreatePdpRequestInfoSaveTimer=cgdCreatePdpRequestInfoSaveTimer, ciscoGtpDirectorNotification=ciscoGtpDirectorNotification, PYSNMP_MODULE_ID=ciscoGtpDirectorMIB, cgdNotifMgmt=cgdNotifMgmt, ciscoGtpDirectorMIBCompliance=ciscoGtpDirectorMIBCompliance, ciscoGtpDirectorNotifGroup=ciscoGtpDirectorNotifGroup, ciscoGtpDirectorNotifMgmtGroup=ciscoGtpDirectorNotifMgmtGroup, cgdCreateRequestRejected=cgdCreateRequestRejected, cgdPendingPdps=cgdPendingPdps, cgdTotalUnsupportedMessages=cgdTotalUnsupportedMessages, ciscoGtpDirectorNotifications=ciscoGtpDirectorNotifications, ciscoGtpDirectorMIBGroups=ciscoGtpDirectorMIBGroups, cgdStatus=cgdStatus, ciscoGtpDirectorMIB=ciscoGtpDirectorMIB, cgdNotifEnable=cgdNotifEnable, cgdConfigurations=cgdConfigurations, ciscoGtpDirectorStatusGroup=ciscoGtpDirectorStatusGroup)
