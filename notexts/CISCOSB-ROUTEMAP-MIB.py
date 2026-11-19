#
# PySNMP MIB module CISCOSB-ROUTEMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-ROUTEMAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressType, InetAddress, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressIPv6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlRouteMap = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227))
rlRouteMap.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: rlRouteMap.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlRouteMap.setOrganization('Cisco Systems, Inc.')
class RlRouteMapInetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlRouteMapPbrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1), )
if mibBuilder.loadTexts: rlRouteMapPbrTable.setStatus('current')
rlRouteMapPbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1), ).setIndexNames((0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrInetType"))
if mibBuilder.loadTexts: rlRouteMapPbrEntry.setStatus('current')
rlRouteMapPbrRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapName.setStatus('current')
rlRouteMapPbrRouteMapSectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapSectionId.setStatus('current')
rlRouteMapPbrInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 3), RlRouteMapInetType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrInetType.setStatus('current')
rlRouteMapPbrMatchAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrMatchAccessListName.setStatus('current')
rlRouteMapPbrActionNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddressType.setStatus('current')
rlRouteMapPbrActionNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddress.setStatus('current')
rlRouteMapPbrActionNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopIfIndex.setStatus('current')
rlRouteMapPbrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrRowStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-ROUTEMAP-MIB", rlRouteMapPbrTable=rlRouteMapPbrTable, rlRouteMapPbrMatchAccessListName=rlRouteMapPbrMatchAccessListName, rlRouteMapPbrActionNexthopIfIndex=rlRouteMapPbrActionNexthopIfIndex, rlRouteMap=rlRouteMap, rlRouteMapPbrRowStatus=rlRouteMapPbrRowStatus, rlRouteMapPbrEntry=rlRouteMapPbrEntry, rlRouteMapPbrInetType=rlRouteMapPbrInetType, rlRouteMapPbrActionNexthopInetAddress=rlRouteMapPbrActionNexthopInetAddress, PYSNMP_MODULE_ID=rlRouteMap, RlRouteMapInetType=RlRouteMapInetType, rlRouteMapPbrRouteMapSectionId=rlRouteMapPbrRouteMapSectionId, rlRouteMapPbrActionNexthopInetAddressType=rlRouteMapPbrActionNexthopInetAddressType, rlRouteMapPbrRouteMapName=rlRouteMapPbrRouteMapName)
