#
# PySNMP MIB module CISCO-WIRELESS-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WIRELESS-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter64, MibIdentifier, NotificationType, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter64", "MibIdentifier", "NotificationType", "iso", "Unsigned32", "Counter32")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
ciscoWirelessNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 712))
ciscoWirelessNotificationMIB.setRevisions(('2011-06-06 00:00', '2010-09-15 00:00', '2009-10-28 00:00',))
if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setLastUpdated('201106060000Z')
if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setOrganization('Cisco Systems, Inc.')
class CWirelessNotificationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("alert", 2), ("event", 3))

class CWirelessNotificationCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("unknown", 1), ("accessPoints", 2), ("adhocRogue", 3), ("clients", 4), ("controllers", 5), ("coverageHole", 6), ("interference", 7), ("contextAwareNotifications", 8), ("meshLinks", 9), ("mobilityService", 10), ("performance", 11), ("rogueAP", 12), ("rrm", 13), ("security", 14), ("wcs", 15), ("switch", 16), ("ncs", 17))

ciscoWirelessNotificationMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 0))
ciscoWirelessNotificationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 1))
ciscoWirelessNotificationMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 2))
cWNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1))
cwNotificationHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwNotificationHistoryTableMaxLength.setStatus('current')
cwNotificationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2), )
if mibBuilder.loadTexts: cwNotificationHistoryTable.setStatus('current')
cwNotificationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationIndex"))
if mibBuilder.loadTexts: cwNotificationHistoryEntry.setStatus('current')
cWNotificationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cWNotificationIndex.setStatus('current')
cWNotificationTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationTimestamp.setStatus('current')
cWNotificationUpdatedTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationUpdatedTimestamp.setStatus('current')
cWNotificationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationKey.setStatus('current')
cWNotificationCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 5), CWirelessNotificationCategory()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationCategory.setStatus('current')
cWNotificationSubCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSubCategory.setStatus('current')
cWNotificationManagedObjectAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationManagedObjectAddressType.setStatus('current')
cWNotificationManagedObjectAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationManagedObjectAddress.setStatus('current')
cWNotificationSourceDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSourceDisplayName.setStatus('current')
cWNotificationDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationDescription.setStatus('current')
cWNotificationSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 11), CiscoAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSeverity.setStatus('current')
cWNotificationSpecialAttributes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSpecialAttributes.setStatus('current')
cWNotificationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 13), CWirelessNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationType.setStatus('current')
cWNotificationVirtualDomains = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationVirtualDomains.setStatus('current')
cwNotificationMOStatusEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwNotificationMOStatusEnable.setStatus('current')
ciscoWirelessMOStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 712, 0, 1)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationUpdatedTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationKey"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSubCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddressType"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddress"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSourceDisplayName"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationDescription"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSeverity"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSpecialAttributes"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationVirtualDomains"))
if mibBuilder.loadTexts: ciscoWirelessMOStatusNotification.setStatus('current')
ciscoWirelessNotificationMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 1))
ciscoWirelessNotificationMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2))
ciscoWirelessNotificationMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 1, 1)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationObjectsGroup"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationsGroup"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationConfigGroup"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationEnableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationMIBCompliance = ciscoWirelessNotificationMIBCompliance.setStatus('current')
ciscoWirelessNotificationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 1)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cwNotificationHistoryTableMaxLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationConfigGroup = ciscoWirelessNotificationConfigGroup.setStatus('current')
ciscoWirelessNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 2)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessMOStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationsGroup = ciscoWirelessNotificationsGroup.setStatus('current')
ciscoWirelessNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 3)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationUpdatedTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationKey"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSubCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddressType"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddress"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSourceDisplayName"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationDescription"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSeverity"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSpecialAttributes"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationType"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationVirtualDomains"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationObjectsGroup = ciscoWirelessNotificationObjectsGroup.setStatus('current')
ciscoWirelessNotificationEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 4)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cwNotificationMOStatusEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationEnableGroup = ciscoWirelessNotificationEnableGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WIRELESS-NOTIFICATION-MIB", cWNotificationCategory=cWNotificationCategory, cWNotificationSourceDisplayName=cWNotificationSourceDisplayName, cWNotificationSpecialAttributes=cWNotificationSpecialAttributes, cWNotificationData=cWNotificationData, cWNotificationVirtualDomains=cWNotificationVirtualDomains, CWirelessNotificationType=CWirelessNotificationType, cWNotificationType=cWNotificationType, ciscoWirelessNotificationMIBGroups=ciscoWirelessNotificationMIBGroups, ciscoWirelessNotificationMIBCompliance=ciscoWirelessNotificationMIBCompliance, cwNotificationHistoryTableMaxLength=cwNotificationHistoryTableMaxLength, cWNotificationManagedObjectAddressType=cWNotificationManagedObjectAddressType, cWNotificationDescription=cWNotificationDescription, ciscoWirelessNotificationMIB=ciscoWirelessNotificationMIB, cWNotificationTimestamp=cWNotificationTimestamp, PYSNMP_MODULE_ID=ciscoWirelessNotificationMIB, cWNotificationSubCategory=cWNotificationSubCategory, ciscoWirelessMOStatusNotification=ciscoWirelessMOStatusNotification, cWNotificationIndex=cWNotificationIndex, ciscoWirelessNotificationMIBObjects=ciscoWirelessNotificationMIBObjects, cWNotificationUpdatedTimestamp=cWNotificationUpdatedTimestamp, ciscoWirelessNotificationsGroup=ciscoWirelessNotificationsGroup, ciscoWirelessNotificationMIBConform=ciscoWirelessNotificationMIBConform, cwNotificationHistoryTable=cwNotificationHistoryTable, ciscoWirelessNotificationEnableGroup=ciscoWirelessNotificationEnableGroup, cWNotificationSeverity=cWNotificationSeverity, ciscoWirelessNotificationMIBNotifs=ciscoWirelessNotificationMIBNotifs, CWirelessNotificationCategory=CWirelessNotificationCategory, ciscoWirelessNotificationMIBCompliances=ciscoWirelessNotificationMIBCompliances, cWNotificationManagedObjectAddress=cWNotificationManagedObjectAddress, ciscoWirelessNotificationConfigGroup=ciscoWirelessNotificationConfigGroup, cWNotificationKey=cWNotificationKey, ciscoWirelessNotificationObjectsGroup=ciscoWirelessNotificationObjectsGroup, cwNotificationMOStatusEnable=cwNotificationMOStatusEnable, cwNotificationHistoryEntry=cwNotificationHistoryEntry)
