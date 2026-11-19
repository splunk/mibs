#
# PySNMP MIB module CISCO-ACCESS-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ACCESS-ENVMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoEnvMonTemperatureState, ciscoEnvMonVoltageStatusDescr, ciscoEnvMonVoltageState, ciscoEnvMonSupplyStatusEntry, ciscoEnvMonTemperatureStatusDescr = mibBuilder.importSymbols("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState", "ciscoEnvMonVoltageStatusDescr", "ciscoEnvMonVoltageState", "ciscoEnvMonSupplyStatusEntry", "ciscoEnvMonTemperatureStatusDescr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAccessEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 61))
ciscoAccessEnvMonMIB.setRevisions(('1998-08-05 00:00',))
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setLastUpdated('9808050000Z')
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setOrganization('Cisco Systems, Inc.')
caemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 1))
caemSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1), )
if mibBuilder.loadTexts: caemSupplyStatusTable.setStatus('current')
caemSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1), )
ciscoEnvMonSupplyStatusEntry.registerAugmentions(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyStatusEntry"))
caemSupplyStatusEntry.setIndexNames(*ciscoEnvMonSupplyStatusEntry.getIndexNames())
if mibBuilder.loadTexts: caemSupplyStatusEntry.setStatus('current')
caemSupplyFailedComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("inputVoltage", 2), ("dcOutputVoltage", 3), ("thermal", 4), ("multiple", 5), ("fan", 6), ("overvoltage", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caemSupplyFailedComponent.setStatus('current')
caemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2))
caemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0))
caemTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 1)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
if mibBuilder.loadTexts: caemTemperatureNotification.setStatus('current')
caemVoltageNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
if mibBuilder.loadTexts: caemVoltageNotification.setStatus('current')
caemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3))
caemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1))
caemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2))
caemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemCompliance = caemCompliance.setStatus('current')
caemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyFailedComponent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemGroup = caemGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ACCESS-ENVMON-MIB", caemTemperatureNotification=caemTemperatureNotification, ciscoAccessEnvMonMIB=ciscoAccessEnvMonMIB, caemConformance=caemConformance, caemSupplyFailedComponent=caemSupplyFailedComponent, caemGroups=caemGroups, caemObjects=caemObjects, PYSNMP_MODULE_ID=ciscoAccessEnvMonMIB, caemGroup=caemGroup, caemVoltageNotification=caemVoltageNotification, caemCompliances=caemCompliances, caemSupplyStatusEntry=caemSupplyStatusEntry, caemCompliance=caemCompliance, caemMIBNotificationPrefix=caemMIBNotificationPrefix, caemMIBNotifications=caemMIBNotifications, caemSupplyStatusTable=caemSupplyStatusTable)
