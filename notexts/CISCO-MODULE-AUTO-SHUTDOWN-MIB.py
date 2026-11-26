#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODULE-AUTO-SHUTDOWN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalModelName, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalModelName", "entPhysicalName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "DateAndTime")
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
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-MIB", cmasModuleTable=cmasModuleTable, cmasModuleGroup=cmasModuleGroup, cmasModuleEnable=cmasModuleEnable, cmasNotifObjects=cmasNotifObjects, cmasModuleLastResetTime=cmasModuleLastResetTime, cmasModuleSysActionReason=cmasModuleSysActionReason, PYSNMP_MODULE_ID=ciscoModuleAutoShutdownMIB, cmasModuleLastResetReason=cmasModuleLastResetReason, cmasMIBCompliances=cmasMIBCompliances, cmasModuleSysActionNotifEnable=cmasModuleSysActionNotifEnable, cmasMIBConformance=cmasMIBConformance, cmasMIBGroups=cmasMIBGroups, cmasMIBCompliance=cmasMIBCompliance, cmasNotificationsGroup=cmasNotificationsGroup, cmasMIBCompliance2=cmasMIBCompliance2, cmasModuleSysAction=cmasModuleSysAction, cmasMIBEnableNotification=cmasMIBEnableNotification, cmasModuleEntry=cmasModuleEntry, cmasMIBObjects=cmasMIBObjects, cmasNotificationsGroup2=cmasNotificationsGroup2, cmasModuleSysActionGroup=cmasModuleSysActionGroup, cmasModuleNumResets=cmasModuleNumResets, cmasPeriod=cmasPeriod, ciscoModuleAutoShutdownMIB=ciscoModuleAutoShutdownMIB, cmasNotificationEnableGroup=cmasNotificationEnableGroup, cmasMIBNotifs=cmasMIBNotifs, cmasFrequency=cmasFrequency, cmasModuleSysActionObjects=cmasModuleSysActionObjects, cmasGlobal=cmasGlobal, cmasModule=cmasModule, CiscoModuleAutoShutSysAction=CiscoModuleAutoShutSysAction, cmasModuleAutoShutdown=cmasModuleAutoShutdown, cmasModuleSysActionNotif=cmasModuleSysActionNotif)
