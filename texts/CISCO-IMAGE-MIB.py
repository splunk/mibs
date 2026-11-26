#
# PySNMP MIB module CISCO-IMAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMAGE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoImageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 25))
ciscoImageMIB.setRevisions(('1995-08-15 00:00', '1995-01-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImageMIB.setRevisionsDescriptions(('Specify a correct (non-negative) range for an index\n        object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImageMIB.setLastUpdated('9508150000Z')
if mibBuilder.loadTexts: ciscoImageMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImageMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoImageMIB.setDescription('Router image MIB which identify the capabilities\n        and characteristics of the image')
ciscoImageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 1))
ciscoImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1), )
if mibBuilder.loadTexts: ciscoImageTable.setStatus('current')
if mibBuilder.loadTexts: ciscoImageTable.setDescription('A table provides content information describing the\n        executing IOS image.')
ciscoImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1), ).setIndexNames((0, "CISCO-IMAGE-MIB", "ciscoImageIndex"))
if mibBuilder.loadTexts: ciscoImageEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoImageEntry.setDescription('A image characteristic string entry.')
ciscoImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoImageIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoImageIndex.setDescription('A sequence number for each string stored\n        in the IOS image.')
ciscoImageString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageString.setStatus('current')
if mibBuilder.loadTexts: ciscoImageString.setDescription('The string of this entry.')
ciscoImageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2))
ciscoImageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1))
ciscoImageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2))
ciscoImageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCompliance = ciscoImageMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBCompliance.setDescription('The compliance statement for entities which implement\n        the Cisco Image MIB')
ciscoImageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBGroup = ciscoImageMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBGroup.setDescription('A collection of objects providing IOS image characteristics')
mibBuilder.exportSymbols("CISCO-IMAGE-MIB", ciscoImageMIB=ciscoImageMIB, ciscoImageMIBConformance=ciscoImageMIBConformance, ciscoImageIndex=ciscoImageIndex, ciscoImageMIBCompliance=ciscoImageMIBCompliance, ciscoImageTable=ciscoImageTable, ciscoImageMIBGroup=ciscoImageMIBGroup, ciscoImageMIBObjects=ciscoImageMIBObjects, ciscoImageMIBCompliances=ciscoImageMIBCompliances, ciscoImageMIBGroups=ciscoImageMIBGroups, PYSNMP_MODULE_ID=ciscoImageMIB, ciscoImageEntry=ciscoImageEntry, ciscoImageString=ciscoImageString)
