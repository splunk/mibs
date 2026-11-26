#
# PySNMP MIB module SENSORTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/SENSORTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:14:16 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, enterprises, Integer32, Bits, iso, Counter32, Gauge32, ModuleIdentity, TimeTicks, NotificationType, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "enterprises", "Integer32", "Bits", "iso", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "NotificationType", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rielloMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 5491))
sensorgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5491, 9))
sensor = MibIdentifier((1, 3, 6, 1, 4, 1, 5491, 9, 1))
sensorId = MibScalar((1, 3, 6, 1, 4, 1, 5491, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorId.setStatus('mandatory')
sensorTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2))
sensorAlarmTMax = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,1)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorAlarmTMaxRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,2)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorAlarmTMin = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,3)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorAlarmTMinRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,4)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorIOAlarm = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,5)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorIOAlarmRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,6)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityAlarm = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,7)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityAlarmRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,8)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,9)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityLowAlarmRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,10)).setObjects(("SENSORTRAP-MIB", "sensorId"))
mibBuilder.exportSymbols("SENSORTRAP-MIB", sensorHumidityLowAlarm=sensorHumidityLowAlarm, sensor=sensor, sensorHumidityAlarm=sensorHumidityAlarm, sensorHumidityLowAlarmRemoved=sensorHumidityLowAlarmRemoved, sensorAlarmTMinRemoved=sensorAlarmTMinRemoved, sensorIOAlarmRemoved=sensorIOAlarmRemoved, rielloMIB=rielloMIB, sensorAlarmTMax=sensorAlarmTMax, sensorAlarmTMin=sensorAlarmTMin, sensorIOAlarm=sensorIOAlarm, sensorId=sensorId, sensorHumidityAlarmRemoved=sensorHumidityAlarmRemoved, sensorgroup=sensorgroup, sensorAlarmTMaxRemoved=sensorAlarmTMaxRemoved, sensorTrapGroup=sensorTrapGroup)
