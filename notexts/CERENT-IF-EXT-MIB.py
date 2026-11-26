#
# PySNMP MIB module CERENT-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CERENT-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cerentRequirements, cerentGeneric, cerentModules = mibBuilder.importSymbols("CERENT-GLOBAL-REGISTRY", "cerentRequirements", "cerentGeneric", "cerentModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cerentIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3607, 1, 10, 140))
cerentIfExtMIB.setRevisions(('2005-11-14 00:00',))
if mibBuilder.loadTexts: cerentIfExtMIB.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: cerentIfExtMIB.setOrganization('Cisco Systems, Inc.')
cerentIfExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 2, 100))
cerentIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10), )
if mibBuilder.loadTexts: cerentIfExtTable.setStatus('current')
cerentIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cerentIfExtEntry.setStatus('current')
cerentIfExtPreServiceAlarmSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtPreServiceAlarmSuppression.setStatus('current')
cerentIfExtConfiguredSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 20), Integer32().clone(480)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtConfiguredSoakTime.setStatus('current')
cerentIfExtCurrentSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 30), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cerentIfExtCurrentSoakTime.setStatus('current')
cerentIfExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90))
cerentIfExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1))
cerentIfExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2))
cerentIfExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1, 1)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtMIBCompliance = cerentIfExtMIBCompliance.setStatus('current')
cerentIfExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2, 10)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtPreServiceAlarmSuppression"), ("CERENT-IF-EXT-MIB", "cerentIfExtConfiguredSoakTime"), ("CERENT-IF-EXT-MIB", "cerentIfExtCurrentSoakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtGroup = cerentIfExtGroup.setStatus('current')
mibBuilder.exportSymbols("CERENT-IF-EXT-MIB", cerentIfExtMIBConformance=cerentIfExtMIBConformance, cerentIfExtCurrentSoakTime=cerentIfExtCurrentSoakTime, PYSNMP_MODULE_ID=cerentIfExtMIB, cerentIfExtMIBObjects=cerentIfExtMIBObjects, cerentIfExtTable=cerentIfExtTable, cerentIfExtMIB=cerentIfExtMIB, cerentIfExtPreServiceAlarmSuppression=cerentIfExtPreServiceAlarmSuppression, cerentIfExtMIBCompliance=cerentIfExtMIBCompliance, cerentIfExtGroup=cerentIfExtGroup, cerentIfExtMIBCompliances=cerentIfExtMIBCompliances, cerentIfExtConfiguredSoakTime=cerentIfExtConfiguredSoakTime, cerentIfExtEntry=cerentIfExtEntry, cerentIfExtMIBGroups=cerentIfExtMIBGroups)
