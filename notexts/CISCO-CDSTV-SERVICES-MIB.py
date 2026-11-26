#
# PySNMP MIB module CISCO-CDSTV-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CDSTV-SERVICES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoCdstvServicesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 729))
ciscoCdstvServicesMIB.setRevisions(('2010-03-29 00:00',))
if mibBuilder.loadTexts: ciscoCdstvServicesMIB.setLastUpdated('201003290000Z')
if mibBuilder.loadTexts: ciscoCdstvServicesMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvServicesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 0))
ciscoCdstvServicesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 1))
ciscoCdstvServicesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 2))
cdstvServicesMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1), )
if mibBuilder.loadTexts: cdstvServicesMonitorTable.setStatus('current')
cdstvServicesMonitorTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1), ).setIndexNames((0, "CISCO-CDSTV-SERVICES-MIB", "cdstvServicesMonitorIndex"))
if mibBuilder.loadTexts: cdstvServicesMonitorTableEntry.setStatus('current')
cdstvServicesMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cdstvServicesMonitorIndex.setStatus('current')
cdstvServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServiceName.setStatus('current')
cdstvServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServiceStatus.setStatus('current')
cdstvServiceTrapsEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2))
cdstvServiceUpNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServiceUpNotifEnable.setStatus('current')
cdstvServiceDownNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServiceDownNotifEnable.setStatus('current')
cdstvServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 729, 0, 1)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"))
if mibBuilder.loadTexts: cdstvServiceUp.setStatus('current')
cdstvServiceDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 729, 0, 2)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"))
if mibBuilder.loadTexts: cdstvServiceDown.setStatus('current')
ciscoCdstvServicesMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 1))
ciscoCdstvServicesMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2))
ciscoCdstvServicesMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 1, 1)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBMainObjectGroup"), ("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBNotificationGroup"), ("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBNotifEnableObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBCompliance = ciscoCdstvServicesMIBCompliance.setStatus('current')
ciscoCdstvServicesMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 1)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"), ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBMainObjectGroup = ciscoCdstvServicesMIBMainObjectGroup.setStatus('current')
ciscoCdstvServicesMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 2)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceUp"), ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBNotificationGroup = ciscoCdstvServicesMIBNotificationGroup.setStatus('current')
ciscoCdstvServicesMIBNotifEnableObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 3)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceUpNotifEnable"), ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceDownNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBNotifEnableObjectGroup = ciscoCdstvServicesMIBNotifEnableObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-SERVICES-MIB", ciscoCdstvServicesMIBNotificationGroup=ciscoCdstvServicesMIBNotificationGroup, cdstvServiceDown=cdstvServiceDown, cdstvServicesMonitorIndex=cdstvServicesMonitorIndex, ciscoCdstvServicesMIBObjects=ciscoCdstvServicesMIBObjects, cdstvServiceUp=cdstvServiceUp, ciscoCdstvServicesMIBNotifs=ciscoCdstvServicesMIBNotifs, PYSNMP_MODULE_ID=ciscoCdstvServicesMIB, cdstvServicesMonitorTableEntry=cdstvServicesMonitorTableEntry, cdstvServiceName=cdstvServiceName, cdstvServiceTrapsEnable=cdstvServiceTrapsEnable, ciscoCdstvServicesMIB=ciscoCdstvServicesMIB, ciscoCdstvServicesMIBCompliance=ciscoCdstvServicesMIBCompliance, cdstvServiceStatus=cdstvServiceStatus, cdstvServiceUpNotifEnable=cdstvServiceUpNotifEnable, ciscoCdstvServicesMIBNotifEnableObjectGroup=ciscoCdstvServicesMIBNotifEnableObjectGroup, ciscoCdstvServicesMIBMainObjectGroup=ciscoCdstvServicesMIBMainObjectGroup, ciscoCdstvServicesMIBConform=ciscoCdstvServicesMIBConform, cdstvServicesMonitorTable=cdstvServicesMonitorTable, ciscoCdstvServicesMIBCompliances=ciscoCdstvServicesMIBCompliances, cdstvServiceDownNotifEnable=cdstvServiceDownNotifEnable, ciscoCdstvServicesMIBGroups=ciscoCdstvServicesMIBGroups)
