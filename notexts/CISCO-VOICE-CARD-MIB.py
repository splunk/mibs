#
# PySNMP MIB module CISCO-VOICE-CARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-CARD-MIB
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
ciscoVoiceCard = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 300576))
ciscoVoiceCard.setRevisions(('2002-02-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCard.setLastUpdated('200202150000Z')
if mibBuilder.loadTexts: ciscoVoiceCard.setOrganization('Cisco Systems, Inc')
ciscoVoiceCardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 0))
ciscoVoiceCardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1))
cVoiceCardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1), )
if mibBuilder.loadTexts: cVoiceCardTable.setStatus('current')
cVoiceCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CARD-MIB", "cVoiceCardIndex"))
if mibBuilder.loadTexts: cVoiceCardEntry.setStatus('current')
cVoiceCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: cVoiceCardIndex.setStatus('current')
cVoiceCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoiceCardSlotNumber.setStatus('current')
cVoiceCardCodecComplexity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("hc", 2), ("mc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoiceCardCodecComplexity.setStatus('current')
cVoiceCardAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoiceCardAdminStatus.setStatus('current')
ciscoVoiceCardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2))
ciscoVoiceCardMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1))
ciscoVoiceCardMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2))
ciscoVoiceCardMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1, 1)).setObjects(("CISCO-VOICE-CARD-MIB", "ciscoVoiceCardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCardMIBCompliance = ciscoVoiceCardMIBCompliance.setStatus('current')
ciscoVoiceCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2, 1)).setObjects(("CISCO-VOICE-CARD-MIB", "cVoiceCardSlotNumber"), ("CISCO-VOICE-CARD-MIB", "cVoiceCardCodecComplexity"), ("CISCO-VOICE-CARD-MIB", "cVoiceCardAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCardGroup = ciscoVoiceCardGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CARD-MIB", ciscoVoiceCardObjects=ciscoVoiceCardObjects, cVoiceCardCodecComplexity=cVoiceCardCodecComplexity, ciscoVoiceCardNotifications=ciscoVoiceCardNotifications, cVoiceCardEntry=cVoiceCardEntry, cVoiceCardAdminStatus=cVoiceCardAdminStatus, ciscoVoiceCard=ciscoVoiceCard, ciscoVoiceCardGroup=ciscoVoiceCardGroup, cVoiceCardSlotNumber=cVoiceCardSlotNumber, PYSNMP_MODULE_ID=ciscoVoiceCard, ciscoVoiceCardMIBCompliance=ciscoVoiceCardMIBCompliance, ciscoVoiceCardMIBCompliances=ciscoVoiceCardMIBCompliances, cVoiceCardIndex=cVoiceCardIndex, ciscoVoiceCardMIBGroups=ciscoVoiceCardMIBGroups, cVoiceCardTable=cVoiceCardTable, ciscoVoiceCardConformance=ciscoVoiceCardConformance)
