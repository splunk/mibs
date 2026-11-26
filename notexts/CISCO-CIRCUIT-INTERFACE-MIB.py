#
# PySNMP MIB module CISCO-CIRCUIT-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CIRCUIT-INTERFACE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoCircuitInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 160))
ciscoCircuitInterfaceMIB.setRevisions(('2000-05-09 00:00',))
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setLastUpdated('200005090000Z')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setOrganization('Cisco Systems, Inc.')
ciscoCircuitInterfaceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1))
cciDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1))
cciDescriptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1), )
if mibBuilder.loadTexts: cciDescriptionTable.setStatus('current')
cciDescriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cciDescriptionEntry.setStatus('current')
cciDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciDescr.setStatus('current')
cciStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciStatus.setStatus('current')
ciscoCircuitInterfaceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3))
ciscoCircuitInterfaceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1))
ciscoCircuitInterfaceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2))
ciscoCircuitInterfaceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "ciscoCircuitInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceMIBCompliance = ciscoCircuitInterfaceMIBCompliance.setStatus('current')
ciscoCircuitInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "cciDescr"), ("CISCO-CIRCUIT-INTERFACE-MIB", "cciStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceGroup = ciscoCircuitInterfaceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CIRCUIT-INTERFACE-MIB", ciscoCircuitInterfaceMIB=ciscoCircuitInterfaceMIB, cciDescriptionEntry=cciDescriptionEntry, cciDescription=cciDescription, cciDescr=cciDescr, ciscoCircuitInterfaceMIBCompliances=ciscoCircuitInterfaceMIBCompliances, PYSNMP_MODULE_ID=ciscoCircuitInterfaceMIB, ciscoCircuitInterfaceMIBObjects=ciscoCircuitInterfaceMIBObjects, ciscoCircuitInterfaceGroup=ciscoCircuitInterfaceGroup, cciDescriptionTable=cciDescriptionTable, ciscoCircuitInterfaceMIBGroups=ciscoCircuitInterfaceMIBGroups, cciStatus=cciStatus, ciscoCircuitInterfaceMIBCompliance=ciscoCircuitInterfaceMIBCompliance, ciscoCircuitInterfaceMIBConformance=ciscoCircuitInterfaceMIBConformance)
