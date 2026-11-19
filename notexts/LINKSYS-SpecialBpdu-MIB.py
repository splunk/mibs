#
# PySNMP MIB module LINKSYS-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-SpecialBpdu-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:16 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, TimeTicks, NotificationType, MibIdentifier, Counter64, iso, Unsigned32, IpAddress, ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "NotificationType", "MibIdentifier", "Counter64", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, RowStatus, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString", "TruthValue")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Linksys LLC.')
class EncapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1), ).setIndexNames((0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2, 1), ).setIndexNames((0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-SpecialBpdu-MIB", rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, rlSpecialBpduHwAction=rlSpecialBpduHwAction, EncapType=EncapType, rlSpecialBpduEntry=rlSpecialBpduEntry, Action=Action, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, rlSpecialBpduHwTable=rlSpecialBpduHwTable, HwAction=HwAction, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpdu=rlSpecialBpdu, PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpduTable=rlSpecialBpduTable)
