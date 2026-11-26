#
# PySNMP MIB module DLINKSW-BPDU-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-BPDU-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, NotificationType, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwBpduProtectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 47))
dlinkSwBpduProtectionMIB.setRevisions(('2013-02-19 00:00',))
if mibBuilder.loadTexts: dlinkSwBpduProtectionMIB.setLastUpdated('201302190000Z')
if mibBuilder.loadTexts: dlinkSwBpduProtectionMIB.setOrganization('D-Link Corp.')
dBpduProtectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 0))
dBpduProtectionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 1))
dBpduProtectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 2))
dBpduProtectionGlobalEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dBpduProtectionGlobalEnabled.setStatus('current')
dBpduProtectionNotifyEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dBpduProtectionNotifyEnabled.setStatus('current')
dBpduProtectionIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3), )
if mibBuilder.loadTexts: dBpduProtectionIfTable.setStatus('current')
dBpduProtectionIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dBpduProtectionIfEntry.setStatus('current')
dBpduProtectionIfCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("drop", 2), ("block", 3), ("shutdown", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dBpduProtectionIfCfgMode.setStatus('current')
dBpduProtectionIfAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("underAttack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dBpduProtectionIfAttackStatus.setStatus('current')
dBpduProtectionAttackOccur = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 47, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfCfgMode"))
if mibBuilder.loadTexts: dBpduProtectionAttackOccur.setStatus('current')
dBpduProtectionAttackRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 47, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dBpduProtectionAttackRecover.setStatus('current')
dBpduProtectionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 1))
dBpduProtectionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2))
dBpduProtectionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 1, 1)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionCfgGroup"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionMIBCompliance = dBpduProtectionMIBCompliance.setStatus('current')
dBpduProtectionCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 1)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionGlobalEnabled"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionNotifyEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionCfgGroup = dBpduProtectionCfgGroup.setStatus('current')
dBpduProtectionIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 2)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfCfgMode"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfAttackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionIfGroup = dBpduProtectionIfGroup.setStatus('current')
dBpduProtectionNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 3)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionAttackOccur"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionAttackRecover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionNotifyGroup = dBpduProtectionNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-BPDU-PROTECTION-MIB", dBpduProtectionAttackOccur=dBpduProtectionAttackOccur, dBpduProtectionAttackRecover=dBpduProtectionAttackRecover, dBpduProtectionMIBGroups=dBpduProtectionMIBGroups, dBpduProtectionMIBCompliance=dBpduProtectionMIBCompliance, dBpduProtectionGlobalEnabled=dBpduProtectionGlobalEnabled, dlinkSwBpduProtectionMIB=dlinkSwBpduProtectionMIB, dBpduProtectionObjects=dBpduProtectionObjects, dBpduProtectionConformance=dBpduProtectionConformance, dBpduProtectionIfCfgMode=dBpduProtectionIfCfgMode, dBpduProtectionIfTable=dBpduProtectionIfTable, dBpduProtectionMIBCompliances=dBpduProtectionMIBCompliances, dBpduProtectionCfgGroup=dBpduProtectionCfgGroup, dBpduProtectionNotifyGroup=dBpduProtectionNotifyGroup, PYSNMP_MODULE_ID=dlinkSwBpduProtectionMIB, dBpduProtectionIfAttackStatus=dBpduProtectionIfAttackStatus, dBpduProtectionNotifications=dBpduProtectionNotifications, dBpduProtectionIfEntry=dBpduProtectionIfEntry, dBpduProtectionNotifyEnabled=dBpduProtectionNotifyEnabled, dBpduProtectionIfGroup=dBpduProtectionIfGroup)
