#
# PySNMP MIB module CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoWanPersistentXgcpEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 18))
ciscoWanPersistentXgcpEventsMIB.setRevisions(('2003-10-20 00:00',))
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setLastUpdated('200310200000Z')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanPersistentXgcpEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1))
persistentXgcpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1))
persistentXgcpEventsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1), )
if mibBuilder.loadTexts: persistentXgcpEventsTable.setStatus('current')
persistentXgcpEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"))
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setStatus('current')
persistentXgcpEventNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: persistentXgcpEventNum.setStatus('current')
persistentXgcpEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventName.setStatus('current')
persistentXgcpEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setStatus('current')
persistentXgcpEventsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2))
persistentXgcpEventsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1))
persistentXgcpEventsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2))
persistentXgcpEventsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBCompliance = persistentXgcpEventsMIBCompliance.setStatus('current')
persistentXgcpEventsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"), ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBGroup = persistentXgcpEventsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", ciscoWanPersistentXgcpEventsMIB=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEvents=persistentXgcpEvents, persistentXgcpEventName=persistentXgcpEventName, persistentXgcpEventNum=persistentXgcpEventNum, persistentXgcpEventsTable=persistentXgcpEventsTable, persistentXgcpEventRowStatus=persistentXgcpEventRowStatus, persistentXgcpEventsEntry=persistentXgcpEventsEntry, ciscoWanPersistentXgcpEventsMIBObjects=ciscoWanPersistentXgcpEventsMIBObjects, persistentXgcpEventsMIBCompliances=persistentXgcpEventsMIBCompliances, PYSNMP_MODULE_ID=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventsMIBGroups=persistentXgcpEventsMIBGroups, persistentXgcpEventsMIBCompliance=persistentXgcpEventsMIBCompliance, persistentXgcpEventsMIBConformance=persistentXgcpEventsMIBConformance, persistentXgcpEventsMIBGroup=persistentXgcpEventsMIBGroup)
