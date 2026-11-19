#
# PySNMP MIB module CISCO-VLAN-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-GROUP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Cisco2KVlanList, = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, StorageType, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "RowStatus", "TextualConvention")
ciscoVlanGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 709))
ciscoVlanGroupMIB.setRevisions(('2011-03-22 00:00', '2009-11-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanGroupMIB.setRevisionsDescriptions(('Added cvgConfigTableSizeGroup.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setLastUpdated('201103220000Z')
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setDescription('MIB module for monitoring and configuring VLAN Group Mapping\n        information.')
ciscoVlanGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 0))
ciscoVlanGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 1))
ciscoVlanGroupMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2))
cvgConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1), )
if mibBuilder.loadTexts: cvgConfigTable.setStatus('current')
if mibBuilder.loadTexts: cvgConfigTable.setDescription('A list of VLAN groups configured in the system.')
cvgConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1), ).setIndexNames((0, "CISCO-VLAN-GROUP-MIB", "cvgConfigGroupName"))
if mibBuilder.loadTexts: cvgConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cvgConfigEntry.setDescription('An entry containing VLAN mapping configuration for a particular\n        VLAN group.  At least one VLAN must be associated with the group\n        specified by cvgConfigGroupName when the entry is created.')
cvgConfigGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvgConfigGroupName.setStatus('current')
if mibBuilder.loadTexts: cvgConfigGroupName.setDescription('The name of the VLAN group.')
cvgConfigVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 2), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansFirst2K.setStatus('current')
if mibBuilder.loadTexts: cvgConfigVlansFirst2K.setDescription('A string of octets containing one bit per VLAN for VLANs 0 to\n        2047.')
cvgConfigVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 3), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansSecond2K.setStatus('current')
if mibBuilder.loadTexts: cvgConfigVlansSecond2K.setDescription('A string of octets containing one bit per VLAN for VLANs 2048\n        to 4095.')
cvgConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: cvgConfigStorageType.setDescription('This object specifies the storage type for this conceptual row\n        in ciscoVlanGroupTable.')
cvgConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvgConfigRowStatus.setDescription('The status of this conceptual row.\n\n        All writable objects in this row may be modified at any time.')
cvgConfigTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvgConfigTableSize.setStatus('current')
if mibBuilder.loadTexts: cvgConfigTableSize.setDescription('Indicates the maximum number of entries that can\n        be created in cvgConfigTable. A value of zero indicates \n        no limit to the number of entries that can be created\n        in cvgConfigTable.')
ciscoVlanGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1))
ciscoVlanGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2))
ciscoVlanGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance = ciscoVlanGroupMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoVlanGroupMIBCompliance.setDescription('The compliance statement for entities which implement\n        CISCO-VLAN-GROUP-MIB.')
ciscoVlanGroupMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance2 = ciscoVlanGroupMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupMIBCompliance2.setDescription('The compliance statement for entities which implement\n        CISCO-VLAN-GROUP-MIB.')
ciscoVlanGroupConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansFirst2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansSecond2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigRowStatus"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupConfigGroup = ciscoVlanGroupConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupConfigGroup.setDescription('A collection of objects for VLAN Group configuration.')
cvgConfigTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvgConfigTableSizeGroup = cvgConfigTableSizeGroup.setStatus('current')
if mibBuilder.loadTexts: cvgConfigTableSizeGroup.setDescription('A collection of objects which provides the limit information\n        on the number of VLAN groups that can be created.')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-MIB", cvgConfigTable=cvgConfigTable, ciscoVlanGroupMIBGroups=ciscoVlanGroupMIBGroups, cvgConfigGroupName=cvgConfigGroupName, ciscoVlanGroupMIBCompliances=ciscoVlanGroupMIBCompliances, ciscoVlanGroupMIBCompliance=ciscoVlanGroupMIBCompliance, cvgConfigEntry=cvgConfigEntry, ciscoVlanGroupMIBCompliance2=ciscoVlanGroupMIBCompliance2, PYSNMP_MODULE_ID=ciscoVlanGroupMIB, cvgConfigRowStatus=cvgConfigRowStatus, cvgConfigTableSizeGroup=cvgConfigTableSizeGroup, cvgConfigVlansSecond2K=cvgConfigVlansSecond2K, ciscoVlanGroupConfigGroup=ciscoVlanGroupConfigGroup, cvgConfigVlansFirst2K=cvgConfigVlansFirst2K, cvgConfigTableSize=cvgConfigTableSize, ciscoVlanGroupMIBConform=ciscoVlanGroupMIBConform, ciscoVlanGroupMIBNotifs=ciscoVlanGroupMIBNotifs, ciscoVlanGroupMIB=ciscoVlanGroupMIB, ciscoVlanGroupMIBObjects=ciscoVlanGroupMIBObjects, cvgConfigStorageType=cvgConfigStorageType)
