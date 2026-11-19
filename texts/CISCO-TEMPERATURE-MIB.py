#
# PySNMP MIB module CISCO-TEMPERATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TEMPERATURE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTempMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 870))
ciscoTempMIB.setRevisions(('2020-05-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTempMIB.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoTempMIB.setLastUpdated('202005280000Z')
if mibBuilder.loadTexts: ciscoTempMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTempMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTempMIB.setDescription('This MIB is intended for collecting\n                telementry data such as temperature details.')
ciscoTempMIBInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 1))
ciscoTempTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1), )
if mibBuilder.loadTexts: ciscoTempTable.setStatus('current')
if mibBuilder.loadTexts: ciscoTempTable.setDescription('Entry in the information table,\n                that gives temperature value.')
ciscoTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1), ).setIndexNames((0, "CISCO-TEMPERATURE-MIB", "ciscoTempIndex"))
if mibBuilder.loadTexts: ciscoTempEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoTempEntry.setDescription('Each entry shows details realted to temperature.')
ciscoTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoTempIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoTempIndex.setDescription('Unique index for the temperature being instrumented.\n                This index is for SNMP purposes only, and has no\n                intrinsic meaning.')
ciscoTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 2), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempValue.setStatus('current')
if mibBuilder.loadTexts: ciscoTempValue.setDescription('The current temperature measurement value of AP.')
ciscoTempHyst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 3), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempHyst.setStatus('current')
if mibBuilder.loadTexts: ciscoTempHyst.setDescription('The current T-Hyst measurement value of AP.')
ciscoTempOs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 4), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempOs.setStatus('current')
if mibBuilder.loadTexts: ciscoTempOs.setDescription('The current T-OS measurement value of AP.')
ciscoTempMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2))
ciscoTempMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1))
ciscoTempMIBConformGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2))
ciscoTempMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1, 1)).setObjects(("CISCO-TEMPERATURE-MIB", "ciscoTempMIBGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTempMIBCompliance = ciscoTempMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoTempMIBCompliance.setDescription('The compliance statement for the SNMP entities that\n                 implement the ciscoTempMIB module.')
ciscoTempMIBGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2, 1)).setObjects(("CISCO-TEMPERATURE-MIB", "ciscoTempValue"), ("CISCO-TEMPERATURE-MIB", "ciscoTempHyst"), ("CISCO-TEMPERATURE-MIB", "ciscoTempOs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTempMIBGlobalGroup = ciscoTempMIBGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoTempMIBGlobalGroup.setDescription('This collection of objects provide information about\n                 the temperature details of Access Point.')
mibBuilder.exportSymbols("CISCO-TEMPERATURE-MIB", ciscoTempTable=ciscoTempTable, ciscoTempMIBCompliance=ciscoTempMIBCompliance, ciscoTempIndex=ciscoTempIndex, ciscoTempValue=ciscoTempValue, ciscoTempHyst=ciscoTempHyst, ciscoTempMIBConform=ciscoTempMIBConform, ciscoTempMIBGlobalGroup=ciscoTempMIBGlobalGroup, ciscoTempMIBInformation=ciscoTempMIBInformation, PYSNMP_MODULE_ID=ciscoTempMIB, ciscoTempMIBCompliances=ciscoTempMIBCompliances, ciscoTempOs=ciscoTempOs, ciscoTempEntry=ciscoTempEntry, ciscoTempMIBConformGroups=ciscoTempMIBConformGroups, ciscoTempMIB=ciscoTempMIB)
