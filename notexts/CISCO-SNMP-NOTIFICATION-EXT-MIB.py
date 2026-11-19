#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-NOTIFICATION-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
snmpNotifyFilterEntry, = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpNotificationExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 408))
ciscoSnmpNotificationExtMIB.setRevisions(('2004-05-12 00:00',))
if mibBuilder.loadTexts: ciscoSnmpNotificationExtMIB.setLastUpdated('200405120000Z')
if mibBuilder.loadTexts: ciscoSnmpNotificationExtMIB.setOrganization('Cisco Systems, Inc.')
csneMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 0))
csneMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 1))
csneMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2))
csneNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1))
csneSnmpNotifyFilterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1), )
if mibBuilder.loadTexts: csneSnmpNotifyFilterTable.setStatus('current')
csneSnmpNotifyFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1), )
snmpNotifyFilterEntry.registerAugmentions(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneSnmpNotifyFilterEntry"))
csneSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())
if mibBuilder.loadTexts: csneSnmpNotifyFilterEntry.setStatus('current')
csneFilterAdminTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 1), Unsigned32().clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csneFilterAdminTimer.setStatus('current')
csneFilterOperTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csneFilterOperTimer.setStatus('current')
csneFilterTimerUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("seconds", 1), ("minutes", 2), ("hours", 3))).clone('minutes')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csneFilterTimerUnit.setStatus('current')
csneMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1))
csneMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2))
csneMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1, 1)).setObjects(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneNotifyFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csneMIBCompliance = csneMIBCompliance.setStatus('current')
csneNotifyFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2, 1)).setObjects(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterOperTimer"), ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterAdminTimer"), ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterTimerUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csneNotifyFilterGroup = csneNotifyFilterGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-EXT-MIB", csneFilterTimerUnit=csneFilterTimerUnit, csneSnmpNotifyFilterEntry=csneSnmpNotifyFilterEntry, csneMIBNotifs=csneMIBNotifs, csneMIBObjects=csneMIBObjects, csneNotifyObjects=csneNotifyObjects, PYSNMP_MODULE_ID=ciscoSnmpNotificationExtMIB, csneSnmpNotifyFilterTable=csneSnmpNotifyFilterTable, csneMIBGroups=csneMIBGroups, csneNotifyFilterGroup=csneNotifyFilterGroup, csneFilterAdminTimer=csneFilterAdminTimer, csneMIBCompliance=csneMIBCompliance, csneMIBCompliances=csneMIBCompliances, csneMIBConform=csneMIBConform, csneFilterOperTimer=csneFilterOperTimer, ciscoSnmpNotificationExtMIB=ciscoSnmpNotificationExtMIB)
