#
# PySNMP MIB module CISCOSB-ROUTEMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-ROUTEMAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "TimeTicks")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlRouteMap = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227))
rlRouteMap.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlRouteMap.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlRouteMap.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlRouteMap.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlRouteMap.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n\n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlRouteMap.setDescription('The private MIB module definition for Route Map distribution mechanism.')
class RlRouteMapInetType(TextualConvention, Integer32):
    description = 'The inet type of a route map'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlRouteMapPbrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1), )
if mibBuilder.loadTexts: rlRouteMapPbrTable.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrTable.setDescription('Main table serving as container for route map table definition.')
rlRouteMapPbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1), ).setIndexNames((0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrInetType"))
if mibBuilder.loadTexts: rlRouteMapPbrEntry.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrEntry.setDescription('The row definition for this table.')
rlRouteMapPbrRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapName.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapName.setDescription('Name (identifier) of the route map.')
rlRouteMapPbrRouteMapSectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapSectionId.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapSectionId.setDescription('Identifier of single section the route map.')
rlRouteMapPbrInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 3), RlRouteMapInetType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrInetType.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrInetType.setDescription('Inet type of this route-map.')
rlRouteMapPbrMatchAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrMatchAccessListName.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrMatchAccessListName.setDescription('Identifier of access list, if used for matching.')
rlRouteMapPbrActionNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddressType.setDescription('The inet type of rlRouteMapPbrActionNexthopInetAddress')
rlRouteMapPbrActionNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddress.setDescription('Inet address of nexthop, if used for action.')
rlRouteMapPbrActionNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopIfIndex.setDescription('Inet address of nexthop, if used for action.')
rlRouteMapPbrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrRowStatus.setDescription('The row status of this entry.')
mibBuilder.exportSymbols("CISCOSB-ROUTEMAP-MIB", RlRouteMapInetType=RlRouteMapInetType, rlRouteMap=rlRouteMap, rlRouteMapPbrActionNexthopInetAddress=rlRouteMapPbrActionNexthopInetAddress, PYSNMP_MODULE_ID=rlRouteMap, rlRouteMapPbrRowStatus=rlRouteMapPbrRowStatus, rlRouteMapPbrRouteMapName=rlRouteMapPbrRouteMapName, rlRouteMapPbrInetType=rlRouteMapPbrInetType, rlRouteMapPbrRouteMapSectionId=rlRouteMapPbrRouteMapSectionId, rlRouteMapPbrActionNexthopIfIndex=rlRouteMapPbrActionNexthopIfIndex, rlRouteMapPbrMatchAccessListName=rlRouteMapPbrMatchAccessListName, rlRouteMapPbrTable=rlRouteMapPbrTable, rlRouteMapPbrActionNexthopInetAddressType=rlRouteMapPbrActionNexthopInetAddressType, rlRouteMapPbrEntry=rlRouteMapPbrEntry)
