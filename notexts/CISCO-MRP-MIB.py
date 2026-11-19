#
# PySNMP MIB module CISCO-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MRP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:42 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 850))
ciscoMrpMIB.setRevisions(('2017-09-12 00:00',))
if mibBuilder.loadTexts: ciscoMrpMIB.setLastUpdated('201709120000Z')
if mibBuilder.loadTexts: ciscoMrpMIB.setOrganization('Cisco Systems, Inc.')
ciscoMrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 0))
ciscoMrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 1))
ciscoMrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2))
ciscoMrpDomainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1), )
if mibBuilder.loadTexts: ciscoMrpDomainTable.setStatus('current')
ciscoMrpDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1), ).setIndexNames((0, "CISCO-MRP-MIB", "ciscoMrpDomainIndex"))
if mibBuilder.loadTexts: ciscoMrpDomainEntry.setStatus('current')
ciscoMrpDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciscoMrpDomainIndex.setStatus('current')
ciscoMrpDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainID.setStatus('current')
ciscoMrpDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainName.setStatus('current')
ciscoMrpDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainState.setStatus('current')
ciscoMrpRingOpen = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 850, 0, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpDomainID"), ("CISCO-MRP-MIB", "ciscoMrpDomainName"), ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
if mibBuilder.loadTexts: ciscoMrpRingOpen.setStatus('current')
ciscoMrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1))
ciscoMrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2))
ciscoMrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpMIBMainObjectGroup"), ("CISCO-MRP-MIB", "ciscoMrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBCompliance = ciscoMrpMIBCompliance.setStatus('current')
ciscoMrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpDomainID"), ("CISCO-MRP-MIB", "ciscoMrpDomainName"), ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBMainObjectGroup = ciscoMrpMIBMainObjectGroup.setStatus('current')
ciscoMrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 2)).setObjects(("CISCO-MRP-MIB", "ciscoMrpRingOpen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBNotificationGroup = ciscoMrpMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MRP-MIB", ciscoMrpDomainID=ciscoMrpDomainID, ciscoMrpDomainIndex=ciscoMrpDomainIndex, ciscoMrpDomainName=ciscoMrpDomainName, ciscoMrpMIBNotifs=ciscoMrpMIBNotifs, ciscoMrpMIBObjects=ciscoMrpMIBObjects, ciscoMrpDomainEntry=ciscoMrpDomainEntry, ciscoMrpMIBNotificationGroup=ciscoMrpMIBNotificationGroup, ciscoMrpRingOpen=ciscoMrpRingOpen, ciscoMrpMIBMainObjectGroup=ciscoMrpMIBMainObjectGroup, PYSNMP_MODULE_ID=ciscoMrpMIB, ciscoMrpMIBConform=ciscoMrpMIBConform, ciscoMrpMIBCompliance=ciscoMrpMIBCompliance, ciscoMrpDomainTable=ciscoMrpDomainTable, ciscoMrpMIBCompliances=ciscoMrpMIBCompliances, ciscoMrpMIB=ciscoMrpMIB, ciscoMrpDomainState=ciscoMrpDomainState, ciscoMrpMIBGroups=ciscoMrpMIBGroups)
