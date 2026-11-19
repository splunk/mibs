#
# PySNMP MIB module CISCO-INTERFACETOPN-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-INTERFACETOPN-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
interfaceTopNControlEntry, = mibBuilder.importSymbols("INTERFACETOPN-MIB", "interfaceTopNControlEntry")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoInterfaceTopNExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 482))
ciscoInterfaceTopNExtMIB.setRevisions(('2010-10-19 00:00', '2008-01-15 00:00', '2006-03-15 00:00',))
if mibBuilder.loadTexts: ciscoInterfaceTopNExtMIB.setLastUpdated('201010190000Z')
if mibBuilder.loadTexts: ciscoInterfaceTopNExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoInterfaceTopNExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 0))
ciscoInterfaceTopNExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 1))
ciscoInterfaceTopNExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 2))
citneInterfaceTopNCaps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 1), Bits().clone(namedValues=NamedValues(("utilization", 0), ("bytes", 1), ("packets", 2), ("broadcast", 3), ("multicast", 4), ("overflow", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: citneInterfaceTopNCaps.setStatus('current')
citneInterfaceTopNControlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2), )
if mibBuilder.loadTexts: citneInterfaceTopNControlTable.setStatus('current')
citneInterfaceTopNControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1), )
interfaceTopNControlEntry.registerAugmentions(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNControlEntry"))
citneInterfaceTopNControlEntry.setIndexNames(*interfaceTopNControlEntry.getIndexNames())
if mibBuilder.loadTexts: citneInterfaceTopNControlEntry.setStatus('current')
citneInterfaceTopNCounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("utilization", 2), ("bytes", 3), ("packets", 4), ("broadcast", 5), ("multicast", 6), ("overflow", 7))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citneInterfaceTopNCounterType.setStatus('current')
citneInterfaceTopNInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("all", 1), ("ethernet", 2), ("fastEthernet", 3), ("gigaEthernet", 4), ("tenGigaEthernet", 5), ("portChannel", 6), ("layer2", 7), ("layer3", 8), ("fortyGigaEthernet", 9))).clone('all')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citneInterfaceTopNInterfaceType.setStatus('current')
citneInterfaceTopNVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 3), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citneInterfaceTopNVlanNumber.setStatus('current')
ciscoIfTopNExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1))
ciscoIfTopNExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2))
ciscoIfTopNExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1, 1)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtCapsGroup"), ("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtControlGroup"), ("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtCtrlVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtMIBCompliance = ciscoIfTopNExtMIBCompliance.setStatus('current')
ciscoIfTopNExtCapsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 1)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCaps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtCapsGroup = ciscoIfTopNExtCapsGroup.setStatus('current')
ciscoIfTopNExtControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 2)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCounterType"), ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNInterfaceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtControlGroup = ciscoIfTopNExtControlGroup.setStatus('current')
ciscoIfTopNExtCtrlVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 3)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNVlanNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtCtrlVlanGroup = ciscoIfTopNExtCtrlVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-EXT-MIB", citneInterfaceTopNInterfaceType=citneInterfaceTopNInterfaceType, citneInterfaceTopNVlanNumber=citneInterfaceTopNVlanNumber, citneInterfaceTopNCounterType=citneInterfaceTopNCounterType, PYSNMP_MODULE_ID=ciscoInterfaceTopNExtMIB, ciscoInterfaceTopNExtMIBConform=ciscoInterfaceTopNExtMIBConform, citneInterfaceTopNCaps=citneInterfaceTopNCaps, ciscoInterfaceTopNExtMIBObjects=ciscoInterfaceTopNExtMIBObjects, citneInterfaceTopNControlTable=citneInterfaceTopNControlTable, ciscoIfTopNExtControlGroup=ciscoIfTopNExtControlGroup, ciscoIfTopNExtCtrlVlanGroup=ciscoIfTopNExtCtrlVlanGroup, citneInterfaceTopNControlEntry=citneInterfaceTopNControlEntry, ciscoInterfaceTopNExtMIB=ciscoInterfaceTopNExtMIB, ciscoInterfaceTopNExtMIBNotifs=ciscoInterfaceTopNExtMIBNotifs, ciscoIfTopNExtCapsGroup=ciscoIfTopNExtCapsGroup, ciscoIfTopNExtMIBCompliances=ciscoIfTopNExtMIBCompliances, ciscoIfTopNExtMIBGroups=ciscoIfTopNExtMIBGroups, ciscoIfTopNExtMIBCompliance=ciscoIfTopNExtMIBCompliance)
