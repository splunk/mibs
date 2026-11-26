#
# PySNMP MIB module CERENT-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CERENT-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
cerentModules, cerentRequirements, cerentGeneric = mibBuilder.importSymbols("CERENT-GLOBAL-REGISTRY", "cerentModules", "cerentRequirements", "cerentGeneric")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
cerentIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3607, 1, 10, 140))
cerentIfExtMIB.setRevisions(('2005-11-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cerentIfExtMIB.setRevisionsDescriptions(('Inital version of the module',))
if mibBuilder.loadTexts: cerentIfExtMIB.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: cerentIfExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cerentIfExtMIB.setContactInfo('         support@Cisco.com\n\n         Postal:  Cisco Systems\n                  1450 N. McDowell Blvd.\n                  Petaluma, CA  94954\n                  USA\n\n            Tel:  +1-877-323-7368')
if mibBuilder.loadTexts: cerentIfExtMIB.setDescription('This module defines objects for managing interfaces.')
cerentIfExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 2, 100))
cerentIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10), )
if mibBuilder.loadTexts: cerentIfExtTable.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtTable.setDescription('This table contains one row per interface.')
cerentIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cerentIfExtEntry.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtEntry.setDescription('Row definition for cerentIfExtTable')
cerentIfExtPreServiceAlarmSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtPreServiceAlarmSuppression.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtPreServiceAlarmSuppression.setDescription("This object can be set through a management interface.\n           When the administrative state of this interface is 'down',\n           the value of this object does not have any impact.\n    \n           When the administrative state of this interface is 'up',\n           if this object has a value of 'false', an alarm on this \n           interface will be reported. If the value of this object is 'true'\n           then all alarms on this interface will be suppressed.\n\n           If the interface has a good signal, the soak timer will be\n           started, if the port is faulted before the soak timer expires,\n           the soak timer will be reset to the provisioned maximum value.\n           If the soak timer expires then the value of this object is \n           automatically set to 'false'.")
cerentIfExtConfiguredSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 20), Integer32().clone(480)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtConfiguredSoakTime.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtConfiguredSoakTime.setDescription('This is the configured maximum value of the soak timer\n           for this interface.')
cerentIfExtCurrentSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 30), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cerentIfExtCurrentSoakTime.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtCurrentSoakTime.setDescription('This is the current value of the soak timer\n           for this interface. The difference between \n           cerntIfExtConfiguredSoakTime and this object gives the\n           time duration for which this interface has had a good signal.')
cerentIfExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90))
cerentIfExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1))
cerentIfExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2))
cerentIfExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1, 1)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtMIBCompliance = cerentIfExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtMIBCompliance.setDescription('Describes the requirements for conformance to the\n        High Capacity Media Independent Group.')
cerentIfExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2, 10)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtPreServiceAlarmSuppression"), ("CERENT-IF-EXT-MIB", "cerentIfExtConfiguredSoakTime"), ("CERENT-IF-EXT-MIB", "cerentIfExtCurrentSoakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtGroup = cerentIfExtGroup.setStatus('current')
if mibBuilder.loadTexts: cerentIfExtGroup.setDescription('The objects for storing all the current alarm thresholds ')
mibBuilder.exportSymbols("CERENT-IF-EXT-MIB", cerentIfExtTable=cerentIfExtTable, cerentIfExtConfiguredSoakTime=cerentIfExtConfiguredSoakTime, cerentIfExtEntry=cerentIfExtEntry, cerentIfExtMIBCompliance=cerentIfExtMIBCompliance, cerentIfExtMIBObjects=cerentIfExtMIBObjects, PYSNMP_MODULE_ID=cerentIfExtMIB, cerentIfExtMIB=cerentIfExtMIB, cerentIfExtCurrentSoakTime=cerentIfExtCurrentSoakTime, cerentIfExtGroup=cerentIfExtGroup, cerentIfExtMIBConformance=cerentIfExtMIBConformance, cerentIfExtMIBCompliances=cerentIfExtMIBCompliances, cerentIfExtMIBGroups=cerentIfExtMIBGroups, cerentIfExtPreServiceAlarmSuppression=cerentIfExtPreServiceAlarmSuppression)
