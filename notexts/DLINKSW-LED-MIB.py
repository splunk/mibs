#
# PySNMP MIB module DLINKSW-LED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-LED-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINKSW-LED-MIB", dlinkSwLedMIB=dlinkSwLedMIB, dLedInfoGroup=dLedInfoGroup, dLedMIBConformance=dLedMIBConformance, dLedBoxId=dLedBoxId, dLedInfoEntry=dLedInfoEntry, dLedSysLedStatus=dLedSysLedStatus, dLedIfLedStatus=dLedIfLedStatus, dLedMIBCompliances=dLedMIBCompliances, dLedMIBCompliance=dLedMIBCompliance, dLedMIBNotifications=dLedMIBNotifications, dLedMIBObjects=dLedMIBObjects, dLedMIBGroups=dLedMIBGroups, dLedInfoTable=dLedInfoTable, PYSNMP_MODULE_ID=dlinkSwLedMIB)
