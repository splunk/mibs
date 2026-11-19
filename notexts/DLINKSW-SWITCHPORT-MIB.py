#
# PySNMP MIB module DLINKSW-SWITCHPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-SWITCHPORT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, ModuleIdentity, Unsigned32, Gauge32, Bits, iso, ObjectIdentity, Integer32, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Unsigned32", "Gauge32", "Bits", "iso", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
dlinkSwSwitchPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 11))
dlinkSwSwitchPortMIB.setRevisions(('2013-03-04 00:00',))
if mibBuilder.loadTexts: dlinkSwSwitchPortMIB.setLastUpdated('201303040000Z')
if mibBuilder.loadTexts: dlinkSwSwitchPortMIB.setOrganization('D-Link Corp.')
dSwPortNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 11, 0))
dSwPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 11, 1))
dSwPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 11, 2))
dSwPortIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1), )
if mibBuilder.loadTexts: dSwPortIfTable.setStatus('current')
dSwPortIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dSwPortIfEntry.setStatus('current')
dSwPortIfB1000baseTCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("b1000baseTMaster", 2), ("b1000baseTSlave", 3))).clone('b1000baseTMaster')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSwPortIfB1000baseTCtrl.setStatus('current')
dSwPortIfB10GbaseTCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("b10GbaseTMaster", 2), ("b10GbaseTSlave", 3))).clone('b10GbaseTMaster')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSwPortIfB10GbaseTCtrl.setStatus('current')
dSwPortIfMdix = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("normal", 2), ("cross", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSwPortIfMdix.setStatus('current')
dSwPortIfJumboFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 4), Unsigned32().clone(1536)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSwPortIfJumboFrameSize.setStatus('current')
dSwPortIfSpeedAutoDowngrade = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 11, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSwPortIfSpeedAutoDowngrade.setStatus('current')
dSwPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 1))
dSwPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 1, 1)).setObjects(("DLINKSW-SWITCHPORT-MIB", "dSwPortBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSwPortCompliance = dSwPortCompliance.setStatus('current')
dSwPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 2))
dSwPortBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 11, 2, 2, 1)).setObjects(("DLINKSW-SWITCHPORT-MIB", "dSwPortIfB1000baseTCtrl"), ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfB10GbaseTCtrl"), ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfMdix"), ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfJumboFrameSize"), ("DLINKSW-SWITCHPORT-MIB", "dSwPortIfSpeedAutoDowngrade"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSwPortBasicGroup = dSwPortBasicGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-SWITCHPORT-MIB", dSwPortCompliance=dSwPortCompliance, dSwPortIfB1000baseTCtrl=dSwPortIfB1000baseTCtrl, dSwPortIfB10GbaseTCtrl=dSwPortIfB10GbaseTCtrl, dSwPortIfJumboFrameSize=dSwPortIfJumboFrameSize, dSwPortConformance=dSwPortConformance, PYSNMP_MODULE_ID=dlinkSwSwitchPortMIB, dSwPortNotifications=dSwPortNotifications, dSwPortIfMdix=dSwPortIfMdix, dSwPortObjects=dSwPortObjects, dlinkSwSwitchPortMIB=dlinkSwSwitchPortMIB, dSwPortCompliances=dSwPortCompliances, dSwPortIfSpeedAutoDowngrade=dSwPortIfSpeedAutoDowngrade, dSwPortIfEntry=dSwPortIfEntry, dSwPortBasicGroup=dSwPortBasicGroup, dSwPortIfTable=dSwPortIfTable, dSwPortGroups=dSwPortGroups)
