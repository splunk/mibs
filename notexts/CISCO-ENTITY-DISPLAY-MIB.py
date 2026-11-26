#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DISPLAY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoEntityDisplayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 344))
ciscoEntityDisplayMIB.setRevisions(('2009-10-05 00:00', '2003-03-20 00:00',))
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setLastUpdated('200910050000Z')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setOrganization('Cisco Systems, Inc.')
class CDisplayType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("led", 1), ("alphanumeric", 2))

class CDisplayColor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("white", 2), ("red", 3), ("green", 4), ("yellow", 5), ("amber", 6), ("blue", 7), ("greenAndAmber", 8))

class CDisplayState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("on", 3), ("blinking", 4))

ciscoEntityDisplayMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 1))
ceDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1), )
if mibBuilder.loadTexts: ceDisplayTable.setStatus('current')
ceDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayEntry.setStatus('current')
ceDisplayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: ceDisplayIndex.setStatus('current')
ceDisplayType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 2), CDisplayType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayType.setStatus('current')
ceDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayName.setStatus('current')
ceDisplayState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 4), CDisplayState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayState.setStatus('current')
ceDisplayColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 5), CDisplayColor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayColor.setStatus('current')
ceDisplayText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayText.setStatus('current')
ceDisplayBeaconTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2), )
if mibBuilder.loadTexts: ceDisplayBeaconTable.setStatus('current')
ceDisplayBeaconEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayBeaconEntry.setStatus('current')
ceDisplayBeaconEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceDisplayBeaconEnabled.setStatus('current')
ceDisplayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2))
ceDisplayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1))
ceDisplayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2))
ceDisplayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance = ceDisplayMIBCompliance.setStatus('deprecated')
ceDisplayMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance2 = ceDisplayMIBCompliance2.setStatus('current')
ceDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayType"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayName"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayGroup = ceDisplayGroup.setStatus('current')
ceDisplayLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayLEDGroup = ceDisplayLEDGroup.setStatus('current')
ceDisplayAlphaNumericGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 3)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayAlphaNumericGroup = ceDisplayAlphaNumericGroup.setStatus('current')
ceDisplayBeaconGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 4)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayBeaconGroup = ceDisplayBeaconGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-MIB", ceDisplayMIBConformance=ceDisplayMIBConformance, ceDisplayTable=ceDisplayTable, ceDisplayMIBGroups=ceDisplayMIBGroups, ceDisplayMIBCompliances=ceDisplayMIBCompliances, PYSNMP_MODULE_ID=ciscoEntityDisplayMIB, CDisplayType=CDisplayType, ceDisplayBeaconEntry=ceDisplayBeaconEntry, ceDisplayState=ceDisplayState, ceDisplayName=ceDisplayName, ceDisplayBeaconTable=ceDisplayBeaconTable, CDisplayState=CDisplayState, ceDisplayLEDGroup=ceDisplayLEDGroup, ceDisplayEntry=ceDisplayEntry, ceDisplayMIBCompliance=ceDisplayMIBCompliance, CDisplayColor=CDisplayColor, ceDisplayAlphaNumericGroup=ceDisplayAlphaNumericGroup, ceDisplayColor=ceDisplayColor, ceDisplayText=ceDisplayText, ceDisplayIndex=ceDisplayIndex, ceDisplayBeaconGroup=ceDisplayBeaconGroup, ciscoEntityDisplayMIBObjects=ciscoEntityDisplayMIBObjects, ceDisplayBeaconEnabled=ceDisplayBeaconEnabled, ciscoEntityDisplayMIB=ciscoEntityDisplayMIB, ceDisplayGroup=ceDisplayGroup, ceDisplayMIBCompliance2=ceDisplayMIBCompliance2, ceDisplayType=ceDisplayType)
