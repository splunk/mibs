#
# PySNMP MIB module CISCO-MAU-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAU-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifMauIndex, ifMauIfIndex, ifJackEntry = mibBuilder.importSymbols("MAU-MIB", "ifMauIndex", "ifMauIfIndex", "ifJackEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoMauExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 398))
ciscoMauExtMIB.setRevisions(('2008-03-05 00:00', '2004-04-21 00:00',))
if mibBuilder.loadTexts: ciscoMauExtMIB.setLastUpdated('200803050000Z')
if mibBuilder.loadTexts: ciscoMauExtMIB.setOrganization('Cisco Systems, Inc.')
cmExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 0))
cmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1))
cmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2))
cmExtMauConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1))
cmExtJackConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1), )
if mibBuilder.loadTexts: cmExtJackConfigTable.setStatus('current')
cmExtJackConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1), )
ifJackEntry.registerAugmentions(("CISCO-MAU-EXT-MIB", "cmExtJackConfigEntry"))
cmExtJackConfigEntry.setIndexNames(*ifJackEntry.getIndexNames())
if mibBuilder.loadTexts: cmExtJackConfigEntry.setStatus('current')
cmExtJackState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmExtJackState.setStatus('current')
cmExtAutoMdixConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2))
cmExtIfAutoMdixConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1), )
if mibBuilder.loadTexts: cmExtIfAutoMdixConfigTable.setStatus('current')
cmExtIfAutoMdixConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: cmExtIfAutoMdixConfigEntry.setStatus('current')
cmExtIfAutoMdixEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmExtIfAutoMdixEnabled.setStatus('current')
cmExtIfMau = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3))
cmExtIfMauTrafficTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1), )
if mibBuilder.loadTexts: cmExtIfMauTrafficTable.setStatus('current')
cmExtIfMauTrafficEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: cmExtIfMauTrafficEntry.setStatus('current')
cmExtIfMauTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("adminControl", 2), ("user", 3))).clone('user')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmExtIfMauTrafficType.setStatus('current')
cmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1))
cmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2))
cmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 1)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance = cmExtMIBCompliance.setStatus('deprecated')
cmExtMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 2)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance2 = cmExtMIBCompliance2.setStatus('deprecated')
cmExtMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 3)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance3 = cmExtMIBCompliance3.setStatus('current')
cmExtJackConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 1)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtJackConfigGroup = cmExtJackConfigGroup.setStatus('current')
cmExtIfAutoMdixConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 2)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtIfAutoMdixConfigGroup = cmExtIfAutoMdixConfigGroup.setStatus('current')
cmExtIfMauTrafficGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 3)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtIfMauTrafficGroup = cmExtIfMauTrafficGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-EXT-MIB", cmExtJackConfigGroup=cmExtJackConfigGroup, cmExtMauConfig=cmExtMauConfig, cmExtJackState=cmExtJackState, cmExtIfMauTrafficEntry=cmExtIfMauTrafficEntry, cmExtJackConfigEntry=cmExtJackConfigEntry, cmExtAutoMdixConfig=cmExtAutoMdixConfig, cmExtMIBObjects=cmExtMIBObjects, cmExtIfMauTrafficType=cmExtIfMauTrafficType, cmExtMIBCompliance2=cmExtMIBCompliance2, cmExtIfMauTrafficGroup=cmExtIfMauTrafficGroup, cmExtIfAutoMdixConfigGroup=cmExtIfAutoMdixConfigGroup, cmExtMIBCompliance3=cmExtMIBCompliance3, cmExtMIBCompliance=cmExtMIBCompliance, cmExtIfMauTrafficTable=cmExtIfMauTrafficTable, cmExtMIBCompliances=cmExtMIBCompliances, cmExtMIBGroups=cmExtMIBGroups, cmExtIfAutoMdixEnabled=cmExtIfAutoMdixEnabled, cmExtIfMau=cmExtIfMau, cmExtIfAutoMdixConfigTable=cmExtIfAutoMdixConfigTable, cmExtMIBConformance=cmExtMIBConformance, cmExtMIBNotifs=cmExtMIBNotifs, ciscoMauExtMIB=ciscoMauExtMIB, cmExtIfAutoMdixConfigEntry=cmExtIfAutoMdixConfigEntry, PYSNMP_MODULE_ID=ciscoMauExtMIB, cmExtJackConfigTable=cmExtJackConfigTable)
