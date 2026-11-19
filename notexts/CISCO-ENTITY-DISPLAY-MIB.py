#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DISPLAY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-MIB", ceDisplayState=ceDisplayState, ceDisplayMIBCompliance=ceDisplayMIBCompliance, ceDisplayBeaconTable=ceDisplayBeaconTable, ceDisplayLEDGroup=ceDisplayLEDGroup, ceDisplayName=ceDisplayName, CDisplayType=CDisplayType, ceDisplayText=ceDisplayText, ceDisplayEntry=ceDisplayEntry, ceDisplayMIBConformance=ceDisplayMIBConformance, ceDisplayIndex=ceDisplayIndex, ceDisplayMIBGroups=ceDisplayMIBGroups, ceDisplayTable=ceDisplayTable, ceDisplayType=ceDisplayType, ciscoEntityDisplayMIB=ciscoEntityDisplayMIB, ceDisplayBeaconGroup=ceDisplayBeaconGroup, ceDisplayAlphaNumericGroup=ceDisplayAlphaNumericGroup, ceDisplayMIBCompliances=ceDisplayMIBCompliances, CDisplayState=CDisplayState, ceDisplayGroup=ceDisplayGroup, ceDisplayMIBCompliance2=ceDisplayMIBCompliance2, PYSNMP_MODULE_ID=ciscoEntityDisplayMIB, ceDisplayBeaconEntry=ceDisplayBeaconEntry, ciscoEntityDisplayMIBObjects=ciscoEntityDisplayMIBObjects, ceDisplayColor=ceDisplayColor, CDisplayColor=CDisplayColor, ceDisplayBeaconEnabled=ceDisplayBeaconEnabled)
