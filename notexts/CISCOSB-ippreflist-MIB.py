#
# PySNMP MIB module CISCOSB-ippreflist-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-ippreflist-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InetAddressType, InetVersion, InetZoneIndex, InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetVersion", "InetZoneIndex", "InetAddress", "InetAddressPrefixLength")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Integer32, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Integer32", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
TimeStamp, TruthValue, TextualConvention, DisplayString, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "TextualConvention", "DisplayString", "RowStatus", "DateAndTime")
rlIpPrefList = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212))
class RlIpPrefListEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rule", 1), ("description", 2))

class RlIpPrefListActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("drop", 1), ("permit", 2))

class RlIpPrefListType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlIpPrefListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1), )
if mibBuilder.loadTexts: rlIpPrefListTable.setStatus('current')
rlIpPrefListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1), ).setIndexNames((0, "CISCOSB-ippreflist-MIB", "rlIpPrefListType"), (0, "CISCOSB-ippreflist-MIB", "rlIpPrefListName"), (0, "CISCOSB-ippreflist-MIB", "rlIpPrefListEntryIndex"))
if mibBuilder.loadTexts: rlIpPrefListEntry.setStatus('current')
rlIpPrefListType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 1), RlIpPrefListType())
if mibBuilder.loadTexts: rlIpPrefListType.setStatus('current')
rlIpPrefListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlIpPrefListName.setStatus('current')
rlIpPrefListEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)))
if mibBuilder.loadTexts: rlIpPrefListEntryIndex.setStatus('current')
rlIpPrefListEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 4), RlIpPrefListEntryType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListEntryType.setStatus('current')
rlIpPrefListInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListInetAddrType.setStatus('current')
rlIpPrefListInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListInetAddr.setStatus('current')
rlIpPrefListPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListPrefixLength.setStatus('current')
rlIpPrefListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 8), RlIpPrefListActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListAction.setStatus('current')
rlIpPrefListGeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListGeLength.setStatus('current')
rlIpPrefListLeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListLeLength.setStatus('current')
rlIpPrefListDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListDescription.setStatus('current')
rlIpPrefListHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 12), Integer32())
if mibBuilder.loadTexts: rlIpPrefListHitCount.setStatus('current')
rlIpPrefListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 1, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListRowStatus.setStatus('current')
rlIpPrefListInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2), )
if mibBuilder.loadTexts: rlIpPrefListInfoTable.setStatus('current')
rlIpPrefListInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2, 1), ).setIndexNames((0, "CISCOSB-ippreflist-MIB", "rlIpPrefListInfoType"), (0, "CISCOSB-ippreflist-MIB", "rlIpPrefListInfoName"))
if mibBuilder.loadTexts: rlIpPrefListInfoEntry.setStatus('current')
rlIpPrefListInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2, 1, 1), RlIpPrefListType())
if mibBuilder.loadTexts: rlIpPrefListInfoType.setStatus('current')
rlIpPrefListInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlIpPrefListInfoName.setStatus('current')
rlIpPrefListInfoEntriesNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoEntriesNumber.setStatus('current')
rlIpPrefListInfoRangeEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoRangeEntries.setStatus('current')
rlIpPrefListInfoNextFreeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoNextFreeIndex.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-ippreflist-MIB", rlIpPrefListHitCount=rlIpPrefListHitCount, rlIpPrefListInfoEntriesNumber=rlIpPrefListInfoEntriesNumber, rlIpPrefListInfoNextFreeIndex=rlIpPrefListInfoNextFreeIndex, rlIpPrefListInfoTable=rlIpPrefListInfoTable, rlIpPrefListInfoType=rlIpPrefListInfoType, rlIpPrefListRowStatus=rlIpPrefListRowStatus, rlIpPrefListEntry=rlIpPrefListEntry, rlIpPrefListAction=rlIpPrefListAction, rlIpPrefListEntryType=rlIpPrefListEntryType, rlIpPrefListInetAddrType=rlIpPrefListInetAddrType, rlIpPrefListType=rlIpPrefListType, rlIpPrefListInfoRangeEntries=rlIpPrefListInfoRangeEntries, rlIpPrefListInfoEntry=rlIpPrefListInfoEntry, rlIpPrefListInfoName=rlIpPrefListInfoName, rlIpPrefListDescription=rlIpPrefListDescription, rlIpPrefList=rlIpPrefList, rlIpPrefListGeLength=rlIpPrefListGeLength, rlIpPrefListName=rlIpPrefListName, rlIpPrefListLeLength=rlIpPrefListLeLength, rlIpPrefListTable=rlIpPrefListTable, RlIpPrefListType=RlIpPrefListType, rlIpPrefListInetAddr=rlIpPrefListInetAddr, RlIpPrefListActionType=RlIpPrefListActionType, rlIpPrefListPrefixLength=rlIpPrefListPrefixLength, rlIpPrefListEntryIndex=rlIpPrefListEntryIndex, RlIpPrefListEntryType=RlIpPrefListEntryType)
