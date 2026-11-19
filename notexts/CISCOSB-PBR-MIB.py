#
# PySNMP MIB module CISCOSB-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-PBR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
rlRouteMapPbrRouteMapName, rlRouteMapPbrRouteMapSectionId = mibBuilder.importSymbols("CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName", "rlRouteMapPbrRouteMapSectionId")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressType, InetAddress, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressIPv6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlPolicyBasedRouting = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228))
rlPolicyBasedRouting.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: rlPolicyBasedRouting.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setOrganization('Cisco Systems, Inc.')
class RlPBRInetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class RlPBRStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("noIp", 2), ("interfaceDown", 3))

rlPBRTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1), )
if mibBuilder.loadTexts: rlPBRTable.setStatus('current')
rlPBREntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1), ).setIndexNames((0, "CISCOSB-PBR-MIB", "rlPBRIfIndex"), (0, "CISCOSB-PBR-MIB", "rlPBRInetType"))
if mibBuilder.loadTexts: rlPBREntry.setStatus('current')
rlPBRIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlPBRIfIndex.setStatus('current')
rlPBRInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 2), RlPBRInetType())
if mibBuilder.loadTexts: rlPBRInetType.setStatus('current')
rlPBRRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRouteMapName.setStatus('current')
rlPBRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 4), RlPBRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRStatus.setStatus('current')
rlPBRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRowStatus.setStatus('current')
class RlPBRNexthopStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notReachable", 2), ("notDirect", 3))

rlPBRInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2), )
if mibBuilder.loadTexts: rlPBRInfoTable.setStatus('current')
rlPBRInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1), ).setIndexNames((0, "CISCOSB-PBR-MIB", "rlPBRInetType"), (0, "CISCOSB-PBR-MIB", "rlPBRIfIndex"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"))
if mibBuilder.loadTexts: rlPBRInfoEntry.setStatus('current')
rlPBRInfoAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setStatus('current')
rlPBRInfoNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setStatus('current')
rlPBRInfoNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setStatus('current')
rlPBRInfoNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setStatus('current')
rlPBRInfoNexthopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 5), RlPBRNexthopStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-PBR-MIB", rlPBRInfoNexthopIfIndex=rlPBRInfoNexthopIfIndex, rlPBRInetType=rlPBRInetType, rlPolicyBasedRouting=rlPolicyBasedRouting, rlPBRRowStatus=rlPBRRowStatus, rlPBRInfoNexthopStatus=rlPBRInfoNexthopStatus, RlPBRNexthopStatusType=RlPBRNexthopStatusType, rlPBREntry=rlPBREntry, rlPBRInfoNexthopInetAddress=rlPBRInfoNexthopInetAddress, rlPBRIfIndex=rlPBRIfIndex, RlPBRStatusType=RlPBRStatusType, rlPBRTable=rlPBRTable, rlPBRInfoTable=rlPBRInfoTable, rlPBRRouteMapName=rlPBRRouteMapName, rlPBRInfoAccessListName=rlPBRInfoAccessListName, rlPBRInfoEntry=rlPBRInfoEntry, rlPBRStatus=rlPBRStatus, rlPBRInfoNexthopInetAddressType=rlPBRInfoNexthopInetAddressType, PYSNMP_MODULE_ID=rlPolicyBasedRouting, RlPBRInetType=RlPBRInetType)
