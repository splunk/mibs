#
# PySNMP MIB module CISCO-FC-DEVICE-ALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-DEVICE-ALIAS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
CdpvmDevType, = mibBuilder.importSymbols("CISCO-DYNAMIC-PORT-VSAN-MIB", "CdpvmDevType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoFcDeviceAliasMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 430))
ciscoFcDeviceAliasMIB.setRevisions(('2004-09-20 00:00',))
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setLastUpdated('200409200000Z')
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setOrganization('Cisco Systems Inc.')
cfdaMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 0))
cfdaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 1))
cfdaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2))
cfdaConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1))
cfdaConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1), )
if mibBuilder.loadTexts: cfdaConfigTable.setStatus('current')
cfdaConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceAlias"))
if mibBuilder.loadTexts: cfdaConfigEntry.setStatus('current')
cfdaConfigDeviceAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cfdaConfigDeviceAlias.setStatus('current')
cfdaConfigDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 2), CdpvmDevType().clone('pwwn')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigDeviceType.setStatus('current')
cfdaConfigDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigDeviceId.setStatus('current')
cfdaConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigRowStatus.setStatus('current')
ciscoFcDaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1))
ciscoFcDaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2))
ciscoFcDaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1, 1)).setObjects(("CISCO-FC-DEVICE-ALIAS-MIB", "ciscoFcDaConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcDaMIBCompliance = ciscoFcDaMIBCompliance.setStatus('current')
ciscoFcDaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2, 1)).setObjects(("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceType"), ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceId"), ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcDaConfigGroup = ciscoFcDaConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-DEVICE-ALIAS-MIB", ciscoFcDaMIBCompliances=ciscoFcDaMIBCompliances, cfdaMIBObjects=cfdaMIBObjects, cfdaMIBNotifs=cfdaMIBNotifs, cfdaConfigDeviceId=cfdaConfigDeviceId, PYSNMP_MODULE_ID=ciscoFcDeviceAliasMIB, cfdaConfigRowStatus=cfdaConfigRowStatus, cfdaConfigDeviceType=cfdaConfigDeviceType, ciscoFcDaMIBGroups=ciscoFcDaMIBGroups, ciscoFcDaMIBCompliance=ciscoFcDaMIBCompliance, cfdaMIBConform=cfdaMIBConform, cfdaConfigTable=cfdaConfigTable, cfdaConfigEntry=cfdaConfigEntry, ciscoFcDeviceAliasMIB=ciscoFcDeviceAliasMIB, cfdaConfiguration=cfdaConfiguration, ciscoFcDaConfigGroup=ciscoFcDaConfigGroup, cfdaConfigDeviceAlias=cfdaConfigDeviceAlias)
