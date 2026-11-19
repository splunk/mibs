#
# PySNMP MIB module ARUBAWIRED-FANTRAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBAWIRED-FANTRAY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
arubaWiredChassisMIB, = mibBuilder.importSymbols("ARUBAWIRED-CHASSIS-MIB", "arubaWiredChassisMIB")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Bits, Gauge32, TimeTicks, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Bits", "Gauge32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredFanTray = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4))
arubaWiredFanTray.setRevisions(('2020-02-13 00:00',))
if mibBuilder.loadTexts: arubaWiredFanTray.setLastUpdated('202002130000Z')
if mibBuilder.loadTexts: arubaWiredFanTray.setOrganization('HPE/Aruba Networking Division')
arubaWiredFanTrayNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 0))
arubaWiredFanTrayStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 0, 1)).setObjects(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayName"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayState"))
if mibBuilder.loadTexts: arubaWiredFanTrayStateNotification.setStatus('current')
arubaWiredFanTrayTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1), )
if mibBuilder.loadTexts: arubaWiredFanTrayTable.setStatus('current')
arubaWiredFanTrayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1), ).setIndexNames((0, "ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayGroupIndex"), (0, "ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTraySlotIndex"))
if mibBuilder.loadTexts: arubaWiredFanTrayEntry.setStatus('current')
arubaWiredFanTrayGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: arubaWiredFanTrayGroupIndex.setStatus('current')
arubaWiredFanTraySlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: arubaWiredFanTraySlotIndex.setStatus('current')
arubaWiredFanTrayName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredFanTrayName.setStatus('current')
arubaWiredFanTrayState = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredFanTrayState.setStatus('current')
arubaWiredFanTrayProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredFanTrayProductName.setStatus('current')
arubaWiredFanTraySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredFanTraySerialNumber.setStatus('current')
arubaWiredFanTrayNumberFans = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredFanTrayNumberFans.setStatus('current')
arubaWiredFanTrayConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99))
arubaWiredFanTrayCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 1))
arubaWiredFanTrayGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 2))
arubaWiredFanTrayCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 1, 1)).setObjects(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayTable"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayNotificationsGroup"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredFanTrayCompliance = arubaWiredFanTrayCompliance.setStatus('current')
arubaWiredFanTrayTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 2, 1)).setObjects(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayName"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayState"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayProductName"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTraySerialNumber"), ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayNumberFans"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredFanTrayTableGroup = arubaWiredFanTrayTableGroup.setStatus('current')
arubaWiredFanTrayNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 2, 2)).setObjects(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayStateNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredFanTrayNotificationsGroup = arubaWiredFanTrayNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-FANTRAY-MIB", arubaWiredFanTrayCompliances=arubaWiredFanTrayCompliances, PYSNMP_MODULE_ID=arubaWiredFanTray, arubaWiredFanTrayGroupIndex=arubaWiredFanTrayGroupIndex, arubaWiredFanTraySerialNumber=arubaWiredFanTraySerialNumber, arubaWiredFanTraySlotIndex=arubaWiredFanTraySlotIndex, arubaWiredFanTrayTable=arubaWiredFanTrayTable, arubaWiredFanTray=arubaWiredFanTray, arubaWiredFanTrayName=arubaWiredFanTrayName, arubaWiredFanTrayTableGroup=arubaWiredFanTrayTableGroup, arubaWiredFanTrayGroups=arubaWiredFanTrayGroups, arubaWiredFanTrayStateNotification=arubaWiredFanTrayStateNotification, arubaWiredFanTrayNumberFans=arubaWiredFanTrayNumberFans, arubaWiredFanTrayConformance=arubaWiredFanTrayConformance, arubaWiredFanTrayNotificationsGroup=arubaWiredFanTrayNotificationsGroup, arubaWiredFanTrayState=arubaWiredFanTrayState, arubaWiredFanTrayNotifications=arubaWiredFanTrayNotifications, arubaWiredFanTrayProductName=arubaWiredFanTrayProductName, arubaWiredFanTrayEntry=arubaWiredFanTrayEntry, arubaWiredFanTrayCompliance=arubaWiredFanTrayCompliance)
