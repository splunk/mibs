#
# PySNMP MIB module CISCO-LEC-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LEC-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
lecConfigEntry, = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "lecConfigEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLecExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 77))
ciscoLecExtMIB.setRevisions(('1997-05-09 12:30',))
if mibBuilder.loadTexts: ciscoLecExtMIB.setLastUpdated('9705091230Z')
if mibBuilder.loadTexts: ciscoLecExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoLecExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1))
cLecExtVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1))
cLecToVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1), )
if mibBuilder.loadTexts: cLecToVlanTable.setStatus('current')
cLecToVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1), )
lecConfigEntry.registerAugmentions(("CISCO-LEC-EXT-MIB", "cLecToVlanEntry"))
cLecToVlanEntry.setIndexNames(*lecConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cLecToVlanEntry.setStatus('current')
cLecToVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1, 1), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLecToVlanId.setStatus('current')
ciscoLecExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2))
ciscoLecExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2, 0))
ciscoLecExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3))
ciscoLecExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1))
ciscoLecExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2))
ciscoLecExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1, 1)).setObjects(("CISCO-LEC-EXT-MIB", "ciscoLecExtVlanMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtMIBCompliance = ciscoLecExtMIBCompliance.setStatus('current')
ciscoLecExtVlanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2, 1)).setObjects(("CISCO-LEC-EXT-MIB", "cLecToVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtVlanMIBGroup = ciscoLecExtVlanMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LEC-EXT-MIB", ciscoLecExtMIBConformance=ciscoLecExtMIBConformance, ciscoLecExtMIBNotifications=ciscoLecExtMIBNotifications, ciscoLecExtMIBCompliances=ciscoLecExtMIBCompliances, ciscoLecExtMIBGroups=ciscoLecExtMIBGroups, ciscoLecExtMIBNotificationPrefix=ciscoLecExtMIBNotificationPrefix, ciscoLecExtMIBObjects=ciscoLecExtMIBObjects, cLecToVlanEntry=cLecToVlanEntry, ciscoLecExtVlanMIBGroup=ciscoLecExtVlanMIBGroup, PYSNMP_MODULE_ID=ciscoLecExtMIB, ciscoLecExtMIBCompliance=ciscoLecExtMIBCompliance, ciscoLecExtMIB=ciscoLecExtMIB, cLecToVlanId=cLecToVlanId, cLecToVlanTable=cLecToVlanTable, cLecExtVlan=cLecExtVlan)
