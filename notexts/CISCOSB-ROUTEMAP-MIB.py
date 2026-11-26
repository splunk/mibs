#
# PySNMP MIB module CISCOSB-ROUTEMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-ROUTEMAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("CISCOSB-ROUTEMAP-MIB", rlRouteMapPbrActionNexthopInetAddress=rlRouteMapPbrActionNexthopInetAddress, rlRouteMapPbrActionNexthopIfIndex=rlRouteMapPbrActionNexthopIfIndex, rlRouteMapPbrTable=rlRouteMapPbrTable, rlRouteMapPbrEntry=rlRouteMapPbrEntry, rlRouteMap=rlRouteMap, rlRouteMapPbrInetType=rlRouteMapPbrInetType, rlRouteMapPbrActionNexthopInetAddressType=rlRouteMapPbrActionNexthopInetAddressType, rlRouteMapPbrMatchAccessListName=rlRouteMapPbrMatchAccessListName, rlRouteMapPbrRouteMapSectionId=rlRouteMapPbrRouteMapSectionId, RlRouteMapInetType=RlRouteMapInetType, rlRouteMapPbrRowStatus=rlRouteMapPbrRowStatus, rlRouteMapPbrRouteMapName=rlRouteMapPbrRouteMapName, PYSNMP_MODULE_ID=rlRouteMap)
