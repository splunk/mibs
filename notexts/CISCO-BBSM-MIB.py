#
# PySNMP MIB module CISCO-BBSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BBSM-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
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
mibBuilder.exportSymbols("CISCO-BBSM-MIB", cbbsmEventTime=cbbsmEventTime, ciscoBbsmMIBGroup=ciscoBbsmMIBGroup, ciscoBbsmEvent=ciscoBbsmEvent, ciscoBbsmMIBGroups=ciscoBbsmMIBGroups, ciscoBbsmMIBConformance=ciscoBbsmMIBConformance, cbbsmEventSource=cbbsmEventSource, ciscoBbsmMIBCompliance=ciscoBbsmMIBCompliance, ciscoBbsmMIBNotificationGroup=ciscoBbsmMIBNotificationGroup, cbbsmEventDescription=cbbsmEventDescription, ciscoBbsmEventInfo=ciscoBbsmEventInfo, cbbsmEventID=cbbsmEventID, ciscoBbsmNotifications=ciscoBbsmNotifications, ciscoBbsmMIB=ciscoBbsmMIB, ciscoBbsmMIBCompliances=ciscoBbsmMIBCompliances, ciscoBbsmMIBObjects=ciscoBbsmMIBObjects, cbbsmEventType=cbbsmEventType, PYSNMP_MODULE_ID=ciscoBbsmMIB)
