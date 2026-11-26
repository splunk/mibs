#
# PySNMP MIB module LINKSYS-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-SpecialBpdu-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity")
RowStatus, TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSpecialBpdu.setRevisionsDescriptions(('The private MIB module definition Traffic Segmentation MIB.',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlSpecialBpdu.setContactInfo('www.linksys.com/business/support')
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

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduTable.setDescription('A table contains entries of Special BPDU configuration')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1), ).setIndexNames((0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEntry.setDescription('An entry of Special BPDU configuration table')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setDescription('Reserved MAC Mc 01:80:C2:00:00:00 - 01:80:C2:00:00:2F.')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEncap.setDescription('L2 Encapsulation Type: Ethernet-V2, LLC or LLC-Snap.')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduProtId.setDescription('Protocol ID. For Ethernet-V2: 0x600 - 0xFFFF; For LLC: 0 - 0xFFFF;\n         For LLC-Snap: 0 - 0xFFFFFFFFFF.')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduAction.setDescription('Action to be taken on the incoming frame: Discard or Bridge.')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setDescription('This object indicates the status of this entry.')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setDescription('A table contains entries of Special BPDU Hw status')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2, 1), ).setIndexNames((0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setDescription('An entry of Special BPDU Hw status table')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setDescription('HW action per MAC address: Forward, Drop or Trap.')
mibBuilder.exportSymbols("LINKSYS-SpecialBpdu-MIB", HwAction=HwAction, EncapType=EncapType, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpduTable=rlSpecialBpduTable, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, rlSpecialBpduHwAction=rlSpecialBpduHwAction, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduHwTable=rlSpecialBpduHwTable, Action=Action, rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpdu=rlSpecialBpdu, PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry)
