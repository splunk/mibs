#
# PySNMP MIB module SENSORTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/SENSORTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:39:34 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter32, TimeTicks, MibIdentifier, Gauge32, Counter64, enterprises, ObjectIdentity, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter32", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "enterprises", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SENSORTRAP-MIB", sensorgroup=sensorgroup, sensorAlarmTMin=sensorAlarmTMin, rielloMIB=rielloMIB, sensorAlarmTMax=sensorAlarmTMax, sensorId=sensorId, sensorAlarmTMaxRemoved=sensorAlarmTMaxRemoved, sensorHumidityAlarm=sensorHumidityAlarm, sensorAlarmTMinRemoved=sensorAlarmTMinRemoved, sensorHumidityAlarmRemoved=sensorHumidityAlarmRemoved, sensorIOAlarmRemoved=sensorIOAlarmRemoved, sensorIOAlarm=sensorIOAlarm, sensorHumidityLowAlarmRemoved=sensorHumidityLowAlarmRemoved, sensorHumidityLowAlarm=sensorHumidityLowAlarm, sensor=sensor, sensorTrapGroup=sensorTrapGroup)
