#
# PySNMP MIB module CISCO-FC-SDV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-SDV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcAddressId, DomainIdOrZero, FcNameIdOrZero = mibBuilder.importSymbols("CISCO-ST-TC", "FcAddressId", "DomainIdOrZero", "FcNameIdOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
FcList, = mibBuilder.importSymbols("CISCO-ZS-MIB", "FcList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, RowStatus, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "StorageType")
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
mibBuilder.exportSymbols("CISCO-FC-SDV-MIB", cFcSdvVirtRealDevMapStorageType=cFcSdvVirtRealDevMapStorageType, ciscoFcSdvMIBConform=ciscoFcSdvMIBConform, CiscoFcSdvDevId=CiscoFcSdvDevId, cFcSdvVdName=cFcSdvVdName, ciscoFcSdvMIBGroups=ciscoFcSdvMIBGroups, ciscoFcSdvMIBCompliance=ciscoFcSdvMIBCompliance, cFcSdvVdIndex=cFcSdvVdIndex, cFcSdvVirtRealDevMapEntry=cFcSdvVirtRealDevMapEntry, ciscoFcSdvConfigGroup=ciscoFcSdvConfigGroup, cFcSdvVdNwwn=cFcSdvVdNwwn, PYSNMP_MODULE_ID=ciscoFcSdvMIB, cFcSdvVirtRealDevMapTable=cFcSdvVirtRealDevMapTable, cFcSdvVirtDeviceTable=cFcSdvVirtDeviceTable, cFcSdvVirtRealDevMapIndex=cFcSdvVirtRealDevMapIndex, cFcSdvVirtRealDeviceIdType=cFcSdvVirtRealDeviceIdType, cFcSdvVirtRealDevMapType=cFcSdvVirtRealDevMapType, cFcSdvVdStorageType=cFcSdvVdStorageType, ciscoFcSdvMIB=ciscoFcSdvMIB, cFcSdvVdVirtDomain=cFcSdvVdVirtDomain, CiscoFcSdvDevIdType=CiscoFcSdvDevIdType, CiscoFcSdvRealDevMapType=CiscoFcSdvRealDevMapType, cFcSdvVdRowStatus=cFcSdvVdRowStatus, cFcSdvVdPwwn=cFcSdvVdPwwn, cFcSdvVirtRealDevMapRowStatus=cFcSdvVirtRealDevMapRowStatus, cFcSdvVdFcId=cFcSdvVdFcId, ciscoFcSdvMIBObjects=ciscoFcSdvMIBObjects, ciscoFcSdvMIBCompliances=ciscoFcSdvMIBCompliances, cFcSdvVdRealDevMapList=cFcSdvVdRealDevMapList, cFcSdvVirtRealDeviceId=cFcSdvVirtRealDeviceId, cFcSdvConfig=cFcSdvConfig, cFcSdvVirtDeviceEntry=cFcSdvVirtDeviceEntry, cFcSdvVdAssignedFcId=cFcSdvVdAssignedFcId, ciscoFcSdvMIBNotifs=ciscoFcSdvMIBNotifs)
