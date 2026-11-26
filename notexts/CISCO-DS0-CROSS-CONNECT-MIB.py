#
# PySNMP MIB module CISCO-DS0-CROSS-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DS0-CROSS-CONNECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-DS0-CROSS-CONNECT-MIB", cds0Endpt1Ds0Group=cds0Endpt1Ds0Group, cds0ConnRowStatus=cds0ConnRowStatus, ciscoDs0CrossConnectMIBCompliances=ciscoDs0CrossConnectMIBCompliances, ciscoDs0CrossConnectMIBObjects=ciscoDs0CrossConnectMIBObjects, cds0Endpt2Ds1=cds0Endpt2Ds1, ciscoDs0CrossConnectMIBGroups=ciscoDs0CrossConnectMIBGroups, cds0Endpt2Ds0Group=cds0Endpt2Ds0Group, ciscoDs0CrossConnectMIBNotifs=ciscoDs0CrossConnectMIBNotifs, ciscoDs0CrossConnectMIBCompliance=ciscoDs0CrossConnectMIBCompliance, cDs0CrossConnectConfigGroup=cDs0CrossConnectConfigGroup, cds0CrossConnectConfigTable=cds0CrossConnectConfigTable, PYSNMP_MODULE_ID=ciscoDs0CrossConnectMIB, cDs0CrossConnectConfig=cDs0CrossConnectConfig, cds0CrossConnectConfigEntry=cds0CrossConnectConfigEntry, cds0Endpt1Ds1=cds0Endpt1Ds1, ciscoDs0CrossConnectMIB=ciscoDs0CrossConnectMIB, ciscoDs0CrossConnectMIBConformance=ciscoDs0CrossConnectMIBConformance)
