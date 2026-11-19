#
# PySNMP MIB module CISCO-FC-SDV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-SDV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameIdOrZero, DomainIdOrZero, FcAddressId = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameIdOrZero", "DomainIdOrZero", "FcAddressId")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
FcList, = mibBuilder.importSymbols("CISCO-ZS-MIB", "FcList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "RowStatus", "DisplayString")
ciscoFcSdvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 593))
ciscoFcSdvMIB.setRevisions(('2006-09-26 00:00',))
if mibBuilder.loadTexts: ciscoFcSdvMIB.setLastUpdated('200609260000Z')
if mibBuilder.loadTexts: ciscoFcSdvMIB.setOrganization('Cisco Systems, Inc.')
ciscoFcSdvMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 0))
ciscoFcSdvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 1))
ciscoFcSdvMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 2))
cFcSdvConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1))
class CiscoFcSdvDevIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("singleDevPWWN", 1), ("singleDevDevAlias", 2))

class CiscoFcSdvDevId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CiscoFcSdvRealDevMapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primaryDevMap", 1), ("secondaryDevMap", 2))

cFcSdvVirtDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1), )
if mibBuilder.loadTexts: cFcSdvVirtDeviceTable.setStatus('current')
cFcSdvVirtDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FC-SDV-MIB", "cFcSdvVdIndex"))
if mibBuilder.loadTexts: cFcSdvVirtDeviceEntry.setStatus('current')
cFcSdvVdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: cFcSdvVdIndex.setStatus('current')
cFcSdvVdName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdName.setStatus('current')
cFcSdvVdVirtDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 3), DomainIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdVirtDomain.setStatus('current')
cFcSdvVdFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 4), FcAddressId().clone(hexValue="000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdFcId.setStatus('current')
cFcSdvVdPwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 5), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdPwwn.setStatus('current')
cFcSdvVdNwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 6), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdNwwn.setStatus('current')
cFcSdvVdAssignedFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 7), FcAddressId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdAssignedFcId.setStatus('current')
cFcSdvVdRealDevMapList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 8), FcList().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdRealDevMapList.setStatus('current')
cFcSdvVdStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdStorageType.setStatus('current')
cFcSdvVdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdRowStatus.setStatus('current')
cFcSdvVirtRealDevMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2), )
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapTable.setStatus('current')
cFcSdvVirtRealDevMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FC-SDV-MIB", "cFcSdvVdIndex"), (0, "CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapIndex"))
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapEntry.setStatus('current')
cFcSdvVirtRealDevMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapIndex.setStatus('current')
cFcSdvVirtRealDeviceIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 2), CiscoFcSdvDevIdType().clone('singleDevPWWN')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDeviceIdType.setStatus('current')
cFcSdvVirtRealDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 3), CiscoFcSdvDevId().subtype(subtypeSpec=ValueSizeConstraint(1, 64)).clone(hexValue="0000000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDeviceId.setStatus('current')
cFcSdvVirtRealDevMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 4), CiscoFcSdvRealDevMapType().clone('secondaryDevMap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapType.setStatus('current')
cFcSdvVirtRealDevMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapStorageType.setStatus('current')
cFcSdvVirtRealDevMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapRowStatus.setStatus('current')
ciscoFcSdvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 1))
ciscoFcSdvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 2))
ciscoFcSdvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 1, 1)).setObjects(("CISCO-FC-SDV-MIB", "ciscoFcSdvConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcSdvMIBCompliance = ciscoFcSdvMIBCompliance.setStatus('current')
ciscoFcSdvConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 2, 1)).setObjects(("CISCO-FC-SDV-MIB", "cFcSdvVdName"), ("CISCO-FC-SDV-MIB", "cFcSdvVdVirtDomain"), ("CISCO-FC-SDV-MIB", "cFcSdvVdFcId"), ("CISCO-FC-SDV-MIB", "cFcSdvVdPwwn"), ("CISCO-FC-SDV-MIB", "cFcSdvVdNwwn"), ("CISCO-FC-SDV-MIB", "cFcSdvVdAssignedFcId"), ("CISCO-FC-SDV-MIB", "cFcSdvVdStorageType"), ("CISCO-FC-SDV-MIB", "cFcSdvVdRealDevMapList"), ("CISCO-FC-SDV-MIB", "cFcSdvVdRowStatus"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDeviceIdType"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDeviceId"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapType"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapStorageType"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcSdvConfigGroup = ciscoFcSdvConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-SDV-MIB", ciscoFcSdvMIBCompliance=ciscoFcSdvMIBCompliance, PYSNMP_MODULE_ID=ciscoFcSdvMIB, ciscoFcSdvMIBObjects=ciscoFcSdvMIBObjects, cFcSdvVdStorageType=cFcSdvVdStorageType, cFcSdvVirtDeviceEntry=cFcSdvVirtDeviceEntry, cFcSdvVirtRealDevMapIndex=cFcSdvVirtRealDevMapIndex, ciscoFcSdvMIBNotifs=ciscoFcSdvMIBNotifs, cFcSdvVdAssignedFcId=cFcSdvVdAssignedFcId, CiscoFcSdvDevId=CiscoFcSdvDevId, CiscoFcSdvDevIdType=CiscoFcSdvDevIdType, cFcSdvVdPwwn=cFcSdvVdPwwn, cFcSdvVirtRealDeviceIdType=cFcSdvVirtRealDeviceIdType, cFcSdvVdRealDevMapList=cFcSdvVdRealDevMapList, CiscoFcSdvRealDevMapType=CiscoFcSdvRealDevMapType, ciscoFcSdvMIBCompliances=ciscoFcSdvMIBCompliances, cFcSdvConfig=cFcSdvConfig, cFcSdvVdFcId=cFcSdvVdFcId, cFcSdvVirtRealDevMapTable=cFcSdvVirtRealDevMapTable, cFcSdvVirtRealDevMapType=cFcSdvVirtRealDevMapType, ciscoFcSdvMIB=ciscoFcSdvMIB, cFcSdvVirtRealDeviceId=cFcSdvVirtRealDeviceId, cFcSdvVdIndex=cFcSdvVdIndex, ciscoFcSdvConfigGroup=ciscoFcSdvConfigGroup, cFcSdvVdName=cFcSdvVdName, ciscoFcSdvMIBConform=ciscoFcSdvMIBConform, ciscoFcSdvMIBGroups=ciscoFcSdvMIBGroups, cFcSdvVirtDeviceTable=cFcSdvVirtDeviceTable, cFcSdvVdRowStatus=cFcSdvVdRowStatus, cFcSdvVdVirtDomain=cFcSdvVdVirtDomain, cFcSdvVdNwwn=cFcSdvVdNwwn, cFcSdvVirtRealDevMapRowStatus=cFcSdvVirtRealDevMapRowStatus, cFcSdvVirtRealDevMapEntry=cFcSdvVirtRealDevMapEntry, cFcSdvVirtRealDevMapStorageType=cFcSdvVirtRealDevMapStorageType)
