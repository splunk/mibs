#
# PySNMP MIB module CISCO-IMAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMAGE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 25))
ciscoImageMIB.setRevisions(('1995-08-15 00:00', '1995-01-16 00:00',))
if mibBuilder.loadTexts: ciscoImageMIB.setLastUpdated('9508150000Z')
if mibBuilder.loadTexts: ciscoImageMIB.setOrganization('Cisco Systems, Inc.')
ciscoImageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 1))
ciscoImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1), )
if mibBuilder.loadTexts: ciscoImageTable.setStatus('current')
ciscoImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1), ).setIndexNames((0, "CISCO-IMAGE-MIB", "ciscoImageIndex"))
if mibBuilder.loadTexts: ciscoImageEntry.setStatus('current')
ciscoImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoImageIndex.setStatus('current')
ciscoImageString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageString.setStatus('current')
ciscoImageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2))
ciscoImageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1))
ciscoImageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2))
ciscoImageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCompliance = ciscoImageMIBCompliance.setStatus('current')
ciscoImageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBGroup = ciscoImageMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-MIB", ciscoImageString=ciscoImageString, ciscoImageTable=ciscoImageTable, ciscoImageMIBConformance=ciscoImageMIBConformance, ciscoImageEntry=ciscoImageEntry, ciscoImageIndex=ciscoImageIndex, ciscoImageMIBCompliance=ciscoImageMIBCompliance, ciscoImageMIBGroup=ciscoImageMIBGroup, PYSNMP_MODULE_ID=ciscoImageMIB, ciscoImageMIBObjects=ciscoImageMIBObjects, ciscoImageMIB=ciscoImageMIB, ciscoImageMIBCompliances=ciscoImageMIBCompliances, ciscoImageMIBGroups=ciscoImageMIBGroups)
