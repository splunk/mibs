#
# PySNMP MIB module CISCO-VLAN-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-GROUP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Cisco2KVlanList, = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention")
ciscoVlanGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 709))
ciscoVlanGroupMIB.setRevisions(('2011-03-22 00:00', '2009-11-20 00:00',))
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setLastUpdated('201103220000Z')
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setOrganization('Cisco Systems, Inc.')
ciscoVlanGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 0))
ciscoVlanGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 1))
ciscoVlanGroupMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2))
cvgConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1), )
if mibBuilder.loadTexts: cvgConfigTable.setStatus('current')
cvgConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1), ).setIndexNames((0, "CISCO-VLAN-GROUP-MIB", "cvgConfigGroupName"))
if mibBuilder.loadTexts: cvgConfigEntry.setStatus('current')
cvgConfigGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvgConfigGroupName.setStatus('current')
cvgConfigVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 2), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansFirst2K.setStatus('current')
cvgConfigVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 3), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansSecond2K.setStatus('current')
cvgConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigStorageType.setStatus('current')
cvgConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigRowStatus.setStatus('current')
cvgConfigTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvgConfigTableSize.setStatus('current')
ciscoVlanGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1))
ciscoVlanGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2))
ciscoVlanGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance = ciscoVlanGroupMIBCompliance.setStatus('deprecated')
ciscoVlanGroupMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance2 = ciscoVlanGroupMIBCompliance2.setStatus('current')
ciscoVlanGroupConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansFirst2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansSecond2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigRowStatus"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupConfigGroup = ciscoVlanGroupConfigGroup.setStatus('current')
cvgConfigTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvgConfigTableSizeGroup = cvgConfigTableSizeGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-MIB", cvgConfigTable=cvgConfigTable, cvgConfigVlansFirst2K=cvgConfigVlansFirst2K, PYSNMP_MODULE_ID=ciscoVlanGroupMIB, ciscoVlanGroupMIB=ciscoVlanGroupMIB, ciscoVlanGroupMIBCompliance=ciscoVlanGroupMIBCompliance, cvgConfigVlansSecond2K=cvgConfigVlansSecond2K, cvgConfigTableSizeGroup=cvgConfigTableSizeGroup, ciscoVlanGroupMIBCompliance2=ciscoVlanGroupMIBCompliance2, cvgConfigStorageType=cvgConfigStorageType, cvgConfigTableSize=cvgConfigTableSize, ciscoVlanGroupConfigGroup=ciscoVlanGroupConfigGroup, ciscoVlanGroupMIBGroups=ciscoVlanGroupMIBGroups, ciscoVlanGroupMIBNotifs=ciscoVlanGroupMIBNotifs, ciscoVlanGroupMIBConform=ciscoVlanGroupMIBConform, cvgConfigEntry=cvgConfigEntry, cvgConfigRowStatus=cvgConfigRowStatus, ciscoVlanGroupMIBCompliances=ciscoVlanGroupMIBCompliances, ciscoVlanGroupMIBObjects=ciscoVlanGroupMIBObjects, cvgConfigGroupName=cvgConfigGroupName)
