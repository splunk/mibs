#
# PySNMP MIB module CISCO-WAN-ATM-PREF-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-ATM-PREF-ROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PnniNodeId, PnniPortId = mibBuilder.importSymbols("PNNI-MIB", "PnniNodeId", "PnniPortId")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoWanATMPrefRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99996))
ciscoWanATMPrefRouteMIB.setRevisions(('2002-06-25 00:00',))
if mibBuilder.loadTexts: ciscoWanATMPrefRouteMIB.setLastUpdated('200206250000Z')
if mibBuilder.loadTexts: ciscoWanATMPrefRouteMIB.setOrganization('Cisco System Inc.')
ciscoWanATMPrefRouteMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 0))
ciscoWanATMPrefRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1))
cwaPrefRouteConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2))
class RouteId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cwaPrefRouteConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1), )
if mibBuilder.loadTexts: cwaPrefRouteConfTable.setStatus('current')
cwaPrefRouteConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteId"))
if mibBuilder.loadTexts: cwaPrefRouteConfEntry.setStatus('current')
cwaPrefRouteId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1), RouteId())
if mibBuilder.loadTexts: cwaPrefRouteId.setStatus('current')
cwaPrefRouteNwElemCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemCount.setStatus('current')
cwaPrefRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteRowStatus.setStatus('current')
cwaPrefRouteNwElemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2), )
if mibBuilder.loadTexts: cwaPrefRouteNwElemTable.setStatus('current')
cwaPrefRouteNwElemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1), ).setIndexNames((0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteId"), (0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemPos"))
if mibBuilder.loadTexts: cwaPrefRouteNwElemEntry.setStatus('current')
cwaPrefRouteNwElemPos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: cwaPrefRouteNwElemPos.setStatus('current')
cwaPrefRouteNwElemNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 2), PnniNodeId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemNodeId.setStatus('current')
cwaPrefRouteNwElemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 3), PnniPortId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemPortId.setStatus('current')
cwaPrefRouteNwElemRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemRowStatus.setStatus('current')
cwaPrefRouteCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1))
cwaPrefMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2))
cwaPrefMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaPrefMIBCompliance = cwaPrefMIBCompliance.setStatus('current')
cwaPrefRouteMIBGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2, 1)).setObjects(("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemCount"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteRowStatus"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemNodeId"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemPortId"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaPrefRouteMIBGroups = cwaPrefRouteMIBGroups.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-PREF-ROUTE-MIB", cwaPrefRouteNwElemCount=cwaPrefRouteNwElemCount, cwaPrefRouteNwElemEntry=cwaPrefRouteNwElemEntry, cwaPrefRouteNwElemNodeId=cwaPrefRouteNwElemNodeId, cwaPrefRouteId=cwaPrefRouteId, cwaPrefRouteNwElemRowStatus=cwaPrefRouteNwElemRowStatus, RouteId=RouteId, cwaPrefRouteNwElemPos=cwaPrefRouteNwElemPos, cwaPrefRouteNwElemTable=cwaPrefRouteNwElemTable, cwaPrefRouteNwElemPortId=cwaPrefRouteNwElemPortId, PYSNMP_MODULE_ID=ciscoWanATMPrefRouteMIB, ciscoWanATMPrefRouteMIBObjects=ciscoWanATMPrefRouteMIBObjects, cwaPrefRouteCompliances=cwaPrefRouteCompliances, cwaPrefRouteMIBGroups=cwaPrefRouteMIBGroups, cwaPrefRouteRowStatus=cwaPrefRouteRowStatus, cwaPrefRouteConfTable=cwaPrefRouteConfTable, cwaPrefMIBGroups=cwaPrefMIBGroups, cwaPrefRouteConformance=cwaPrefRouteConformance, cwaPrefMIBCompliance=cwaPrefMIBCompliance, ciscoWanATMPrefRouteMIBNotifs=ciscoWanATMPrefRouteMIBNotifs, cwaPrefRouteConfEntry=cwaPrefRouteConfEntry, ciscoWanATMPrefRouteMIB=ciscoWanATMPrefRouteMIB)
