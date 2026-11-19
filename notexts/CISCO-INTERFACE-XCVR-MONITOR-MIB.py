#
# PySNMP MIB module CISCO-INTERFACE-XCVR-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-INTERFACE-XCVR-MONITOR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoInterfaceXcvrMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 706))
ciscoInterfaceXcvrMonitorMIB.setRevisions(('2009-10-09 00:00',))
if mibBuilder.loadTexts: ciscoInterfaceXcvrMonitorMIB.setLastUpdated('200910090000Z')
if mibBuilder.loadTexts: ciscoInterfaceXcvrMonitorMIB.setOrganization('Cisco Systems, Inc.')
class CiscoInterfaceXcvrMonitorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("highSet", 1), ("lowSet", 2), ("highClear", 3), ("lowClear", 4), ("normal", 5))

ciscoInterfaceXcvrMonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 0))
ciscoInterfaceXcvrMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 1))
ciscoInterfaceXcvrMonMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 2))
cIfXcvrMonDigitalDiagTempAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 1), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTempAlarm.setStatus('current')
cIfXcvrMonDigitalDiagTempWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 2), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTempWarning.setStatus('current')
cIfXcvrMonDigitalDiagVoltAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 3), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagVoltAlarm.setStatus('current')
cIfXcvrMonDigitalDiagVoltWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 4), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagVoltWarning.setStatus('current')
cIfXcvrMonDigitalDiagCurrAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 5), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagCurrAlarm.setStatus('current')
cIfXcvrMonDigitalDiagCurrWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 6), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagCurrWarning.setStatus('current')
cIfXcvrMonDigitalDiagRxPwrAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 7), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagRxPwrAlarm.setStatus('current')
cIfXcvrMonDigitalDiagRxPwrWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 8), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagRxPwrWarning.setStatus('current')
cIfXcvrMonDigitalDiagTxPwrAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 9), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTxPwrAlarm.setStatus('current')
cIfXcvrMonDigitalDiagTxPwrWarning = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 10), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTxPwrWarning.setStatus('current')
cIfXcvrMonDigitalDiagTxFaultAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 11), CiscoInterfaceXcvrMonitorStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cIfXcvrMonDigitalDiagTxFaultAlarm.setStatus('current')
cIfXcvrMonStatusChangeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 706, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIfXcvrMonStatusChangeNotifEnable.setStatus('current')
cIfXcvrMonStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 706, 0, 1)).setObjects(("IF-MIB", "ifName"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxFaultAlarm"))
if mibBuilder.loadTexts: cIfXcvrMonStatusChangeNotif.setStatus('current')
ciscoInterfaceXcvrMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 1))
ciscoInterfaceXcvrMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2))
cIfXcvrMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 1, 1)).setObjects(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrDigitalDiagMonStatusGroup"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfXcvrMonMIBCompliance = cIfXcvrMonMIBCompliance.setStatus('current')
cIfXcvrDigitalDiagMonStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2, 1)).setObjects(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTempWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagVoltWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagCurrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagRxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxPwrWarning"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonDigitalDiagTxFaultAlarm"), ("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfXcvrDigitalDiagMonStatusGroup = cIfXcvrDigitalDiagMonStatusGroup.setStatus('current')
cIfXcvrMonStatusChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 706, 2, 2, 2)).setObjects(("CISCO-INTERFACE-XCVR-MONITOR-MIB", "cIfXcvrMonStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfXcvrMonStatusChangeNotifGroup = cIfXcvrMonStatusChangeNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACE-XCVR-MONITOR-MIB", cIfXcvrMonDigitalDiagCurrWarning=cIfXcvrMonDigitalDiagCurrWarning, cIfXcvrMonStatusChangeNotif=cIfXcvrMonStatusChangeNotif, ciscoInterfaceXcvrMonitorMIB=ciscoInterfaceXcvrMonitorMIB, ciscoInterfaceXcvrMonMIBGroups=ciscoInterfaceXcvrMonMIBGroups, cIfXcvrMonDigitalDiagTempWarning=cIfXcvrMonDigitalDiagTempWarning, cIfXcvrMonDigitalDiagVoltWarning=cIfXcvrMonDigitalDiagVoltWarning, PYSNMP_MODULE_ID=ciscoInterfaceXcvrMonitorMIB, ciscoInterfaceXcvrMonMIBNotifs=ciscoInterfaceXcvrMonMIBNotifs, cIfXcvrMonDigitalDiagCurrAlarm=cIfXcvrMonDigitalDiagCurrAlarm, cIfXcvrMonDigitalDiagVoltAlarm=cIfXcvrMonDigitalDiagVoltAlarm, ciscoInterfaceXcvrMonMIBObjects=ciscoInterfaceXcvrMonMIBObjects, CiscoInterfaceXcvrMonitorStatus=CiscoInterfaceXcvrMonitorStatus, cIfXcvrMonDigitalDiagTxPwrWarning=cIfXcvrMonDigitalDiagTxPwrWarning, cIfXcvrMonDigitalDiagTempAlarm=cIfXcvrMonDigitalDiagTempAlarm, cIfXcvrMonDigitalDiagRxPwrWarning=cIfXcvrMonDigitalDiagRxPwrWarning, ciscoInterfaceXcvrMonMIBConform=ciscoInterfaceXcvrMonMIBConform, cIfXcvrMonStatusChangeNotifEnable=cIfXcvrMonStatusChangeNotifEnable, cIfXcvrMonDigitalDiagRxPwrAlarm=cIfXcvrMonDigitalDiagRxPwrAlarm, cIfXcvrMonDigitalDiagTxPwrAlarm=cIfXcvrMonDigitalDiagTxPwrAlarm, cIfXcvrMonDigitalDiagTxFaultAlarm=cIfXcvrMonDigitalDiagTxFaultAlarm, ciscoInterfaceXcvrMonMIBCompliances=ciscoInterfaceXcvrMonMIBCompliances, cIfXcvrDigitalDiagMonStatusGroup=cIfXcvrDigitalDiagMonStatusGroup, cIfXcvrMonMIBCompliance=cIfXcvrMonMIBCompliance, cIfXcvrMonStatusChangeNotifGroup=cIfXcvrMonStatusChangeNotifGroup)
