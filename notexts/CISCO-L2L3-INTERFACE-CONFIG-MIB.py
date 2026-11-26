#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L2L3-INTERFACE-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 151))
ciscoL2L3IfConfigMIB.setRevisions(('2000-05-10 19:00',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setLastUpdated('200005101900Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setOrganization('Cisco Systems, Inc.')
ciscoL2L3IfConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1))
cL2L3IfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1))
class CL2L3InterfaceMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("routed", 1), ("switchport", 2))

cL2L3IfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1), )
if mibBuilder.loadTexts: cL2L3IfTable.setStatus('current')
cL2L3IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cL2L3IfEntry.setStatus('current')
cL2L3IfModeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 1), CL2L3InterfaceMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cL2L3IfModeAdmin.setStatus('current')
cL2L3IfModeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 2), CL2L3InterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cL2L3IfModeOper.setStatus('current')
ciscoL2L3IfConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3))
ciscoL2L3IfConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1))
ciscoL2L3IfConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2))
ciscoL2L3IfConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "ciscoL2L3IfConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBCompliance = ciscoL2L3IfConfigMIBCompliance.setStatus('current')
ciscoL2L3IfConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeAdmin"), ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBGroup = ciscoL2L3IfConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-MIB", ciscoL2L3IfConfigMIBCompliance=ciscoL2L3IfConfigMIBCompliance, ciscoL2L3IfConfigMIBCompliances=ciscoL2L3IfConfigMIBCompliances, cL2L3IfModeOper=cL2L3IfModeOper, ciscoL2L3IfConfigMIBGroup=ciscoL2L3IfConfigMIBGroup, cL2L3IfConfig=cL2L3IfConfig, cL2L3IfEntry=cL2L3IfEntry, ciscoL2L3IfConfigMIBObjects=ciscoL2L3IfConfigMIBObjects, ciscoL2L3IfConfigMIB=ciscoL2L3IfConfigMIB, ciscoL2L3IfConfigMIBConformance=ciscoL2L3IfConfigMIBConformance, CL2L3InterfaceMode=CL2L3InterfaceMode, cL2L3IfModeAdmin=cL2L3IfModeAdmin, ciscoL2L3IfConfigMIBGroups=ciscoL2L3IfConfigMIBGroups, PYSNMP_MODULE_ID=ciscoL2L3IfConfigMIB, cL2L3IfTable=cL2L3IfTable)
