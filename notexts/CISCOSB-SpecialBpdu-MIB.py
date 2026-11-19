#
# PySNMP MIB module CISCOSB-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-SpecialBpdu-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, RowStatus, TextualConvention, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "MacAddress", "TruthValue")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Cisco Systems, Inc.')
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

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1), ).setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1), ).setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SpecialBpdu-MIB", rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, PYSNMP_MODULE_ID=rlSpecialBpdu, Action=Action, rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpduTable=rlSpecialBpduTable, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduHwTable=rlSpecialBpduHwTable, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, rlSpecialBpduHwAction=rlSpecialBpduHwAction, rlSpecialBpdu=rlSpecialBpdu, rlSpecialBpduProtId=rlSpecialBpduProtId, HwAction=HwAction, EncapType=EncapType)
