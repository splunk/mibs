#
# PySNMP MIB module CISCO-MGX82XX-CARD-FEATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX82XX-CARD-FEATURE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxCardFeatureMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 74))
ciscoMgx82xxCardFeatureMIB.setRevisions(('2003-05-05 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setLastUpdated('200305050000Z')
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setOrganization('Cisco Systems, Inc.')
ascFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 5))
pxmFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 15))
coreCardCommands = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 20))
vsiControllersAllowed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiControllersAllowed.setStatus('current')
apsCardAttributes = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsCardAttributes.setStatus('current')
trkCACEnable = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkCACEnable.setStatus('current')
pxmCardCacMode = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pcrBasedCac", 1), ("scrBasedCac", 2))).clone('pcrBasedCac')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmCardCacMode.setStatus('current')
redundancyAllowed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redNotAllowed", 1), ("redAllowed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyAllowed.setStatus('current')
switchCoreCard = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 20, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("doswitchcc", 2), ("instswitchcc", 3), ("fallbackswitchcc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: switchCoreCard.setStatus('current')
cmCardFeatureMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2))
cmCardFeatureMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1))
cmCardFeatureMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2))
cmCardFeatureCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2, 1)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmPxmCardFeatureGroup"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmAscCardFeatureGroup"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmCoreCardFeatureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmCardFeatureCompliance = cmCardFeatureCompliance.setStatus('current')
cmPxmCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 1)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "vsiControllersAllowed"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "apsCardAttributes"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "trkCACEnable"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "pxmCardCacMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPxmCardFeatureGroup = cmPxmCardFeatureGroup.setStatus('current')
cmAscCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 2)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "redundancyAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAscCardFeatureGroup = cmAscCardFeatureGroup.setStatus('current')
cmCoreCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 3)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "switchCoreCard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmCoreCardFeatureGroup = cmCoreCardFeatureGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-CARD-FEATURE-MIB", redundancyAllowed=redundancyAllowed, pxmCardCacMode=pxmCardCacMode, cmAscCardFeatureGroup=cmAscCardFeatureGroup, cmCoreCardFeatureGroup=cmCoreCardFeatureGroup, ascFeatures=ascFeatures, cmCardFeatureCompliance=cmCardFeatureCompliance, cmPxmCardFeatureGroup=cmPxmCardFeatureGroup, cmCardFeatureMIBConformance=cmCardFeatureMIBConformance, cmCardFeatureMIBGroups=cmCardFeatureMIBGroups, ciscoMgx82xxCardFeatureMIB=ciscoMgx82xxCardFeatureMIB, coreCardCommands=coreCardCommands, pxmFeatures=pxmFeatures, apsCardAttributes=apsCardAttributes, PYSNMP_MODULE_ID=ciscoMgx82xxCardFeatureMIB, switchCoreCard=switchCoreCard, vsiControllersAllowed=vsiControllersAllowed, cmCardFeatureMIBCompliances=cmCardFeatureMIBCompliances, trkCACEnable=trkCACEnable)
