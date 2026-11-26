#
# PySNMP MIB module CISCO-WAN-CODEC-GEN-PARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-CODEC-GEN-PARM-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanCodecGenParmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 21))
ciscoWanCodecGenParmMIB.setRevisions(('2004-03-17 00:00', '2004-01-30 00:00', '2003-05-23 00:00', '2001-09-10 00:00', '2001-08-21 15:00', '2001-08-02 15:00', '2001-06-15 15:00', '2001-03-20 15:00',))
if mibBuilder.loadTexts: ciscoWanCodecGenParmMIB.setLastUpdated('200403170000Z')
if mibBuilder.loadTexts: ciscoWanCodecGenParmMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanCodecGenParmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 1))
vismCodecGenParmGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1))
vismCodecGenParmTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1), )
if mibBuilder.loadTexts: vismCodecGenParmTable.setStatus('current')
vismCodecGenParmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecIndex"))
if mibBuilder.loadTexts: vismCodecGenParmEntry.setStatus('current')
vismCodecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("g711u", 1), ("g711a", 2), ("g726r32000", 3), ("g729a", 4), ("g729ab", 5), ("clearChannel", 6), ("g726r16000", 7), ("g726r24000", 8), ("g726r40000", 9), ("g723h", 11), ("g723ah", 12), ("g723l", 13), ("g723al", 14), ("lossless", 15))))
if mibBuilder.loadTexts: vismCodecIndex.setStatus('current')
vismCodecJitterDelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fixed", 1), ("adaptive", 2), ("fixedWithTimeStamp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCodecJitterDelayMode.setStatus('current')
vismCodecJitterInitialDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 21, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100))).clone(namedValues=NamedValues(("zero", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9), ("ten", 10), ("eleven", 11), ("twelve", 12), ("thirteen", 13), ("fourteen", 14), ("fifteen", 15), ("sixteen", 16), ("seventeen", 17), ("eighteen", 18), ("nineteen", 19), ("twenty", 20), ("twentyone", 21), ("twentytwo", 22), ("twentythree", 23), ("twentyfour", 24), ("twentyfive", 25), ("twentysix", 26), ("twentyseven", 27), ("twentyeight", 28), ("twentynine", 29), ("thirty", 30), ("thirtyone", 31), ("thirtytwo", 32), ("thirtythree", 33), ("thirtyfour", 34), ("thirtyfive", 35), ("thirtysix", 36), ("thirtyseven", 37), ("thirtyeight", 38), ("thirtynine", 39), ("fourty", 40), ("fortyone", 41), ("fortytwo", 42), ("fortythree", 43), ("fortyfour", 44), ("fortyfive", 45), ("fortysix", 46), ("fortyseven", 47), ("fortyeight", 48), ("fortynine", 49), ("fifty", 50), ("fiftyfive", 55), ("sixty", 60), ("sixtyfive", 65), ("seventy", 70), ("seventyfive", 75), ("eighty", 80), ("eightyfive", 85), ("ninty", 90), ("ninetyfive", 95), ("hundred", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCodecJitterInitialDelay.setStatus('current')
vismCodecGenParmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 2))
vismCodecGenParmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 2, 0))
vismCodecGenParmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 3))
vismCodecGenParmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 1))
vismCodecGenParmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 2))
vismCodecGenParmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 1, 1)).setObjects(("CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecGenParmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismCodecGenParmMIBCompliance = vismCodecGenParmMIBCompliance.setStatus('current')
vismCodecGenParmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 21, 3, 2, 1)).setObjects(("CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecJitterDelayMode"), ("CISCO-WAN-CODEC-GEN-PARM-MIB", "vismCodecJitterInitialDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismCodecGenParmGroup = vismCodecGenParmGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-CODEC-GEN-PARM-MIB", ciscoWanCodecGenParmMIB=ciscoWanCodecGenParmMIB, vismCodecGenParmTable=vismCodecGenParmTable, vismCodecGenParmGrp=vismCodecGenParmGrp, vismCodecGenParmEntry=vismCodecGenParmEntry, vismCodecGenParmMIBCompliance=vismCodecGenParmMIBCompliance, ciscoWanCodecGenParmMIBObjects=ciscoWanCodecGenParmMIBObjects, vismCodecGenParmMIBConformance=vismCodecGenParmMIBConformance, vismCodecGenParmMIBCompliances=vismCodecGenParmMIBCompliances, vismCodecGenParmNotifications=vismCodecGenParmNotifications, vismCodecGenParmNotificationPrefix=vismCodecGenParmNotificationPrefix, vismCodecJitterDelayMode=vismCodecJitterDelayMode, vismCodecIndex=vismCodecIndex, vismCodecGenParmMIBGroups=vismCodecGenParmMIBGroups, vismCodecGenParmGroup=vismCodecGenParmGroup, vismCodecJitterInitialDelay=vismCodecJitterInitialDelay, PYSNMP_MODULE_ID=ciscoWanCodecGenParmMIB)
