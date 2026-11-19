#
# PySNMP MIB module CISCO-IF-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IF-LOOPBACK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoIfLoopbackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9399))
ciscoIfLoopbackMIB.setRevisions(('2001-11-15 00:00',))
if mibBuilder.loadTexts: ciscoIfLoopbackMIB.setLastUpdated('200111150000Z')
if mibBuilder.loadTexts: ciscoIfLoopbackMIB.setOrganization('Cisco Systems, Inc.')
ciscoIfLoopbackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1))
ciscoIfLoopbackConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1))
cifLConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1), )
if mibBuilder.loadTexts: cifLConfTable.setStatus('current')
cifLConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cifLConfEntry.setStatus('current')
cifLLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("farEndLineLoopback", 1), ("farEndPayloadLoopback", 2), ("remoteLineLoopback", 3), ("remotePayloadLoopback", 4), ("localLoopback", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifLLoopback.setStatus('current')
cifLLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("completed", 1), ("inProgress", 2), ("clockOutOfSync", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifLLoopbackStatus.setStatus('current')
cifLFELoopbackDeviceAndCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("nonLatchOCUwith1", 1), ("nonLatchOCUwithout1", 2), ("nonLatchCSU", 3), ("nonLatchDSU", 4), ("latchDS0Drop", 5), ("latchDS0Line", 6), ("latchOCU", 7), ("latchCSU", 8), ("latchDSU", 9), ("latchHL96", 10), ("v54PN127Polynomial", 11), ("lineInband", 12), ("lineLoopbackESF", 13), ("payloadLoopbackESF", 14), ("noCode", 15), ("lineLoopbackFEAC", 16), ("smartJackInband", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifLFELoopbackDeviceAndCode.setStatus('current')
cifLRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifLRowStatus.setStatus('current')
ciscoIfLoopbackMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8))
ciscoIfLoopbackMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1))
ciscoIfLoopbackMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2))
ciscoIfLoopbackMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1, 1)).setObjects(("CISCO-IF-LOOPBACK-MIB", "ciscoIfLoopbackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfLoopbackMIBCompliance = ciscoIfLoopbackMIBCompliance.setStatus('current')
ciscoIfLoopbackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2, 1)).setObjects(("CISCO-IF-LOOPBACK-MIB", "cifLLoopback"), ("CISCO-IF-LOOPBACK-MIB", "cifLLoopbackStatus"), ("CISCO-IF-LOOPBACK-MIB", "cifLFELoopbackDeviceAndCode"), ("CISCO-IF-LOOPBACK-MIB", "cifLRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfLoopbackGroup = ciscoIfLoopbackGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-LOOPBACK-MIB", ciscoIfLoopbackMIBObjects=ciscoIfLoopbackMIBObjects, cifLFELoopbackDeviceAndCode=cifLFELoopbackDeviceAndCode, ciscoIfLoopbackMIBCompliances=ciscoIfLoopbackMIBCompliances, PYSNMP_MODULE_ID=ciscoIfLoopbackMIB, ciscoIfLoopbackConfig=ciscoIfLoopbackConfig, ciscoIfLoopbackMIBCompliance=ciscoIfLoopbackMIBCompliance, ciscoIfLoopbackMIB=ciscoIfLoopbackMIB, cifLLoopback=cifLLoopback, ciscoIfLoopbackGroup=ciscoIfLoopbackGroup, cifLLoopbackStatus=cifLLoopbackStatus, cifLConfEntry=cifLConfEntry, ciscoIfLoopbackMIBGroups=ciscoIfLoopbackMIBGroups, ciscoIfLoopbackMIBConformance=ciscoIfLoopbackMIBConformance, cifLRowStatus=cifLRowStatus, cifLConfTable=cifLConfTable)
