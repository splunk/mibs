#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SVI-AUTOSTATE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
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
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoSVIAutostateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 376))
ciscoSVIAutostateMIB.setRevisions(('2004-04-06 00:00',))
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setLastUpdated('200404060000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setOrganization('Cisco Systems, Inc.')
ciscoSVIAutostateMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 0))
ciscoSVIAutostateMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1))
ciscoSVIAutostateMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2))
csaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1))
csaInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2))
csaFeatureEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaFeatureEnable.setStatus('current')
csaTrackedVlansLow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansLow.setStatus('current')
csaTrackedVlansHigh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansHigh.setStatus('current')
csaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1), )
if mibBuilder.loadTexts: csaIfConfigTable.setStatus('current')
csaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csaIfConfigEntry.setStatus('current')
csaInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("exclude", 2), ("track", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaInterfaceMode.setStatus('current')
csaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1))
csaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2))
csaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVIAutostateGroup"), ("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVITrackedVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBCompliance = csaMIBCompliance.setStatus('current')
ciscoSVIAutostateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaFeatureEnable"), ("CISCO-SVI-AUTOSTATE-MIB", "csaInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVIAutostateGroup = ciscoSVIAutostateGroup.setStatus('current')
ciscoSVITrackedVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 2)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansLow"), ("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVITrackedVlanGroup = ciscoSVITrackedVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-MIB", ciscoSVIAutostateMIB=ciscoSVIAutostateMIB, csaMIBCompliances=csaMIBCompliances, csaIfConfigTable=csaIfConfigTable, csaTrackedVlansLow=csaTrackedVlansLow, csaInterfaceMode=csaInterfaceMode, ciscoSVITrackedVlanGroup=ciscoSVITrackedVlanGroup, csaMIBCompliance=csaMIBCompliance, ciscoSVIAutostateMIBObjects=ciscoSVIAutostateMIBObjects, csaIfConfigEntry=csaIfConfigEntry, csaTrackedVlansHigh=csaTrackedVlansHigh, csaMIBGroups=csaMIBGroups, csaInterface=csaInterface, csaFeatureEnable=csaFeatureEnable, ciscoSVIAutostateMIBConformance=ciscoSVIAutostateMIBConformance, ciscoSVIAutostateMIBNotifs=ciscoSVIAutostateMIBNotifs, ciscoSVIAutostateGroup=ciscoSVIAutostateGroup, csaGlobal=csaGlobal, PYSNMP_MODULE_ID=ciscoSVIAutostateMIB)
