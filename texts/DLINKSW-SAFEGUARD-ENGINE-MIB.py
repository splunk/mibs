#
# PySNMP MIB module DLINKSW-SAFEGUARD-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dCpuProtectMIBObjects, = mibBuilder.importSymbols("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectMIBObjects")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
dlinkSwSafeguardEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1))
dlinkSwSafeguardEngineMIB.setRevisions(('2012-06-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setLastUpdated('201206270000Z')
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setContactInfo('        D-Link Corporation\n\n                 Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                         Taipei City 114, Taiwan, R.O.C\n                 Tel:     +886-2-66000123\n                 E-mail: tsd@dlink.com.tw\n                ')
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setDescription('The MIB module for managing Safeguard engine.')
dSafeguardEngineMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0))
dSafeguardEngineMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1))
dSafeguardEngineMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2))
dSafeguardEngineState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineState.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineState.setDescription('This object is used to configure and show the state of Safeguard Engine.')
dSafeguardEngineRiseThresh = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(50)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineRiseThresh.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineRiseThresh.setDescription('This object is used to configure and show the rising threshold \n\t\t\t\tof Safeguard Engine.')
dSafeguardEngineFallThresh = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(20)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineFallThresh.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineFallThresh.setDescription('This object is used to configure and show the falling \n\t\t\t\t threshold of Safeguard Engine.')
dSafeguardEngineCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("exhausted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dSafeguardEngineCurrentMode.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineCurrentMode.setDescription('This object show the current mode of Safeguard Engine.')
dSafeguardEngineNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineNotifEnable.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineNotifEnable.setDescription('This object specifies whether the system sends notifications to the NMS.')
dSafeguardChgToExhausted = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if mibBuilder.loadTexts: dSafeguardChgToExhausted.setStatus('current')
if mibBuilder.loadTexts: dSafeguardChgToExhausted.setDescription('This trap indicates System change operation mode from normal to exhausted.')
dSafeguardChgToNormal = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 2)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if mibBuilder.loadTexts: dSafeguardChgToNormal.setStatus('current')
if mibBuilder.loadTexts: dSafeguardChgToNormal.setDescription('This trap indicates System change operation mode from exhausted to normal.')
dSafeguardEngineCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1))
dSafeguardEngineCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineGroup"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngNotifEnableGroup"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineCompliance = dSafeguardEngineCompliance.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineCompliance.setDescription('The compliance statement for entities which implement the \n\t\t        DLINKSW-SAFEGUARD-ENGINE-MIB.')
dSafeguardEngineGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2))
dSafeguardEngineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineState"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineRiseThresh"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineFallThresh"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineGroup = dSafeguardEngineGroup.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineGroup.setDescription('A collection of objects providing the configuration or inforamtion about Safeguard Engine.')
dSafeguardEngNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 2)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngNotifEnableGroup = dSafeguardEngNotifEnableGroup.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngNotifEnableGroup.setDescription('A collection of object(s) that provides control over\n                Safeguard Engine related notification(s).')
dSafeguardEngineNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 3)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToExhausted"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineNotifGroup = dSafeguardEngineNotifGroup.setStatus('current')
if mibBuilder.loadTexts: dSafeguardEngineNotifGroup.setDescription('A collection of notifications providing information \n                about the System mode change of Safeguard Engine.')
mibBuilder.exportSymbols("DLINKSW-SAFEGUARD-ENGINE-MIB", dlinkSwSafeguardEngineMIB=dlinkSwSafeguardEngineMIB, dSafeguardEngineCompliances=dSafeguardEngineCompliances, PYSNMP_MODULE_ID=dlinkSwSafeguardEngineMIB, dSafeguardEngineFallThresh=dSafeguardEngineFallThresh, dSafeguardEngNotifEnableGroup=dSafeguardEngNotifEnableGroup, dSafeguardEngineMIBNotif=dSafeguardEngineMIBNotif, dSafeguardEngineNotifGroup=dSafeguardEngineNotifGroup, dSafeguardChgToExhausted=dSafeguardChgToExhausted, dSafeguardEngineRiseThresh=dSafeguardEngineRiseThresh, dSafeguardEngineGroup=dSafeguardEngineGroup, dSafeguardEngineMIBConformance=dSafeguardEngineMIBConformance, dSafeguardEngineGroups=dSafeguardEngineGroups, dSafeguardEngineMIBObjects=dSafeguardEngineMIBObjects, dSafeguardChgToNormal=dSafeguardChgToNormal, dSafeguardEngineState=dSafeguardEngineState, dSafeguardEngineNotifEnable=dSafeguardEngineNotifEnable, dSafeguardEngineCurrentMode=dSafeguardEngineCurrentMode, dSafeguardEngineCompliance=dSafeguardEngineCompliance)
