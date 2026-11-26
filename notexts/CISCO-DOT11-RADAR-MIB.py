#
# PySNMP MIB module CISCO-DOT11-RADAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-RADAR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDot11RadarMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 627))
ciscoDot11RadarMIB.setRevisions(('2007-05-07 00:00',))
if mibBuilder.loadTexts: ciscoDot11RadarMIB.setLastUpdated('200705070000Z')
if mibBuilder.loadTexts: ciscoDot11RadarMIB.setOrganization('Cisco System Inc.')
ciscoDot11RadarMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 0))
ciscoDot11RadarMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 1))
ciscoDot11RadarMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 2))
cdrDot11RadarNotifConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1))
cdrDot11RadarDetectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2))
cdrDot11NewFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 1), Unsigned32().clone(0)).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrDot11NewFrequency.setStatus('current')
cdrDot11PreferFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 2), Unsigned32().clone(0)).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrDot11PreferFrequency.setStatus('current')
cdrChannelSwitchLastTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrChannelSwitchLastTime.setStatus('current')
cdrChannelReturnLastTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrChannelReturnLastTime.setStatus('current')
cdrChannelSwitchNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdrChannelSwitchNotifEnabled.setStatus('current')
cdrChannelReturnNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdrChannelReturnNotifEnabled.setStatus('current')
ciscoDot11RadarChannelSwitch = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 627, 0, 1)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11NewFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchLastTime"))
if mibBuilder.loadTexts: ciscoDot11RadarChannelSwitch.setStatus('current')
ciscoDot11RadarChannelReturn = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 627, 0, 2)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11PreferFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnLastTime"))
if mibBuilder.loadTexts: ciscoDot11RadarChannelReturn.setStatus('current')
ciscoDot11RadarMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 1))
ciscoDot11RadarMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2))
ciscoDot11RadarCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 1, 1)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11RadarNotifObjectGroup"), ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarDetectInfoGroup"), ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadarCompliance = ciscoDot11RadarCompliance.setStatus('current')
cdrDot11RadarNotifObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 1)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchNotifEnabled"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdrDot11RadarNotifObjectGroup = cdrDot11RadarNotifObjectGroup.setStatus('current')
ciscoDot11RadarDetectInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 2)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11NewFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrDot11PreferFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchLastTime"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnLastTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadarDetectInfoGroup = ciscoDot11RadarDetectInfoGroup.setStatus('current')
ciscoDot11RadarNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 3)).setObjects(("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarChannelSwitch"), ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarChannelReturn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadarNotificationGroup = ciscoDot11RadarNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-RADAR-MIB", cdrChannelSwitchNotifEnabled=cdrChannelSwitchNotifEnabled, cdrDot11PreferFrequency=cdrDot11PreferFrequency, cdrDot11RadarDetectInfo=cdrDot11RadarDetectInfo, ciscoDot11RadarMIBCompliances=ciscoDot11RadarMIBCompliances, cdrChannelReturnLastTime=cdrChannelReturnLastTime, cdrDot11RadarNotifConfig=cdrDot11RadarNotifConfig, ciscoDot11RadarMIBConform=ciscoDot11RadarMIBConform, ciscoDot11RadarCompliance=ciscoDot11RadarCompliance, PYSNMP_MODULE_ID=ciscoDot11RadarMIB, cdrChannelReturnNotifEnabled=cdrChannelReturnNotifEnabled, ciscoDot11RadarNotificationGroup=ciscoDot11RadarNotificationGroup, cdrChannelSwitchLastTime=cdrChannelSwitchLastTime, cdrDot11RadarNotifObjectGroup=cdrDot11RadarNotifObjectGroup, ciscoDot11RadarMIBObjects=ciscoDot11RadarMIBObjects, ciscoDot11RadarChannelSwitch=ciscoDot11RadarChannelSwitch, ciscoDot11RadarChannelReturn=ciscoDot11RadarChannelReturn, ciscoDot11RadarMIBGroups=ciscoDot11RadarMIBGroups, ciscoDot11RadarDetectInfoGroup=ciscoDot11RadarDetectInfoGroup, ciscoDot11RadarMIB=ciscoDot11RadarMIB, cdrDot11NewFrequency=cdrDot11NewFrequency, ciscoDot11RadarMIBNotifs=ciscoDot11RadarMIBNotifs)
