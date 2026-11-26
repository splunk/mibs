#
# PySNMP MIB module DLINKSW-SAFEGUARD-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dCpuProtectMIBObjects, = mibBuilder.importSymbols("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectMIBObjects")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
dlinkSwSafeguardEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1))
dlinkSwSafeguardEngineMIB.setRevisions(('2012-06-27 00:00',))
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setLastUpdated('201206270000Z')
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setOrganization('D-Link Corp.')
dSafeguardEngineMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0))
dSafeguardEngineMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1))
dSafeguardEngineMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2))
dSafeguardEngineState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineState.setStatus('current')
dSafeguardEngineRiseThresh = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(50)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineRiseThresh.setStatus('current')
dSafeguardEngineFallThresh = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(20)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineFallThresh.setStatus('current')
dSafeguardEngineCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("exhausted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dSafeguardEngineCurrentMode.setStatus('current')
dSafeguardEngineNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineNotifEnable.setStatus('current')
dSafeguardChgToExhausted = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if mibBuilder.loadTexts: dSafeguardChgToExhausted.setStatus('current')
dSafeguardChgToNormal = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 2)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if mibBuilder.loadTexts: dSafeguardChgToNormal.setStatus('current')
dSafeguardEngineCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1))
dSafeguardEngineCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineGroup"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngNotifEnableGroup"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineCompliance = dSafeguardEngineCompliance.setStatus('current')
dSafeguardEngineGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2))
dSafeguardEngineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineState"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineRiseThresh"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineFallThresh"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineGroup = dSafeguardEngineGroup.setStatus('current')
dSafeguardEngNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 2)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngNotifEnableGroup = dSafeguardEngNotifEnableGroup.setStatus('current')
dSafeguardEngineNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 3)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToExhausted"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineNotifGroup = dSafeguardEngineNotifGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-SAFEGUARD-ENGINE-MIB", dSafeguardEngineGroups=dSafeguardEngineGroups, dSafeguardEngineFallThresh=dSafeguardEngineFallThresh, dSafeguardEngineMIBObjects=dSafeguardEngineMIBObjects, dSafeguardEngNotifEnableGroup=dSafeguardEngNotifEnableGroup, dSafeguardEngineCurrentMode=dSafeguardEngineCurrentMode, dSafeguardEngineGroup=dSafeguardEngineGroup, dSafeguardEngineNotifEnable=dSafeguardEngineNotifEnable, PYSNMP_MODULE_ID=dlinkSwSafeguardEngineMIB, dSafeguardEngineMIBNotif=dSafeguardEngineMIBNotif, dSafeguardEngineCompliance=dSafeguardEngineCompliance, dSafeguardEngineNotifGroup=dSafeguardEngineNotifGroup, dlinkSwSafeguardEngineMIB=dlinkSwSafeguardEngineMIB, dSafeguardEngineRiseThresh=dSafeguardEngineRiseThresh, dSafeguardEngineMIBConformance=dSafeguardEngineMIBConformance, dSafeguardChgToNormal=dSafeguardChgToNormal, dSafeguardEngineState=dSafeguardEngineState, dSafeguardEngineCompliances=dSafeguardEngineCompliances, dSafeguardChgToExhausted=dSafeguardChgToExhausted)
