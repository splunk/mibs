#
# PySNMP MIB module A10-AX-SCALEOUT-TRAPS-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/A10-AX-SCALEOUT-TRAPS-V1
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:03 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
axNotification, axLogging = mibBuilder.importSymbols("A10-AX-MIB", "axNotification", "axLogging")
axNotificationScaleOutStatus, axNotifications, axNotificationMsg, axNotificationScaleOutDeviceId, axNotificationScaleOutNumberOfDevice, axNotificationScaleOutTrafficMapType = mibBuilder.importSymbols("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus", "axNotifications", "axNotificationMsg", "axNotificationScaleOutDeviceId", "axNotificationScaleOutNumberOfDevice", "axNotificationScaleOutTrafficMapType")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Integer32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
axScaleoutNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7))
axScaleoutVserverTrafficMap = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,1)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
axScaleoutLocalNodeDisabled = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,2)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
axScaleoutServiceMaster = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,3)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutDeviceId"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus"))
axScaleoutSingleNodeStatus = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,4)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus"))
axScaleoutElection = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,5)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutNumberOfDevice"))
axScaleoutMasterNodeCallingReelection = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,6)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
axScaleoutNodeStatus = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,7)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutDeviceId"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus"))
axScaleoutTrafficMapUpdate = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,8)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutTrafficMapType"))
axScaleoutTrafficMapDistribution = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,9)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
mibBuilder.exportSymbols("A10-AX-SCALEOUT-TRAPS-V1", axScaleoutLocalNodeDisabled=axScaleoutLocalNodeDisabled, axScaleoutNodeStatus=axScaleoutNodeStatus, axScaleoutElection=axScaleoutElection, axScaleoutServiceMaster=axScaleoutServiceMaster, axScaleoutTrafficMapUpdate=axScaleoutTrafficMapUpdate, axScaleoutMasterNodeCallingReelection=axScaleoutMasterNodeCallingReelection, axScaleoutNotifications=axScaleoutNotifications, axScaleoutSingleNodeStatus=axScaleoutSingleNodeStatus, axScaleoutTrafficMapDistribution=axScaleoutTrafficMapDistribution, axScaleoutVserverTrafficMap=axScaleoutVserverTrafficMap)
