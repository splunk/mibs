#
# PySNMP MIB module CISCO-VOICE-ENABLED-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-ENABLED-LINK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
ciscoVoiceEnabledLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 53))
if mibBuilder.loadTexts: ciscoVoiceEnabledLinkMIB.setLastUpdated('9905070000Z')
if mibBuilder.loadTexts: ciscoVoiceEnabledLinkMIB.setOrganization('Cisco Systems, Inc.')
cvenabledlinkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 1))
cvEnabledLink = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1))
cvEnabledDefaultMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledDefaultMacAddr.setStatus('current')
cvEnabledLinkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2), )
if mibBuilder.loadTexts: cvEnabledLinkTable.setStatus('current')
cvEnabledLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkIndex"))
if mibBuilder.loadTexts: cvEnabledLinkEntry.setStatus('current')
cvEnabledLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483648))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkIndex.setStatus('current')
cvEnabledLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("atm", 1), ("framerelay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkType.setStatus('current')
cvEnabledLinkInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkInterfaceName.setStatus('current')
cvEnabledLinkVpiDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkVpiDlci.setStatus('current')
cvEnabledLinkVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkVci.setStatus('current')
cvEnabledLinkRemoteMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 53, 1, 1, 2, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvEnabledLinkRemoteMacAddr.setStatus('current')
ciscoVoiceEnabledLinkMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 2))
ciscoVoiceEnabledLinkMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 2, 0))
ciscoVoiceEnabledlinkMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 3))
ciscoVoiceEnabledlinkMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 1))
ciscoVoiceEnabledlinkMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2))
ciscoVoiceEnabledlinkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 1, 1)).setObjects(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledMacAddrGroup"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceEnabledlinkMIBCompliance = ciscoVoiceEnabledlinkMIBCompliance.setStatus('current')
cvEnabledMacAddrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2, 1)).setObjects(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledDefaultMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvEnabledMacAddrGroup = cvEnabledMacAddrGroup.setStatus('current')
cvEnabledLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 53, 3, 2, 2)).setObjects(("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkIndex"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkType"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkInterfaceName"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkVpiDlci"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkVci"), ("CISCO-VOICE-ENABLED-LINK-MIB", "cvEnabledLinkRemoteMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvEnabledLinkGroup = cvEnabledLinkGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-ENABLED-LINK-MIB", cvEnabledLinkVci=cvEnabledLinkVci, PYSNMP_MODULE_ID=ciscoVoiceEnabledLinkMIB, cvEnabledLinkTable=cvEnabledLinkTable, cvEnabledDefaultMacAddr=cvEnabledDefaultMacAddr, cvEnabledLinkVpiDlci=cvEnabledLinkVpiDlci, cvEnabledLinkIndex=cvEnabledLinkIndex, cvenabledlinkMIBObjects=cvenabledlinkMIBObjects, ciscoVoiceEnabledlinkMIBConformance=ciscoVoiceEnabledlinkMIBConformance, cvEnabledLinkType=cvEnabledLinkType, ciscoVoiceEnabledLinkMIB=ciscoVoiceEnabledLinkMIB, ciscoVoiceEnabledLinkMIBNotifications=ciscoVoiceEnabledLinkMIBNotifications, ciscoVoiceEnabledlinkMIBCompliances=ciscoVoiceEnabledlinkMIBCompliances, ciscoVoiceEnabledlinkMIBGroups=ciscoVoiceEnabledlinkMIBGroups, ciscoVoiceEnabledlinkMIBCompliance=ciscoVoiceEnabledlinkMIBCompliance, cvEnabledLinkRemoteMacAddr=cvEnabledLinkRemoteMacAddr, cvEnabledMacAddrGroup=cvEnabledMacAddrGroup, cvEnabledLinkGroup=cvEnabledLinkGroup, cvEnabledLinkEntry=cvEnabledLinkEntry, cvEnabledLinkInterfaceName=cvEnabledLinkInterfaceName, cvEnabledLink=cvEnabledLink, ciscoVoiceEnabledLinkMIBNotificationPrefix=ciscoVoiceEnabledLinkMIBNotificationPrefix)
