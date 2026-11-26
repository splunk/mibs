#
# PySNMP MIB module CISCO-VOICE-FR-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-FR-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-DIAL-CONTROL-MIB", "CvcGUid")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-VOICE-FR-DIAL-CONTROL-MIB", cvfrdcMIBCompliance=cvfrdcMIBCompliance, cvFrCallHistoryGroup=cvFrCallHistoryGroup, cvFrCallHistoryTable=cvFrCallHistoryTable, cvFrCallHistoryConnectionId=cvFrCallHistoryConnectionId, cvFrCallHistoryDlci=cvFrCallHistoryDlci, cvFrCallHistorySessionTarget=cvFrCallHistorySessionTarget, cvFrCallHistoryEntry=cvFrCallHistoryEntry, cvfrdcMIBConformance=cvfrdcMIBConformance, cvFrCallHistoryLowerIfName=cvFrCallHistoryLowerIfName, cvFrCallHistory=cvFrCallHistory, cvfrdcMIBObjects=cvfrdcMIBObjects, cvfrdcMIBGroups=cvfrdcMIBGroups, ciscoVoiceFrDialControlMIB=ciscoVoiceFrDialControlMIB, cvfrdcMIBCompliances=cvfrdcMIBCompliances, PYSNMP_MODULE_ID=ciscoVoiceFrDialControlMIB)
