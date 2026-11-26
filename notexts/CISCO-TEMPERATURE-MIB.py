#
# PySNMP MIB module CISCO-TEMPERATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TEMPERATURE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTempMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 870))
ciscoTempMIB.setRevisions(('2020-05-28 00:00',))
if mibBuilder.loadTexts: ciscoTempMIB.setLastUpdated('202005280000Z')
if mibBuilder.loadTexts: ciscoTempMIB.setOrganization('Cisco Systems, Inc.')
ciscoTempMIBInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 1))
ciscoTempTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1), )
if mibBuilder.loadTexts: ciscoTempTable.setStatus('current')
ciscoTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1), ).setIndexNames((0, "CISCO-TEMPERATURE-MIB", "ciscoTempIndex"))
if mibBuilder.loadTexts: ciscoTempEntry.setStatus('current')
ciscoTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoTempIndex.setStatus('current')
ciscoTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 2), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempValue.setStatus('current')
ciscoTempHyst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 3), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempHyst.setStatus('current')
ciscoTempOs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 4), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempOs.setStatus('current')
ciscoTempMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2))
ciscoTempMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1))
ciscoTempMIBConformGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2))
ciscoTempMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1, 1)).setObjects(("CISCO-TEMPERATURE-MIB", "ciscoTempMIBGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTempMIBCompliance = ciscoTempMIBCompliance.setStatus('current')
ciscoTempMIBGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2, 1)).setObjects(("CISCO-TEMPERATURE-MIB", "ciscoTempValue"), ("CISCO-TEMPERATURE-MIB", "ciscoTempHyst"), ("CISCO-TEMPERATURE-MIB", "ciscoTempOs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTempMIBGlobalGroup = ciscoTempMIBGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-TEMPERATURE-MIB", ciscoTempTable=ciscoTempTable, ciscoTempMIBCompliances=ciscoTempMIBCompliances, ciscoTempHyst=ciscoTempHyst, ciscoTempIndex=ciscoTempIndex, ciscoTempMIBConformGroups=ciscoTempMIBConformGroups, ciscoTempOs=ciscoTempOs, ciscoTempMIB=ciscoTempMIB, ciscoTempMIBCompliance=ciscoTempMIBCompliance, ciscoTempEntry=ciscoTempEntry, ciscoTempMIBInformation=ciscoTempMIBInformation, ciscoTempMIBConform=ciscoTempMIBConform, ciscoTempValue=ciscoTempValue, PYSNMP_MODULE_ID=ciscoTempMIB, ciscoTempMIBGlobalGroup=ciscoTempMIBGlobalGroup)
