#
# PySNMP MIB module CISCO-VOICE-FR-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-FR-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-DIAL-CONTROL-MIB", "CvcGUid")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceFrDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 36))
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setLastUpdated('9804140000Z')
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvfrdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1))
cvFrCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1))
cvFrCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1), )
if mibBuilder.loadTexts: cvFrCallHistoryTable.setStatus('current')
cvFrCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvFrCallHistoryEntry.setStatus('current')
cvFrCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryConnectionId.setStatus('current')
cvFrCallHistoryDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryDlci.setStatus('current')
cvFrCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryLowerIfName.setStatus('current')
cvFrCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistorySessionTarget.setStatus('current')
cvfrdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3))
cvfrdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1))
cvfrdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2))
cvfrdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvfrdcMIBCompliance = cvfrdcMIBCompliance.setStatus('current')
cvFrCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryConnectionId"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryDlci"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryLowerIfName"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvFrCallHistoryGroup = cvFrCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-FR-DIAL-CONTROL-MIB", cvFrCallHistoryDlci=cvFrCallHistoryDlci, cvFrCallHistorySessionTarget=cvFrCallHistorySessionTarget, PYSNMP_MODULE_ID=ciscoVoiceFrDialControlMIB, cvFrCallHistoryTable=cvFrCallHistoryTable, cvFrCallHistoryGroup=cvFrCallHistoryGroup, cvfrdcMIBObjects=cvfrdcMIBObjects, cvFrCallHistoryConnectionId=cvFrCallHistoryConnectionId, cvfrdcMIBCompliances=cvfrdcMIBCompliances, ciscoVoiceFrDialControlMIB=ciscoVoiceFrDialControlMIB, cvFrCallHistoryEntry=cvFrCallHistoryEntry, cvFrCallHistory=cvFrCallHistory, cvfrdcMIBConformance=cvfrdcMIBConformance, cvFrCallHistoryLowerIfName=cvFrCallHistoryLowerIfName, cvfrdcMIBCompliance=cvfrdcMIBCompliance, cvfrdcMIBGroups=cvfrdcMIBGroups)
