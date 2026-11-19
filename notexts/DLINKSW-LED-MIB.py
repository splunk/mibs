#
# PySNMP MIB module DLINKSW-LED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-LED-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, ModuleIdentity, Gauge32, Unsigned32, Bits, iso, ObjectIdentity, Integer32, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Gauge32", "Unsigned32", "Bits", "iso", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwLedMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 163))
dlinkSwLedMIB.setRevisions(('2013-09-13 00:00', '2013-09-06 00:00',))
if mibBuilder.loadTexts: dlinkSwLedMIB.setLastUpdated('201309130000Z')
if mibBuilder.loadTexts: dlinkSwLedMIB.setOrganization('D-Link Corp.')
dLedMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 0))
dLedMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 1))
dLedMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 2))
dLedInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1), )
if mibBuilder.loadTexts: dLedInfoTable.setStatus('current')
dLedInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1), ).setIndexNames((0, "DLINKSW-LED-MIB", "dLedBoxId"))
if mibBuilder.loadTexts: dLedInfoEntry.setStatus('current')
dLedBoxId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: dLedBoxId.setStatus('current')
dLedSysLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dLedSysLedStatus.setStatus('current')
dLedIfLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dLedIfLedStatus.setStatus('current')
dLedMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 1))
dLedMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 2))
dLedMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 1, 1)).setObjects(("DLINKSW-LED-MIB", "dLedInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLedMIBCompliance = dLedMIBCompliance.setStatus('current')
dLedInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 2, 1)).setObjects(("DLINKSW-LED-MIB", "dLedSysLedStatus"), ("DLINKSW-LED-MIB", "dLedIfLedStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLedInfoGroup = dLedInfoGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-LED-MIB", dLedInfoEntry=dLedInfoEntry, dLedSysLedStatus=dLedSysLedStatus, dLedMIBCompliances=dLedMIBCompliances, dLedInfoTable=dLedInfoTable, PYSNMP_MODULE_ID=dlinkSwLedMIB, dlinkSwLedMIB=dlinkSwLedMIB, dLedMIBNotifications=dLedMIBNotifications, dLedMIBGroups=dLedMIBGroups, dLedInfoGroup=dLedInfoGroup, dLedMIBCompliance=dLedMIBCompliance, dLedMIBConformance=dLedMIBConformance, dLedBoxId=dLedBoxId, dLedMIBObjects=dLedMIBObjects, dLedIfLedStatus=dLedIfLedStatus)
