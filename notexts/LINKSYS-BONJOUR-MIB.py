#
# PySNMP MIB module LINKSYS-BONJOUR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-BONJOUR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:38:08 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, IpAddress, Unsigned32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "IpAddress", "Unsigned32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
rlBonjour = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114))
rlBonjour.setRevisions(('2009-04-23 00:00',))
if mibBuilder.loadTexts: rlBonjour.setLastUpdated('200909210000Z')
if mibBuilder.loadTexts: rlBonjour.setOrganization('Linksys LLC.')
rlBonjourPublish = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourPublish.setStatus('current')
class RlBonjourServiceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlBonjourNotPublished", 0), ("rlBonjourInactive", 1), ("rlBonjourRegistering", 2), ("rlBonjourRunning", 3))

class RlBonjourOperationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class RlBonjourOperationReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notExclude", 0), ("include", 1), ("notInclude", 2), ("exclude", 3), ("bonjourDisabled", 4), ("serviceDisabled", 5), ("noIPaddress", 6), ("l2InterfaceDown", 7), ("notPresent", 8), ("unknown", 9))

rlBonjourStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2), )
if mibBuilder.loadTexts: rlBonjourStatusTable.setStatus('current')
rlBonjourStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1), ).setIndexNames((0, "LINKSYS-BONJOUR-MIB", "rlBonjourStatusServiceName"), (0, "LINKSYS-BONJOUR-MIB", "rlBonjourStatusIPInterfaceType"), (0, "LINKSYS-BONJOUR-MIB", "rlBonjourStatusIPInterfaceAddr"))
if mibBuilder.loadTexts: rlBonjourStatusEntry.setStatus('current')
rlBonjourStatusServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStatusServiceName.setStatus('current')
rlBonjourStatusIPInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceType.setStatus('current')
rlBonjourStatusIPInterfaceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceAddr.setStatus('current')
rlBonjourStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 4), RlBonjourServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStatusState.setStatus('current')
rlBonjourStateTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3), )
if mibBuilder.loadTexts: rlBonjourStateTable.setStatus('current')
rlBonjourStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1), ).setIndexNames((0, "LINKSYS-BONJOUR-MIB", "rlBonjourStateServiceName"), (0, "LINKSYS-BONJOUR-MIB", "rlBonjourStateL2Interface"))
if mibBuilder.loadTexts: rlBonjourStateEntry.setStatus('current')
rlBonjourStateServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStateServiceName.setStatus('current')
rlBonjourStateL2Interface = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourStateL2Interface.setStatus('current')
rlBonjourStateOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 3), RlBonjourOperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationMode.setStatus('current')
rlBonjourStateOperationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 4), RlBonjourOperationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationReason.setStatus('current')
rlBonjourL2Table = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4), )
if mibBuilder.loadTexts: rlBonjourL2Table.setStatus('current')
rlBonjourL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4, 1), ).setIndexNames((0, "LINKSYS-BONJOUR-MIB", "rlBonjourL2Ifindex"))
if mibBuilder.loadTexts: rlBonjourL2Entry.setStatus('current')
rlBonjourL2Ifindex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourL2Ifindex.setStatus('current')
rlBonjourL2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2RowStatus.setStatus('current')
rlBonjourL2Mode = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2Mode.setStatus('current')
rlBonjourInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourInstanceName.setStatus('current')
rlBonjourHostName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourHostName.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-BONJOUR-MIB", rlBonjourL2RowStatus=rlBonjourL2RowStatus, rlBonjourStatusServiceName=rlBonjourStatusServiceName, rlBonjourStateEntry=rlBonjourStateEntry, rlBonjourL2Ifindex=rlBonjourL2Ifindex, rlBonjour=rlBonjour, rlBonjourStateTable=rlBonjourStateTable, RlBonjourOperationReason=RlBonjourOperationReason, RlBonjourServiceState=RlBonjourServiceState, rlBonjourStateL2Interface=rlBonjourStateL2Interface, rlBonjourStatusEntry=rlBonjourStatusEntry, rlBonjourStatusTable=rlBonjourStatusTable, rlBonjourHostName=rlBonjourHostName, rlBonjourL2Mode=rlBonjourL2Mode, rlBonjourStatusIPInterfaceType=rlBonjourStatusIPInterfaceType, rlBonjourInstanceName=rlBonjourInstanceName, PYSNMP_MODULE_ID=rlBonjour, rlBonjourStateOperationReason=rlBonjourStateOperationReason, rlBonjourL2Entry=rlBonjourL2Entry, rlBonjourStateOperationMode=rlBonjourStateOperationMode, rlBonjourL2Table=rlBonjourL2Table, rlBonjourStatusState=rlBonjourStatusState, RlBonjourOperationState=RlBonjourOperationState, rlBonjourStatusIPInterfaceAddr=rlBonjourStatusIPInterfaceAddr, rlBonjourStateServiceName=rlBonjourStateServiceName, rlBonjourPublish=rlBonjourPublish)
