#
# PySNMP MIB module CISCO-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MRP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-MRP-MIB", ciscoMrpDomainState=ciscoMrpDomainState, ciscoMrpMIBCompliance=ciscoMrpMIBCompliance, PYSNMP_MODULE_ID=ciscoMrpMIB, ciscoMrpDomainID=ciscoMrpDomainID, ciscoMrpMIBNotifs=ciscoMrpMIBNotifs, ciscoMrpMIBConform=ciscoMrpMIBConform, ciscoMrpDomainTable=ciscoMrpDomainTable, ciscoMrpMIBCompliances=ciscoMrpMIBCompliances, ciscoMrpMIBGroups=ciscoMrpMIBGroups, ciscoMrpMIBMainObjectGroup=ciscoMrpMIBMainObjectGroup, ciscoMrpMIBObjects=ciscoMrpMIBObjects, ciscoMrpMIB=ciscoMrpMIB, ciscoMrpDomainIndex=ciscoMrpDomainIndex, ciscoMrpMIBNotificationGroup=ciscoMrpMIBNotificationGroup, ciscoMrpDomainName=ciscoMrpDomainName, ciscoMrpDomainEntry=ciscoMrpDomainEntry, ciscoMrpRingOpen=ciscoMrpRingOpen)
