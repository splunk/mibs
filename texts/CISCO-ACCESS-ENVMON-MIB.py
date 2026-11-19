#
# PySNMP MIB module CISCO-ACCESS-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ACCESS-ENVMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoEnvMonTemperatureState, ciscoEnvMonVoltageStatusDescr, ciscoEnvMonSupplyStatusEntry, ciscoEnvMonTemperatureStatusDescr, ciscoEnvMonVoltageState = mibBuilder.importSymbols("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState", "ciscoEnvMonVoltageStatusDescr", "ciscoEnvMonSupplyStatusEntry", "ciscoEnvMonTemperatureStatusDescr", "ciscoEnvMonVoltageState")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAccessEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 61))
ciscoAccessEnvMonMIB.setRevisions(('1998-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setRevisionsDescriptions(('Rename the enumerated values for caemSupplyFailedComponent \n                 and add fan, overvoltage failure events to it. \n                 Add caemVoltageNotification.\n                ',))
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setLastUpdated('9808050000Z')
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n \n                Tel: +1 800 553-NETS\n \n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setDescription('The MIB module to describe the additional status of\n                 the Environmental Monitor on those Cisco Access devices\n                 which support one.\n                ')
caemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 1))
caemSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1), )
if mibBuilder.loadTexts: caemSupplyStatusTable.setStatus('current')
if mibBuilder.loadTexts: caemSupplyStatusTable.setDescription('The table contains the additional power supply information\n             that are not covered in the ciscoEnvMonSupplyStatusTable of\n             CISCO-ENVMON-MIB.                                \n            ')
caemSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1), )
ciscoEnvMonSupplyStatusEntry.registerAugmentions(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyStatusEntry"))
caemSupplyStatusEntry.setIndexNames(*ciscoEnvMonSupplyStatusEntry.getIndexNames())
if mibBuilder.loadTexts: caemSupplyStatusEntry.setStatus('current')
if mibBuilder.loadTexts: caemSupplyStatusEntry.setDescription("Additional information about the failure component or location\n             in the power Supply beyond that provided by Cisco Environmental\n             Monitor MIB's ciscoEnvMonSupplyStatusEntry.\n            ")
caemSupplyFailedComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("inputVoltage", 2), ("dcOutputVoltage", 3), ("thermal", 4), ("multiple", 5), ("fan", 6), ("overvoltage", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caemSupplyFailedComponent.setStatus('current')
if mibBuilder.loadTexts: caemSupplyFailedComponent.setDescription('The failure component of the power supply being instrumented.\n         none            - No failure.\n         inputVoltage    - Input power lost in one of the power supplies\n         dcOutputVoltage - DC output voltage lost in one of the power supplies\n         thermal         - Power supply thermal failure.\n         multiple        - Multiple failures.\n         fan             - Fan failure\n         overvoltage     - Over voltage.\n        ')
caemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2))
caemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0))
caemTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 1)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
if mibBuilder.loadTexts: caemTemperatureNotification.setStatus('current')
if mibBuilder.loadTexts: caemTemperatureNotification.setDescription("A caemTemperatureNotification is sent if the over temperature\n         condition is detected in the managed system.\n         This is a replacement for the ciscoEnvMonTemperatureNotification \n         trap because the information 'ciscoEnvMonTemperatureStatusValue' \n         required by the trap is not available in the managed system.\n        ")
caemVoltageNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
if mibBuilder.loadTexts: caemVoltageNotification.setStatus('current')
if mibBuilder.loadTexts: caemVoltageNotification.setDescription("A caemVoltageNotification is sent if the over voltage \n         condition is detected and ciscoEnvMonVoltageState is not set\n         to 'notPresent' in the managed system.\n         This is a replacement for the ciscoEnvMonVoltageNotification \n         trap because the information 'ciscoEnvMonVoltageStatusValue' \n         required by the trap is not available in the managed system.\n        ")
caemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3))
caemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1))
caemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2))
caemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemCompliance = caemCompliance.setStatus('current')
if mibBuilder.loadTexts: caemCompliance.setDescription('The compliance statement for entities which implement\n             the Cisco Environmental Monitor Supplemental MIB.')
caemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyFailedComponent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemGroup = caemGroup.setStatus('current')
if mibBuilder.loadTexts: caemGroup.setDescription('A collection of objects providing the additional Environmental\n             Monitor information beyond that provided by\n             Cisco Environmental Monitor MIB.\n            ')
mibBuilder.exportSymbols("CISCO-ACCESS-ENVMON-MIB", caemSupplyFailedComponent=caemSupplyFailedComponent, caemGroups=caemGroups, caemGroup=caemGroup, PYSNMP_MODULE_ID=ciscoAccessEnvMonMIB, caemVoltageNotification=caemVoltageNotification, caemMIBNotifications=caemMIBNotifications, caemSupplyStatusEntry=caemSupplyStatusEntry, caemTemperatureNotification=caemTemperatureNotification, ciscoAccessEnvMonMIB=ciscoAccessEnvMonMIB, caemObjects=caemObjects, caemMIBNotificationPrefix=caemMIBNotificationPrefix, caemSupplyStatusTable=caemSupplyStatusTable, caemCompliance=caemCompliance, caemCompliances=caemCompliances, caemConformance=caemConformance)
