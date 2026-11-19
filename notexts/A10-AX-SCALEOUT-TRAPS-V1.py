#
# PySNMP MIB module A10-AX-SCALEOUT-TRAPS-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/A10-AX-SCALEOUT-TRAPS-V1
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
axNotification, axLogging = mibBuilder.importSymbols("A10-AX-MIB", "axNotification", "axLogging")
axNotificationScaleOutStatus, axNotificationScaleOutNumberOfDevice, axNotificationMsg, axNotificationScaleOutTrafficMapType, axNotificationScaleOutDeviceId, axNotifications = mibBuilder.importSymbols("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus", "axNotificationScaleOutNumberOfDevice", "axNotificationMsg", "axNotificationScaleOutTrafficMapType", "axNotificationScaleOutDeviceId", "axNotifications")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Counter32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, ModuleIdentity, MibIdentifier, Bits, iso, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Counter32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Bits", "iso", "IpAddress", "NotificationType")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
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
mibBuilder.exportSymbols("A10-AX-SCALEOUT-TRAPS-V1", axScaleoutServiceMaster=axScaleoutServiceMaster, axScaleoutLocalNodeDisabled=axScaleoutLocalNodeDisabled, axScaleoutSingleNodeStatus=axScaleoutSingleNodeStatus, axScaleoutElection=axScaleoutElection, axScaleoutTrafficMapDistribution=axScaleoutTrafficMapDistribution, axScaleoutTrafficMapUpdate=axScaleoutTrafficMapUpdate, axScaleoutNotifications=axScaleoutNotifications, axScaleoutMasterNodeCallingReelection=axScaleoutMasterNodeCallingReelection, axScaleoutNodeStatus=axScaleoutNodeStatus, axScaleoutVserverTrafficMap=axScaleoutVserverTrafficMap)
