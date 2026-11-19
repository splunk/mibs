#
# PySNMP MIB module CISCO-DS0-CROSS-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DS0-CROSS-CONNECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoDs0CrossConnectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoDs0CrossConnectMIB.setRevisions(('2003-03-05 00:00',))
if mibBuilder.loadTexts: ciscoDs0CrossConnectMIB.setLastUpdated('200303050000Z')
if mibBuilder.loadTexts: ciscoDs0CrossConnectMIB.setOrganization('Cisco Systems, Inc.')
ciscoDs0CrossConnectMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 0))
ciscoDs0CrossConnectMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
ciscoDs0CrossConnectMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
cDs0CrossConnectConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
cds0CrossConnectConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1), )
if mibBuilder.loadTexts: cds0CrossConnectConfigTable.setStatus('current')
cds0CrossConnectConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt1Ds1"), (0, "CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt1Ds0Group"))
if mibBuilder.loadTexts: cds0CrossConnectConfigEntry.setStatus('current')
cds0Endpt1Ds1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cds0Endpt1Ds1.setStatus('current')
cds0Endpt1Ds0Group = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)))
if mibBuilder.loadTexts: cds0Endpt1Ds0Group.setStatus('current')
cds0Endpt2Ds1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cds0Endpt2Ds1.setStatus('current')
cds0Endpt2Ds0Group = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cds0Endpt2Ds0Group.setStatus('current')
cds0ConnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cds0ConnRowStatus.setStatus('current')
ciscoDs0CrossConnectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoDs0CrossConnectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoDs0CrossConnectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-DS0-CROSS-CONNECT-MIB", "cDs0CrossConnectConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0CrossConnectMIBCompliance = ciscoDs0CrossConnectMIBCompliance.setStatus('current')
cDs0CrossConnectConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt2Ds1"), ("CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt2Ds0Group"), ("CISCO-DS0-CROSS-CONNECT-MIB", "cds0ConnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDs0CrossConnectConfigGroup = cDs0CrossConnectConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0-CROSS-CONNECT-MIB", cds0Endpt2Ds1=cds0Endpt2Ds1, cds0CrossConnectConfigEntry=cds0CrossConnectConfigEntry, ciscoDs0CrossConnectMIB=ciscoDs0CrossConnectMIB, cDs0CrossConnectConfig=cDs0CrossConnectConfig, cds0CrossConnectConfigTable=cds0CrossConnectConfigTable, cds0Endpt1Ds0Group=cds0Endpt1Ds0Group, ciscoDs0CrossConnectMIBCompliance=ciscoDs0CrossConnectMIBCompliance, ciscoDs0CrossConnectMIBObjects=ciscoDs0CrossConnectMIBObjects, cDs0CrossConnectConfigGroup=cDs0CrossConnectConfigGroup, ciscoDs0CrossConnectMIBNotifs=ciscoDs0CrossConnectMIBNotifs, cds0ConnRowStatus=cds0ConnRowStatus, ciscoDs0CrossConnectMIBCompliances=ciscoDs0CrossConnectMIBCompliances, ciscoDs0CrossConnectMIBConformance=ciscoDs0CrossConnectMIBConformance, cds0Endpt1Ds1=cds0Endpt1Ds1, ciscoDs0CrossConnectMIBGroups=ciscoDs0CrossConnectMIBGroups, PYSNMP_MODULE_ID=ciscoDs0CrossConnectMIB, cds0Endpt2Ds0Group=cds0Endpt2Ds0Group)
