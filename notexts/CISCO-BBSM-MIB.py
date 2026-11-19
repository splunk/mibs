#
# PySNMP MIB module CISCO-BBSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BBSM-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ciscoBbsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 358))
ciscoBbsmMIB.setRevisions(('2004-04-03 00:00',))
if mibBuilder.loadTexts: ciscoBbsmMIB.setLastUpdated('200404030000Z')
if mibBuilder.loadTexts: ciscoBbsmMIB.setOrganization('Cisco Systems, Inc.')
ciscoBbsmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 0))
ciscoBbsmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 1))
ciscoBbsmEventInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1))
cbbsmEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventDescription.setStatus('current')
cbbsmEventSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventSource.setStatus('current')
cbbsmEventID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventID.setStatus('current')
cbbsmEventType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("information", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventType.setStatus('current')
cbbsmEventTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventTime.setStatus('current')
ciscoBbsmEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 358, 0, 1)).setObjects(("CISCO-BBSM-MIB", "cbbsmEventDescription"), ("CISCO-BBSM-MIB", "cbbsmEventSource"), ("CISCO-BBSM-MIB", "cbbsmEventID"), ("CISCO-BBSM-MIB", "cbbsmEventType"), ("CISCO-BBSM-MIB", "cbbsmEventTime"))
if mibBuilder.loadTexts: ciscoBbsmEvent.setStatus('current')
ciscoBbsmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2))
ciscoBbsmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1))
ciscoBbsmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2))
ciscoBbsmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1, 1)).setObjects(("CISCO-BBSM-MIB", "ciscoBbsmMIBGroup"), ("CISCO-BBSM-MIB", "ciscoBbsmMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBCompliance = ciscoBbsmMIBCompliance.setStatus('current')
ciscoBbsmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 1)).setObjects(("CISCO-BBSM-MIB", "cbbsmEventDescription"), ("CISCO-BBSM-MIB", "cbbsmEventSource"), ("CISCO-BBSM-MIB", "cbbsmEventID"), ("CISCO-BBSM-MIB", "cbbsmEventType"), ("CISCO-BBSM-MIB", "cbbsmEventTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBGroup = ciscoBbsmMIBGroup.setStatus('current')
ciscoBbsmMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 2)).setObjects(("CISCO-BBSM-MIB", "ciscoBbsmEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBNotificationGroup = ciscoBbsmMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-BBSM-MIB", cbbsmEventDescription=cbbsmEventDescription, ciscoBbsmEventInfo=ciscoBbsmEventInfo, cbbsmEventSource=cbbsmEventSource, cbbsmEventTime=cbbsmEventTime, ciscoBbsmMIBConformance=ciscoBbsmMIBConformance, ciscoBbsmMIBCompliances=ciscoBbsmMIBCompliances, ciscoBbsmMIBNotificationGroup=ciscoBbsmMIBNotificationGroup, ciscoBbsmEvent=ciscoBbsmEvent, ciscoBbsmMIBGroup=ciscoBbsmMIBGroup, ciscoBbsmMIB=ciscoBbsmMIB, ciscoBbsmMIBObjects=ciscoBbsmMIBObjects, PYSNMP_MODULE_ID=ciscoBbsmMIB, ciscoBbsmNotifications=ciscoBbsmNotifications, cbbsmEventID=cbbsmEventID, ciscoBbsmMIBCompliance=ciscoBbsmMIBCompliance, cbbsmEventType=cbbsmEventType, ciscoBbsmMIBGroups=ciscoBbsmMIBGroups)
