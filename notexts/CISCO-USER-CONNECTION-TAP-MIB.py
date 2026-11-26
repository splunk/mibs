#
# PySNMP MIB module CISCO-USER-CONNECTION-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-USER-CONNECTION-TAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2StreamIndex, cTap2MediationContentId = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2StreamIndex", "cTap2MediationContentId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoUserConnectionTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 400))
ciscoUserConnectionTapMIB.setRevisions(('2007-08-09 00:00', '2004-03-11 00:00',))
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setLastUpdated('200708090000Z')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setOrganization('Cisco Systems, Inc.')
cUserConnectionTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1))
cUserConnectionTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2))
cuctTapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1))
cuctTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("acctSessionId", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setStatus('current')
cuctTapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2), )
if mibBuilder.loadTexts: cuctTapStreamTable.setStatus('current')
cuctTapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cuctTapStreamEntry.setStatus('current')
cuctTapStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setStatus('current')
cuctTapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamStatus.setStatus('current')
cUserConnectionTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1))
cUserConnectionTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2))
cUserConnectionTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cUserConnectionTapMIBCompliance = cUserConnectionTapMIBCompliance.setStatus('current')
cuctTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamCapabilities"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamAcctSessID"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cuctTapStreamComplianceGroup = cuctTapStreamComplianceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-USER-CONNECTION-TAP-MIB", cUserConnectionTapMIBGroups=cUserConnectionTapMIBGroups, cuctTapStreamComplianceGroup=cuctTapStreamComplianceGroup, cuctTapStreamTable=cuctTapStreamTable, PYSNMP_MODULE_ID=ciscoUserConnectionTapMIB, cuctTapStreamEntry=cuctTapStreamEntry, cUserConnectionTapMIBObjects=cUserConnectionTapMIBObjects, cuctTapStreamEncodePacket=cuctTapStreamEncodePacket, cUserConnectionTapMIBCompliance=cUserConnectionTapMIBCompliance, cUserConnectionTapMIBCompliances=cUserConnectionTapMIBCompliances, ciscoUserConnectionTapMIB=ciscoUserConnectionTapMIB, cuctTapStreamAcctSessID=cuctTapStreamAcctSessID, cUserConnectionTapMIBConform=cUserConnectionTapMIBConform, cuctTapStreamCapabilities=cuctTapStreamCapabilities, cuctTapStreamStatus=cuctTapStreamStatus)
