#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelationshipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 128))
ciscoVlanIfTableRelationshipMIB.setRevisions(('2013-07-15 00:00',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setLastUpdated('9904010530Z')
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setOrganization('Cisco Systems, Inc.')
cviMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1))
cviGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1))
cviVlanInterfaceIndexTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1), )
if mibBuilder.loadTexts: cviVlanInterfaceIndexTable.setStatus('current')
cviVlanInterfaceIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviVlanId"), (0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviPhysicalIfIndex"))
if mibBuilder.loadTexts: cviVlanInterfaceIndexEntry.setStatus('current')
cviVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cviVlanId.setStatus('current')
cviPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cviPhysicalIfIndex.setStatus('current')
cviRoutedVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cviRoutedVlanIfIndex.setStatus('current')
cviMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3))
cviMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1))
cviMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2))
cviMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBCompliance = cviMIBCompliance.setStatus('current')
cviMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviRoutedVlanIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBGroup = cviMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", cviMIBGroups=cviMIBGroups, ciscoVlanIfTableRelationshipMIB=ciscoVlanIfTableRelationshipMIB, cviGlobals=cviGlobals, cviMIBObjects=cviMIBObjects, cviVlanInterfaceIndexTable=cviVlanInterfaceIndexTable, cviVlanId=cviVlanId, cviMIBGroup=cviMIBGroup, cviRoutedVlanIfIndex=cviRoutedVlanIfIndex, cviVlanInterfaceIndexEntry=cviVlanInterfaceIndexEntry, cviPhysicalIfIndex=cviPhysicalIfIndex, PYSNMP_MODULE_ID=ciscoVlanIfTableRelationshipMIB, cviMIBConformance=cviMIBConformance, cviMIBCompliance=cviMIBCompliance, cviMIBCompliances=cviMIBCompliances)
