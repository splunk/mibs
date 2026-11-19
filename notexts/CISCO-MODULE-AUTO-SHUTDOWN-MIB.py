#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODULE-AUTO-SHUTDOWN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalModelName, entPhysicalName, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalModelName", "entPhysicalName", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DateAndTime, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TruthValue", "TextualConvention")
ciscoModuleAutoShutdownMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 386))
ciscoModuleAutoShutdownMIB.setRevisions(('2008-03-12 00:00', '2003-12-29 00:00',))
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setLastUpdated('200803120000Z')
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setOrganization('Cisco Systems, Inc.')
cmasMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 0))
cmasMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1))
cmasMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2))
cmasGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1))
cmasNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2))
cmasModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3))
cmasModuleSysActionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4))
class CiscoModuleAutoShutSysAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("reset", 2), ("powerCycle", 3), ("powerDown", 4))

cmasFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasFrequency.setStatus('current')
cmasPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 2), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasPeriod.setStatus('current')
cmasMIBEnableNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasMIBEnableNotification.setStatus('current')
cmasModuleSysActionNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleSysActionNotifEnable.setStatus('current')
cmasModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1), )
if mibBuilder.loadTexts: cmasModuleTable.setStatus('current')
cmasModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cmasModuleEntry.setStatus('current')
cmasModuleEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleEnable.setStatus('current')
cmasModuleNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleNumResets.setStatus('current')
cmasModuleLastResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetReason.setStatus('current')
cmasModuleLastResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetTime.setStatus('current')
cmasModuleSysAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 1), CiscoModuleAutoShutSysAction()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysAction.setStatus('current')
cmasModuleSysActionReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysActionReason.setStatus('current')
cmasModuleAutoShutdown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"))
if mibBuilder.loadTexts: cmasModuleAutoShutdown.setStatus('current')
cmasModuleSysActionNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if mibBuilder.loadTexts: cmasModuleSysActionNotif.setStatus('current')
cmasMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1))
cmasMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2))
cmasMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance = cmasMIBCompliance.setStatus('deprecated')
cmasMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance2 = cmasMIBCompliance2.setStatus('current')
cmasModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasFrequency"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasPeriod"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleGroup = cmasModuleGroup.setStatus('current')
cmasNotificationEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasMIBEnableNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationEnableGroup = cmasNotificationEnableGroup.setStatus('current')
cmasNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 3)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleAutoShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup = cmasNotificationsGroup.setStatus('current')
cmasModuleSysActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 4)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotifEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleSysActionGroup = cmasModuleSysActionGroup.setStatus('current')
cmasNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 5)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup2 = cmasNotificationsGroup2.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-MIB", cmasModuleSysActionReason=cmasModuleSysActionReason, cmasModuleEnable=cmasModuleEnable, cmasModule=cmasModule, cmasMIBNotifs=cmasMIBNotifs, cmasFrequency=cmasFrequency, cmasMIBCompliance2=cmasMIBCompliance2, cmasNotifObjects=cmasNotifObjects, cmasMIBConformance=cmasMIBConformance, cmasNotificationsGroup2=cmasNotificationsGroup2, cmasModuleSysActionNotif=cmasModuleSysActionNotif, cmasMIBObjects=cmasMIBObjects, cmasModuleTable=cmasModuleTable, cmasModuleSysAction=cmasModuleSysAction, CiscoModuleAutoShutSysAction=CiscoModuleAutoShutSysAction, cmasModuleSysActionNotifEnable=cmasModuleSysActionNotifEnable, PYSNMP_MODULE_ID=ciscoModuleAutoShutdownMIB, cmasModuleAutoShutdown=cmasModuleAutoShutdown, cmasModuleSysActionObjects=cmasModuleSysActionObjects, cmasModuleGroup=cmasModuleGroup, cmasMIBGroups=cmasMIBGroups, cmasModuleLastResetReason=cmasModuleLastResetReason, cmasModuleLastResetTime=cmasModuleLastResetTime, cmasNotificationEnableGroup=cmasNotificationEnableGroup, cmasMIBCompliance=cmasMIBCompliance, cmasModuleNumResets=cmasModuleNumResets, cmasMIBCompliances=cmasMIBCompliances, cmasModuleEntry=cmasModuleEntry, cmasModuleSysActionGroup=cmasModuleSysActionGroup, ciscoModuleAutoShutdownMIB=ciscoModuleAutoShutdownMIB, cmasGlobal=cmasGlobal, cmasPeriod=cmasPeriod, cmasNotificationsGroup=cmasNotificationsGroup, cmasMIBEnableNotification=cmasMIBEnableNotification)
