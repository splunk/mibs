#
# PySNMP MIB module CISCO-IF-LINK-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IF-LINK-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoLocationSpecifier, = mibBuilder.importSymbols("CISCO-TC", "CiscoLocationSpecifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoIfLinkConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 175))
ciscoIfLinkConfigMIB.setRevisions(('2001-10-05 00:00', '2000-09-14 00:00',))
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setLastUpdated('200110050000Z')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setOrganization('Cisco Systems, Inc.')
cilConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1))
cilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1))
cilConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1), )
if mibBuilder.loadTexts: cilConfTable.setStatus('current')
cilConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IF-LINK-CONFIG-MIB", "cilSourceInterface"))
if mibBuilder.loadTexts: cilConfEntry.setStatus('current')
cilSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cilSourceInterface.setStatus('current')
cilTargetModuleInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 2), CiscoLocationSpecifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleInterface.setStatus('current')
cilRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilRowStatus.setStatus('current')
cilTargetModuleFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("dsx1D4", 2), ("dsx1ESF", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleFramingType.setStatus('current')
cilConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3))
cilConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1))
cilConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2))
cilConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBCompliance = cilConfigMIBCompliance.setStatus('deprecated')
cilConfigMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBComplianceRev1 = cilConfigMIBComplianceRev1.setStatus('current')
cilConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroup = cilConfMIBGroup.setStatus('deprecated')
cilConfMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"), ("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleFramingType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroupRev1 = cilConfMIBGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-LINK-CONFIG-MIB", cilConfigMIBObjects=cilConfigMIBObjects, cilConfigMIBGroups=cilConfigMIBGroups, cilConfigMIBCompliance=cilConfigMIBCompliance, cilRowStatus=cilRowStatus, cilConfigMIBCompliances=cilConfigMIBCompliances, ciscoIfLinkConfigMIB=ciscoIfLinkConfigMIB, cilConfEntry=cilConfEntry, cilConfTable=cilConfTable, cilConfMIBGroup=cilConfMIBGroup, cilConfigMIBComplianceRev1=cilConfigMIBComplianceRev1, cilTargetModuleInterface=cilTargetModuleInterface, PYSNMP_MODULE_ID=ciscoIfLinkConfigMIB, cilConfig=cilConfig, cilTargetModuleFramingType=cilTargetModuleFramingType, cilSourceInterface=cilSourceInterface, cilConfMIBGroupRev1=cilConfMIBGroupRev1, cilConfigMIBConformance=cilConfigMIBConformance)
