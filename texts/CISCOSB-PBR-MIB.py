#
# PySNMP MIB module CISCOSB-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-PBR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
rlRouteMapPbrRouteMapName, rlRouteMapPbrRouteMapSectionId = mibBuilder.importSymbols("CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName", "rlRouteMapPbrRouteMapSectionId")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "TimeTicks")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlPolicyBasedRouting = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228))
rlPolicyBasedRouting.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlPolicyBasedRouting.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlPolicyBasedRouting.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n         \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setDescription('The private MIB module definition for Policy-Based Routing mechanism.')
class RlPBRInetType(TextualConvention, Integer32):
    description = 'The inet type of a policy'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class RlPBRStatusType(TextualConvention, Integer32):
    description = 'The types of status for policy-based routing entry'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("noIp", 2), ("interfaceDown", 3))

rlPBRTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1), )
if mibBuilder.loadTexts: rlPBRTable.setStatus('current')
if mibBuilder.loadTexts: rlPBRTable.setDescription('Table containing policy-based routing binding information.')
rlPBREntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1), ).setIndexNames((0, "CISCOSB-PBR-MIB", "rlPBRIfIndex"), (0, "CISCOSB-PBR-MIB", "rlPBRInetType"))
if mibBuilder.loadTexts: rlPBREntry.setStatus('current')
if mibBuilder.loadTexts: rlPBREntry.setDescription('The row definition for this table.')
rlPBRIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlPBRIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlPBRIfIndex.setDescription('IfIndex on which policy based routing is applied.')
rlPBRInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 2), RlPBRInetType())
if mibBuilder.loadTexts: rlPBRInetType.setStatus('current')
if mibBuilder.loadTexts: rlPBRInetType.setDescription('Inet type of this entry.')
rlPBRRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRouteMapName.setStatus('current')
if mibBuilder.loadTexts: rlPBRRouteMapName.setDescription('Route map name to apply.')
rlPBRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 4), RlPBRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRStatus.setStatus('current')
if mibBuilder.loadTexts: rlPBRStatus.setDescription('The route status for this entry.')
rlPBRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlPBRRowStatus.setDescription('The row status of this entry.')
class RlPBRNexthopStatusType(TextualConvention, Integer32):
    description = 'The types of status of nexthop for policy-based routing entry'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notReachable", 2), ("notDirect", 3))

rlPBRInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2), )
if mibBuilder.loadTexts: rlPBRInfoTable.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoTable.setDescription('Table containing policy-based routing information.')
rlPBRInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1), ).setIndexNames((0, "CISCOSB-PBR-MIB", "rlPBRInetType"), (0, "CISCOSB-PBR-MIB", "rlPBRIfIndex"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"))
if mibBuilder.loadTexts: rlPBRInfoEntry.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoEntry.setDescription('The row definition for this table.')
rlPBRInfoAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setDescription('Access-list name of policy-based routing.')
rlPBRInfoNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setDescription('Inet type of rlPBRInfoNexthopInetAddress')
rlPBRInfoNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setDescription('Inet address of nexthop, if used for action.')
rlPBRInfoNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setDescription('Inet address of nexthop, if used for action.')
rlPBRInfoNexthopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 5), RlPBRNexthopStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setStatus('current')
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setDescription('Status of nexthop.')
mibBuilder.exportSymbols("CISCOSB-PBR-MIB", rlPolicyBasedRouting=rlPolicyBasedRouting, rlPBRInfoNexthopStatus=rlPBRInfoNexthopStatus, rlPBRIfIndex=rlPBRIfIndex, rlPBRRouteMapName=rlPBRRouteMapName, rlPBRInfoAccessListName=rlPBRInfoAccessListName, RlPBRStatusType=RlPBRStatusType, rlPBRInfoEntry=rlPBRInfoEntry, PYSNMP_MODULE_ID=rlPolicyBasedRouting, rlPBRStatus=rlPBRStatus, rlPBRRowStatus=rlPBRRowStatus, rlPBREntry=rlPBREntry, rlPBRInetType=rlPBRInetType, RlPBRNexthopStatusType=RlPBRNexthopStatusType, rlPBRInfoNexthopInetAddress=rlPBRInfoNexthopInetAddress, RlPBRInetType=RlPBRInetType, rlPBRInfoNexthopInetAddressType=rlPBRInfoNexthopInetAddressType, rlPBRTable=rlPBRTable, rlPBRInfoNexthopIfIndex=rlPBRInfoNexthopIfIndex, rlPBRInfoTable=rlPBRInfoTable)
