#
# PySNMP MIB module CISCO-ACCESS-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ACCESS-ENVMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoEnvMonVoltageState, ciscoEnvMonTemperatureState, ciscoEnvMonTemperatureStatusDescr, ciscoEnvMonSupplyStatusEntry, ciscoEnvMonVoltageStatusDescr = mibBuilder.importSymbols("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState", "ciscoEnvMonTemperatureState", "ciscoEnvMonTemperatureStatusDescr", "ciscoEnvMonSupplyStatusEntry", "ciscoEnvMonVoltageStatusDescr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
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
mibBuilder.exportSymbols("CISCO-ACCESS-ENVMON-MIB", ciscoAccessEnvMonMIB=ciscoAccessEnvMonMIB, caemCompliance=caemCompliance, caemVoltageNotification=caemVoltageNotification, caemConformance=caemConformance, caemObjects=caemObjects, PYSNMP_MODULE_ID=ciscoAccessEnvMonMIB, caemMIBNotificationPrefix=caemMIBNotificationPrefix, caemGroups=caemGroups, caemCompliances=caemCompliances, caemSupplyStatusEntry=caemSupplyStatusEntry, caemSupplyStatusTable=caemSupplyStatusTable, caemMIBNotifications=caemMIBNotifications, caemTemperatureNotification=caemTemperatureNotification, caemGroup=caemGroup, caemSupplyFailedComponent=caemSupplyFailedComponent)
