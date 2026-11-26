#
# PySNMP MIB module DLINKSW-STORM-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-STORM-CTRL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:27 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, TimeTicks, Integer32, ModuleIdentity, iso, IpAddress, NotificationType, Counter32, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Integer32", "ModuleIdentity", "iso", "IpAddress", "NotificationType", "Counter32", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwStormCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 25))
dlinkSwStormCtrlMIB.setRevisions(('2013-06-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setRevisionsDescriptions(("This is the first version of the MIB file for 'Storm Control'\n            functionality.",))
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setLastUpdated('201306130000Z')
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setDescription('This MIB module defines objects for Storm Control')
class DStormCtlTrafficType(TextualConvention, Integer32):
    description = "The type of storm control traffic type.\n                broadcast(1) - broadcast storm.\n            multicast(2) - including unknown L2 multicast, known L2 \n                           multicast, unknown IP multicast and known \n                           IP multicast.\n            unicast(3) - when the action is configured as 'shutdown mode', \n                         unicast refers to both known and unknown \n                         unicast packet; Otherwise, unicast refers to \n                         unknown unicast packet. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("broadcast", 1), ("multicast", 2), ("unicast", 3))

class DStormCtlThrType(TextualConvention, Integer32):
    description = 'The type of storm control threshold is configured on an interface.\n            pps(1) - the threshold is configured as packet count per second. \n            kbps(2) - the threshold is configured as a rate of bits per second. \n            percentage(3) - the threshold is configured as a percentage of total \n                      bandwidth per port. \n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pps", 1), ("kbps", 2), ("percentage", 3))

class DStormCtlThrTypeValue(TextualConvention, Integer32):
    description = 'Denotes a generic threshold value.\n\n         A DStormCtlThrTypeValue value is always interpreted within the context\n         of a DStormCtlThrType value.  Every usage of the DStormCtlThrTypeValue\n         textual convention is required to specify the DStormCtlThrType\n         object that provides the context.  \n         The unit and valid range are as follows:\n         Threshold Type     Unit                      Valid Range\n         =============      =====================     =================\n         pps                packet per second         1 ~ 2147483647\n         kbps               bits per second           1 ~ 2147483647\n         percentage         percentage                1 ~ 100    \n         \n         The special value of -1 indicates this object is undefined.\n         '
    status = 'current'

dStormCtrlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 0))
dStormCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1))
dStormCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2))
dStormCtrlGentrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1))
dStormCtrlNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("stormOccurred", 2), ("stormCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlNotifyEnable.setDescription('This object controls when a storm control notification will be generated.\n\n            If the object is set to\n            none(1): No notifications will be generated.\n            stormOccurred(2): A notification will be generated when a storm event is\n                      detected.\n            stormCleared(3): A notification will be generated when a storm event is\n                      cleared.\n            both (4): A notification will be generated both when a storm event is \n                   detected and  cleared.\n            NOTE:The default value of this object is none(1).')
dStormCtrlPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 600)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlPollingInterval.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlPollingInterval.setDescription('The interval, in seconds, the switch detects the storm.')
dStormCtrlPollingRetries = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 360), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlPollingRetries.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlPollingRetries.setDescription("Specify the retry count. If the action is configured \n            as 'shutdown' mode and storm keep as long as \n            interval * retries, the port will enters error-disabled state.\n            \n            The effective range is from 1 to 360.\n            \n            0 means that a 'shutdown' mode port will directly enter \n            error-disabled state when storm is detected.\n            \n            -1 means that a 'shutdown' mode port will never enter \n            error-disabled state even if storm is detected.")
dStormCtrlThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2), )
if mibBuilder.loadTexts: dStormCtrlThresholdTable.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlThresholdTable.setDescription('A table consists of a list of interface-specific threshold\n            configuration for storm control.')
dStormCtrlThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"))
if mibBuilder.loadTexts: dStormCtrlThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlThresholdEntry.setDescription('An entry presents threshold configuration on an interface.')
dStormCtrlTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 1), DStormCtlTrafficType())
if mibBuilder.loadTexts: dStormCtrlTrafficType.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlTrafficType.setDescription('This object indicates the traffic type of the entry.')
dStormCtrlThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 2), DStormCtlThrType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlThresholdType.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlThresholdType.setDescription('This object indicates the threshold type of the entry.')
dStormCtrlRiseThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 3), DStormCtlThrTypeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlRiseThresholdValue.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlRiseThresholdValue.setDescription('Specifies the rise threshold value of the entry.\n            A special value of -1 indicates the storm control of the\n            corresponding traffic type is not enabled on that interface.\n            ')
dStormCtrlLowThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 4), DStormCtlThrTypeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlLowThresholdValue.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlLowThresholdValue.setDescription('Specifies the low level threshold.\n            A special value of -1 indicates low level is not specified.\n            The default value will be 80% of the value of the corresponding  \n            dStormCtrlRiseThresholdValue if applicable.')
dStormCtrlIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3), )
if mibBuilder.loadTexts: dStormCtrlIfTable.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlIfTable.setDescription('A table consists of a list of interface-specific configuration for \n            storm control.')
dStormCtrlIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dStormCtrlIfEntry.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlIfEntry.setDescription('An entry presents storm control configuration on an interface.            \n            ')
dStormCtrlIfActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("shutdown", 2), ("drop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlIfActionType.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlIfActionType.setDescription('Specify the action will be taken when storm occurs: \n              none(1) - Not filter the storm packets. \n              shutdown(2) - The storm-control shutdown the port when the rise threshold is reached.\n              drop(3) - The storm-control always discards packets that exceed the rise threshold.')
dStormCtrlTrafficInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4), )
if mibBuilder.loadTexts: dStormCtrlTrafficInfoTable.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlTrafficInfoTable.setDescription('A table consists of a list of status information for traffic types\n            on interfaces. Only the interface/traffic-type on which the storm\n            control is enabled will present on this table.\n            ')
dStormCtrlTrafficInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"))
if mibBuilder.loadTexts: dStormCtrlTrafficInfoEntry.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlTrafficInfoEntry.setDescription('An entry presents the status of a traffic type on an interface.')
dStormCtrlCurTrafficUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 1), DStormCtlThrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlCurTrafficUnitType.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlCurTrafficUnitType.setDescription('This object indicates the current traffic unit of the entry.')
dStormCtrlCurTrafficValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 2), DStormCtlThrTypeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlCurTrafficValue.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlCurTrafficValue.setDescription('Indicating the current traffic value on the interface.\n            ')
dStormCtrlTrafficInfoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("forwarding", 1), ("dropped", 2), ("errorDisabled", 3), ("linkDown", 4), ("inactive", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlTrafficInfoStatus.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlTrafficInfoStatus.setDescription('This object indicates the current status of storm control on a\n            given interface for a given traffic type. \n            forwarding(1): no storm event has been detected.\n            dropped(2): a storm event has occurred and the storm traffic\n                        exceeding the threshold is dropped. \n            errorDisabled(3): the port is disabled due to a storm. \n            linkDown(4): the port is physically linked down.\n            inactive(5): Indicates that storm control is not \n                         enabled for the given traffic type.\n            ')
dStormCtrlNotifyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5))
dStormCtrlNotifyTrafficType = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5, 1), DStormCtlTrafficType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dStormCtrlNotifyTrafficType.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlNotifyTrafficType.setDescription('This object is used by dStormCtrlOccurred and dStormCtrlStormCleared\n              to indicate the traffic type of the occurred storm.')
dStormCtrlOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if mibBuilder.loadTexts: dStormCtrlOccurred.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlOccurred.setDescription("This trap is sent when dStormCtrlNotifyEnable is 'stormOccurred'\n            or 'both' and a storm is detected.")
dStormCtrlStormCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if mibBuilder.loadTexts: dStormCtrlStormCleared.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlStormCleared.setDescription("This trap is sent when dStormCtrlNotifyEnable is 'stormCleared'\n            or 'both' and a storm is cleared.")
dStormCtrlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1))
dStormCtrlCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1, 1)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlBaiscGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlCompliance = dStormCtrlCompliance.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlCompliance.setDescription('The compliance statement for entities which implement the \n            DLINKSW-STORM-CTRL-MIB.')
dStormCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2))
dStormCtrlBaiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 1)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyEnable"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingInterval"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingRetries"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlThresholdType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlRiseThresholdValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlLowThresholdValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlIfActionType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficUnitType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficInfoStatus"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlBaiscGroup = dStormCtrlBaiscGroup.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlBaiscGroup.setDescription('A collection of objects providing the information for storm control')
dStormCtrlNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 2)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlOccurred"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlStormCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlNotifyGroup = dStormCtrlNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: dStormCtrlNotifyGroup.setDescription('The collection of notifications used for storm control.')
mibBuilder.exportSymbols("DLINKSW-STORM-CTRL-MIB", dStormCtrlGentrl=dStormCtrlGentrl, dStormCtrlCompliance=dStormCtrlCompliance, dStormCtrlCompliances=dStormCtrlCompliances, dStormCtrlCurTrafficValue=dStormCtrlCurTrafficValue, dStormCtrlMIBConformance=dStormCtrlMIBConformance, dStormCtrlMIBNotifications=dStormCtrlMIBNotifications, dStormCtrlLowThresholdValue=dStormCtrlLowThresholdValue, dStormCtrlBaiscGroup=dStormCtrlBaiscGroup, DStormCtlThrTypeValue=DStormCtlThrTypeValue, DStormCtlTrafficType=DStormCtlTrafficType, dStormCtrlThresholdType=dStormCtrlThresholdType, dStormCtrlIfEntry=dStormCtrlIfEntry, dStormCtrlNotifyGroup=dStormCtrlNotifyGroup, dStormCtrlPollingInterval=dStormCtrlPollingInterval, dStormCtrlThresholdTable=dStormCtrlThresholdTable, dStormCtrlMIBObjects=dStormCtrlMIBObjects, dStormCtrlIfTable=dStormCtrlIfTable, PYSNMP_MODULE_ID=dlinkSwStormCtrlMIB, dStormCtrlIfActionType=dStormCtrlIfActionType, dStormCtrlTrafficType=dStormCtrlTrafficType, dStormCtrlTrafficInfoTable=dStormCtrlTrafficInfoTable, dStormCtrlOccurred=dStormCtrlOccurred, dStormCtrlNotifyEnable=dStormCtrlNotifyEnable, dStormCtrlThresholdEntry=dStormCtrlThresholdEntry, dStormCtrlTrafficInfoEntry=dStormCtrlTrafficInfoEntry, dStormCtrlTrafficInfoStatus=dStormCtrlTrafficInfoStatus, dStormCtrlPollingRetries=dStormCtrlPollingRetries, dStormCtrlNotifyTrafficType=dStormCtrlNotifyTrafficType, dStormCtrlCurTrafficUnitType=dStormCtrlCurTrafficUnitType, dStormCtrlRiseThresholdValue=dStormCtrlRiseThresholdValue, dStormCtrlGroup=dStormCtrlGroup, dStormCtrlStormCleared=dStormCtrlStormCleared, dStormCtrlNotifyInfo=dStormCtrlNotifyInfo, DStormCtlThrType=DStormCtlThrType, dlinkSwStormCtrlMIB=dlinkSwStormCtrlMIB)
