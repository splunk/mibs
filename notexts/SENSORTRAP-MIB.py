#
# PySNMP MIB module SENSORTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/SENSORTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:39:51 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, ModuleIdentity, Counter32, TimeTicks, enterprises, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, NotificationType, Bits, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "TimeTicks", "enterprises", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "NotificationType", "Bits", "IpAddress", "NotificationType", "Gauge32")
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
mibBuilder.exportSymbols("SENSORTRAP-MIB", sensorAlarmTMax=sensorAlarmTMax, sensorAlarmTMin=sensorAlarmTMin, sensorIOAlarm=sensorIOAlarm, sensorHumidityAlarmRemoved=sensorHumidityAlarmRemoved, sensorIOAlarmRemoved=sensorIOAlarmRemoved, sensorHumidityLowAlarm=sensorHumidityLowAlarm, sensorTrapGroup=sensorTrapGroup, sensorHumidityAlarm=sensorHumidityAlarm, sensorHumidityLowAlarmRemoved=sensorHumidityLowAlarmRemoved, sensorAlarmTMinRemoved=sensorAlarmTMinRemoved, rielloMIB=rielloMIB, sensorgroup=sensorgroup, sensorId=sensorId, sensor=sensor, sensorAlarmTMaxRemoved=sensorAlarmTMaxRemoved)
