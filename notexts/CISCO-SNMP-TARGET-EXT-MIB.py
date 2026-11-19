#
# PySNMP MIB module CISCO-SNMP-TARGET-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-TARGET-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
snmpTargetAddrEntry, snmpTargetAddrName = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry", "snmpTargetAddrName")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TruthValue, StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
ciscoSnmpTargetExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 412))
ciscoSnmpTargetExtMIB.setRevisions(('2008-11-07 00:00', '2007-08-20 00:00', '2004-04-01 00:00',))
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setLastUpdated('200811070000Z')
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoSnmpTargetExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 1))
cExtSnmpTargetAuthAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1))
cExtSnmpTargetAuthInetType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cExtSnmpTargetAuthInetType.setStatus('current')
cExtSnmpTargetAuthInetAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cExtSnmpTargetAuthInetAddr.setStatus('current')
cExtSnmpTargetAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2), )
if mibBuilder.loadTexts: cExtSnmpTargetAddrTable.setStatus('current')
cExtSnmpTargetAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1), )
snmpTargetAddrEntry.registerAugmentions(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrEntry"))
cExtSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: cExtSnmpTargetAddrEntry.setStatus('current')
cExtSnmpTargetAddrIntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpTargetAddrIntIfIndex.setStatus('current')
cExtSnmpTargetVrfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3), )
if mibBuilder.loadTexts: cExtSnmpTargetVrfTable.setStatus('current')
cExtSnmpTargetVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1), ).setIndexNames((0, "SNMP-TARGET-MIB", "snmpTargetAddrName"), (0, "CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfName"))
if mibBuilder.loadTexts: cExtSnmpTargetVrfEntry.setStatus('current')
cExtSnmpTargetVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cExtSnmpTargetVrfName.setStatus('current')
cExtSnmpTargetVrfRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfRoute.setStatus('current')
cExtSnmpTargetVrfFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfFilter.setStatus('current')
cExtSnmpTargetVrfStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfStorage.setStatus('current')
cExtSnmpTargetVrfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfStatus.setStatus('current')
cExtSnmpNotifGblTrapSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpNotifGblTrapSrcIfIndex.setStatus('current')
cExtSnmpNotifGblInformSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpNotifGblInformSrcIfIndex.setStatus('current')
ciscoSnmpTargetExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2))
ciscoSnmpTargetExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1))
ciscoSnmpTargetExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2))
ciscoSnmpTargetExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 1)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBCompliance = ciscoSnmpTargetExtMIBCompliance.setStatus('deprecated')
ciscoSnmpTargetExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 2)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtVrfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBComplianceRev1 = ciscoSnmpTargetExtMIBComplianceRev1.setStatus('deprecated')
ciscoSnmpTargetExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 3)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtVrfMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetNotifSrcIntGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBComplianceRev2 = ciscoSnmpTargetExtMIBComplianceRev2.setStatus('current')
ciscoSnmpTargetAuthFailureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 1)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetType"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetAuthFailureGroup = ciscoSnmpTargetAuthFailureGroup.setStatus('current')
ciscoSnmpTargetExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 2)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrIntIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBGroup = ciscoSnmpTargetExtMIBGroup.setStatus('current')
ciscoSnmpTargetExtVrfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 3)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfRoute"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfFilter"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStorage"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtVrfMIBGroup = ciscoSnmpTargetExtVrfMIBGroup.setStatus('current')
ciscoSnmpTargetNotifSrcIntGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 4)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblTrapSrcIfIndex"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblInformSrcIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetNotifSrcIntGroup = ciscoSnmpTargetNotifSrcIntGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-EXT-MIB", ciscoSnmpTargetExtVrfMIBGroup=ciscoSnmpTargetExtVrfMIBGroup, cExtSnmpTargetAddrEntry=cExtSnmpTargetAddrEntry, ciscoSnmpTargetExtMIBGroup=ciscoSnmpTargetExtMIBGroup, cExtSnmpTargetAddrTable=cExtSnmpTargetAddrTable, cExtSnmpTargetVrfTable=cExtSnmpTargetVrfTable, cExtSnmpTargetVrfName=cExtSnmpTargetVrfName, ciscoSnmpTargetExtMIB=ciscoSnmpTargetExtMIB, cExtSnmpTargetVrfFilter=cExtSnmpTargetVrfFilter, ciscoSnmpTargetExtMIBCompliances=ciscoSnmpTargetExtMIBCompliances, PYSNMP_MODULE_ID=ciscoSnmpTargetExtMIB, cExtSnmpTargetVrfStatus=cExtSnmpTargetVrfStatus, ciscoSnmpTargetExtMIBConformance=ciscoSnmpTargetExtMIBConformance, ciscoSnmpTargetNotifSrcIntGroup=ciscoSnmpTargetNotifSrcIntGroup, ciscoSnmpTargetExtMIBGroups=ciscoSnmpTargetExtMIBGroups, ciscoSnmpTargetExtMIBObjects=ciscoSnmpTargetExtMIBObjects, ciscoSnmpTargetExtMIBComplianceRev1=ciscoSnmpTargetExtMIBComplianceRev1, ciscoSnmpTargetAuthFailureGroup=ciscoSnmpTargetAuthFailureGroup, cExtSnmpTargetVrfRoute=cExtSnmpTargetVrfRoute, cExtSnmpTargetAuthInetType=cExtSnmpTargetAuthInetType, cExtSnmpNotifGblInformSrcIfIndex=cExtSnmpNotifGblInformSrcIfIndex, cExtSnmpTargetAuthInetAddr=cExtSnmpTargetAuthInetAddr, cExtSnmpTargetAddrIntIfIndex=cExtSnmpTargetAddrIntIfIndex, ciscoSnmpTargetExtMIBCompliance=ciscoSnmpTargetExtMIBCompliance, ciscoSnmpTargetExtMIBComplianceRev2=ciscoSnmpTargetExtMIBComplianceRev2, cExtSnmpTargetAuthAddr=cExtSnmpTargetAuthAddr, cExtSnmpTargetVrfStorage=cExtSnmpTargetVrfStorage, cExtSnmpNotifGblTrapSrcIfIndex=cExtSnmpNotifGblTrapSrcIfIndex, cExtSnmpTargetVrfEntry=cExtSnmpTargetVrfEntry)
