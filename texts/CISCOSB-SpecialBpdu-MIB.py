#
# PySNMP MIB module CISCOSB-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-SpecialBpdu-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
RowStatus, MacAddress, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString", "TruthValue")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSpecialBpdu.setRevisionsDescriptions(('The private MIB module definition Traffic Segmentation MIB.',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlSpecialBpdu.setContactInfo('Postal: 170 West Tasman Drive\n                San Jose , CA 95134-1706\n                USA\n\n                \n                Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSpecialBpdu.setDescription('<description>')
class EncapType(TextualConvention, Integer32):
    description = 'The L2 encapsulation type. In case the entry contains MAC only,\n         the encapsulation will be none(1), otherwisw:\n         EthernetV2 (2), LLC (2) or LLC-Snap (3)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    description = 'Action to be taken. Bridge(1) or Discard (2)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    description = 'Configured action in the HW. Forward(1), Drop (2) or Trap(3)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduTable.setDescription('A table contains entries of Special BPDU configuration')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1), ).setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEntry.setDescription('An entry of Special BPDU configuration table')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setDescription('Reserved MAC Mc 01:80:C2:00:00:00 - 01:80:C2:00:00:2F.')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEncap.setDescription('L2 Encapsulation Type: Ethernet-V2, LLC or LLC-Snap.')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduProtId.setDescription('Protocol ID. For Ethernet-V2: 0x600 - 0xFFFF; For LLC: 0 - 0xFFFF;\n         For LLC-Snap: 0 - 0xFFFFFFFFFF.')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduAction.setDescription('Action to be taken on the incoming frame: Discard or Bridge.')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setDescription('This object indicates the status of this entry.')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setDescription('A table contains entries of Special BPDU Hw status')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1), ).setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setDescription('An entry of Special BPDU Hw status table')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setDescription('HW action per MAC address: Forward, Drop or Trap.')
mibBuilder.exportSymbols("CISCOSB-SpecialBpdu-MIB", rlSpecialBpduHwAction=rlSpecialBpduHwAction, Action=Action, rlSpecialBpduHwTable=rlSpecialBpduHwTable, rlSpecialBpdu=rlSpecialBpdu, HwAction=HwAction, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduTable=rlSpecialBpduTable, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, EncapType=EncapType, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpduEncap=rlSpecialBpduEncap, PYSNMP_MODULE_ID=rlSpecialBpdu)
