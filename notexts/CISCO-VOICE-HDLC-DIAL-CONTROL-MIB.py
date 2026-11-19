#
# PySNMP MIB module CISCO-VOICE-HDLC-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-HDLC-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-DIAL-CONTROL-MIB", "CvcGUid")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceHdlcDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 37))
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setLastUpdated('9804140000Z')
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvhdlcdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1))
cvHdlcCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1))
cvHdlcCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1), )
if mibBuilder.loadTexts: cvHdlcCallHistoryTable.setStatus('current')
cvHdlcCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvHdlcCallHistoryEntry.setStatus('current')
cvHdlcCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryConnectionId.setStatus('current')
cvHdlcCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryLowerIfName.setStatus('current')
cvHdlcCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistorySessionTarget.setStatus('current')
cvhdlcdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3))
cvhdlcdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1))
cvhdlcdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2))
cvhdlcdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvhdlcdcMIBCompliance = cvhdlcdcMIBCompliance.setStatus('current')
cvHdlcCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryConnectionId"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryLowerIfName"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvHdlcCallHistoryGroup = cvHdlcCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", cvHdlcCallHistoryGroup=cvHdlcCallHistoryGroup, cvHdlcCallHistoryTable=cvHdlcCallHistoryTable, cvhdlcdcMIBObjects=cvhdlcdcMIBObjects, PYSNMP_MODULE_ID=ciscoVoiceHdlcDialControlMIB, cvHdlcCallHistorySessionTarget=cvHdlcCallHistorySessionTarget, cvhdlcdcMIBCompliance=cvhdlcdcMIBCompliance, ciscoVoiceHdlcDialControlMIB=ciscoVoiceHdlcDialControlMIB, cvHdlcCallHistoryEntry=cvHdlcCallHistoryEntry, cvhdlcdcMIBGroups=cvhdlcdcMIBGroups, cvHdlcCallHistoryConnectionId=cvHdlcCallHistoryConnectionId, cvHdlcCallHistoryLowerIfName=cvHdlcCallHistoryLowerIfName, cvhdlcdcMIBConformance=cvhdlcdcMIBConformance, cvHdlcCallHistory=cvHdlcCallHistory, cvhdlcdcMIBCompliances=cvhdlcdcMIBCompliances)
