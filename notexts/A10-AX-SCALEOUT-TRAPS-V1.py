#
# PySNMP MIB module A10-AX-SCALEOUT-TRAPS-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/A10-AX-SCALEOUT-TRAPS-V1
# Produced by pysmi-1.1.12 at Thu Nov 26 06:04:31 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
axNotification, axLogging = mibBuilder.importSymbols("A10-AX-MIB", "axNotification", "axLogging")
axNotifications, axNotificationScaleOutStatus, axNotificationScaleOutDeviceId, axNotificationScaleOutNumberOfDevice, axNotificationMsg, axNotificationScaleOutTrafficMapType = mibBuilder.importSymbols("A10-AX-NOTIF-OBJ", "axNotifications", "axNotificationScaleOutStatus", "axNotificationScaleOutDeviceId", "axNotificationScaleOutNumberOfDevice", "axNotificationMsg", "axNotificationScaleOutTrafficMapType")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Gauge32, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, NotificationType, Counter64, ModuleIdentity, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity", "iso", "Bits", "IpAddress")
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
mibBuilder.exportSymbols("A10-AX-SCALEOUT-TRAPS-V1", axScaleoutTrafficMapDistribution=axScaleoutTrafficMapDistribution, axScaleoutNodeStatus=axScaleoutNodeStatus, axScaleoutLocalNodeDisabled=axScaleoutLocalNodeDisabled, axScaleoutServiceMaster=axScaleoutServiceMaster, axScaleoutMasterNodeCallingReelection=axScaleoutMasterNodeCallingReelection, axScaleoutSingleNodeStatus=axScaleoutSingleNodeStatus, axScaleoutElection=axScaleoutElection, axScaleoutTrafficMapUpdate=axScaleoutTrafficMapUpdate, axScaleoutNotifications=axScaleoutNotifications, axScaleoutVserverTrafficMap=axScaleoutVserverTrafficMap)
